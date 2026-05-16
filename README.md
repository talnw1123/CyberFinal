# KMUTT Crypto Incident Lab

เว็บ CTF Lab สำหรับโจทย์ข้อ 1 วิทยาการรหัสลับ หัวข้อ AES-CTR nonce reuse ในบริบทการสืบสวนเหตุการณ์ความมั่นคงปลอดภัยไซเบอร์

## Run Local

```bash
pip install -r requirements.txt
python app.py
```

เปิด `http://localhost:5000`

## Docker

```bash
docker build -t kmutt-crypto-lab .
docker run -p 5000:5000 kmutt-crypto-lab
```

## Deploy บน Render

1. Push โฟลเดอร์นี้ขึ้น GitHub
2. ไปที่ Render แล้วเลือก New Web Service
3. เลือก repository นี้
4. Render จะอ่าน `render.yaml` หรือเลือก Runtime เป็น Docker ด้วยตนเอง
5. Instance type: Free
6. Deploy แล้วนำ URL ที่ได้ไปแนบในรายงาน

Health check path:

```text
/health
```

## Artifact

- `network_capture.json`: ciphertext สองชุดที่ใช้ AES-128-CTR nonce เดียวกัน
- `leaked_plaintext.txt`: plaintext ของ note A ที่พบจาก memory artifact
- `solver_template.py`: template สำหรับเขียน solver

## Flag

ระบบตรวจ flag นี้:

```text
KMUTT{CTR_NONCE_REUSE_EXPOSES_SECRET}
```
