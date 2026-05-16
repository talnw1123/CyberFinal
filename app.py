import os
from pathlib import Path

from flask import Flask, abort, render_template, request, send_from_directory


BASE_DIR = Path(__file__).resolve().parent
ARTIFACT_DIR = BASE_DIR / "artifacts"

FLAG = "KMUTT{CTR_NONCE_REUSE_EXPOSES_SECRET}"
ALLOWED_ARTIFACTS = {
    "network_capture.json",
    "leaked_plaintext.txt",
    "solver_template.py",
}

app = Flask(__name__)


@app.get("/health")
def health():
    return {"status": "ok", "service": "kmutt-crypto-incident-lab"}


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    submitted_flag = ""

    if request.method == "POST":
        submitted_flag = request.form.get("flag", "").strip()
        result = submitted_flag == FLAG

    return render_template(
        "index.html",
        artifacts=sorted(ALLOWED_ARTIFACTS),
        result=result,
        submitted_flag=submitted_flag,
        flag=FLAG if result else None,
    )


@app.get("/download/<path:filename>")
def download_artifact(filename):
    if filename not in ALLOWED_ARTIFACTS:
        abort(404)
    return send_from_directory(ARTIFACT_DIR, filename, as_attachment=True)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=False)
