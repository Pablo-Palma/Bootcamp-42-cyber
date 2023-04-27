import struct
import time
import hashlib
import hmac

interval = 30
secret_key = "secretkey"

tiempo_actual=int(time.time())
time_slice = int(time.time()) // interval
time_bytes = struct.pack(">Q", time_slice)
hmac_sha1 = hmac.new(secret_key.encode(), time_bytes, hashlib.sha1).digest()
offset = hmac_sha1[-1] & 0x0F
four_bytes = hmac_sha1[offset:offset+4]
value = struct.unpack(">I", four_bytes)[0]
totp = value % 1000000
totp_str = str(totp).zfill(6)

print(totp_str)
