# Encoded By MUMIT ISLAM HIMU
# Py3 Marshal+Zlib+B64 Encryption
# https://github.com/MUMIT-404-CYBER

import marshal, base64, zlib

exec(marshal.loads(zlib.decompress(base64.b64decode(b'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'))))