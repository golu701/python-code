# pip install pyqrcode
# pip install pypng

import pyqrcode
import png
from pyqrcode import QRCode
qrstring= "https://github.com/golu701"
url = pyqrcode.create(qrstring)
url.png('./qr.png',scale=8)
