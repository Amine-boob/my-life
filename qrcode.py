# QRCode
import qrcode

url = "https://youtu.be/mrV8kK5t0V8"
file_path = "C:\\Users\\hhh\\Desktop\\image.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)



# QRCode (new version)
import qrcode
import os

path = os.path.expanduser("~/Desktop")
url = input("enter the URL :")
file_name = input("enter a file name :")
file_path = os.path.join(path,file_name)
qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)
print("QR Code successfully created")
