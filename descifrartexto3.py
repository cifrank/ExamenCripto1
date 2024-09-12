from base64 import b64decode
from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad
key_base64 = "c3Bpcml0dXM="
key = b64decode(key_base64)[:8]  # Usar solo los primeros 8 bytes ya que asi es el algoritmo
ciphertext_base64 = """
upa4z5/RUfCx1HVLFKLXOlIYSKb8a7zGn4D+d
lPRATPbnz4N4CCBdKWr978T35iXCktj86og7M
+2Qv260qHwkhbpxM1lXXNFcT/v7cb3UFy/5Q
9md49vA7I0o8XCsZyo7KOTgmRonpzXbHzwX
VOimcfTnh2v9pdggxCumDQ5jVpGrF8S7agqo
+Ogts7I+xWHVtOqtlvtgkwXdypikfDuzZV9/NaQ
CmChulm1No/GnZtPnxYsu5hZcPJN8MRUOUs
s+C9q+oIZGxf04cBbSZnt9RCPFkZcjxRcHLyVn
2TfsR7OJ0sbc4z19MqUxQvXPmb8CsRdgbs6
QQ6fxtJWBvkm6Bu3Leuuu1cNOqHmtjdamc5
xUtpzi7Z4UVWNgk67FIuzQGDcTfThFNumpjIiS
6A7jfQmxT+Y7cQqc4FyIz8+He4hQxCciwCu2X
LtNOFk+GXpM7BKZ5g4rInvOoR24xfLsZ8FVU
CCDOJkWBZJq+LNKuP1p5cq3OXJfGDOTAjT7
a/5pJXSarWTGuLMhrVDXLDLHc/QjOvphAqLb
g1kjbgY76WFZug9iktesLlpdBqpb/+8n8mrkXq
CYy0cZcGlbLMOqgOhcsKSkDzRo08J4dqpQjy
KCQroTltDbw==
"""
ciphertext_base64 = "".join(ciphertext_base64.split())
ciphertext = b64decode(ciphertext_base64)
iv = ciphertext[:8]
ciphertext = ciphertext[8:]
cipher = DES.new(key, DES.MODE_CBC, iv)
padded_plaintext = cipher.decrypt(ciphertext)
# Deshacer el padding (si es necesario)
plaintext = unpad(padded_plaintext, DES.block_size)
# Imprimir el texto en claro
print(plaintext.decode('utf-8', errors='ignore'))