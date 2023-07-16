import qrcode

qr=qrcode.QRCode(version=2,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=60,border=1)

qr.add_data("https://leetcode.com/")
qr.make(fit=True)

img=qr.make_image(fill_color="red",back_color="blue")
img.save("qr1.png")