import json
from pathlib import Path


def xor_bytes(left: bytes, right: bytes) -> bytes:
    return bytes(a ^ b for a, b in zip(left, right))


base_dir = Path(__file__).resolve().parent / "artifacts"
capture = json.loads((base_dir / "network_capture.json").read_text(encoding="utf-8"))
known_plaintext = (base_dir / "leaked_plaintext.txt").read_bytes()

note_a = capture["captures"][0]
note_b = capture["captures"][1]

if note_a["nonce_hex"] != note_b["nonce_hex"]:
    raise SystemExit("Nonce values differ; this reference solve expects nonce reuse.")

ciphertext_a = bytes.fromhex(note_a["ciphertext_hex"])
ciphertext_b = bytes.fromhex(note_b["ciphertext_hex"])

keystream = xor_bytes(ciphertext_a, known_plaintext)
plaintext_b = xor_bytes(ciphertext_b, keystream)

print(plaintext_b.decode("utf-8"))
