import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,)
qr.add_data('https://leetcode.com/')
qr.make(fit=True)

img = qr.make_image(fill_color="orange", back_color="white")
img.save("Agro_Mart.png")