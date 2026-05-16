import json
from pathlib import Path


def xor_bytes(left: bytes, right: bytes) -> bytes:
    """Return left XOR right for the shortest shared length."""
    return bytes(a ^ b for a, b in zip(left, right))


base_dir = Path(__file__).resolve().parent
capture = json.loads((base_dir / "network_capture.json").read_text(encoding="utf-8"))
known_plaintext = (base_dir / "leaked_plaintext.txt").read_bytes()

note_a = capture["captures"][0]
note_b = capture["captures"][1]

ciphertext_a = bytes.fromhex(note_a["ciphertext_hex"])
ciphertext_b = bytes.fromhex(note_b["ciphertext_hex"])

# TODO:
# 1. Confirm note_a and note_b reuse the same nonce.
# 2. Recover the CTR keystream with ciphertext_a XOR known_plaintext.
# 3. Decrypt note_b with ciphertext_b XOR recovered_keystream.
# 4. Print the recovered plaintext and submit the flag in the web lab.

if note_a["nonce_hex"] != note_b["nonce_hex"]:
    raise SystemExit("The nonce values are different. Re-check the evidence.")

recovered_keystream = b""  # replace this line
recovered_plaintext_b = b""  # replace this line

print(recovered_plaintext_b.decode("utf-8", errors="replace"))
