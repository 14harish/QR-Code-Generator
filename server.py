from flask import Flask,render_template,request
import qrcode
from io import BytesIO
from base64 import b64encode

app=Flask(__name__)
val="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAASIAAAEiAQAAAAB1xeIbAAABD0lEQVR4nO3YUQ6DIAyAYRIP4JG8ukfiACYM2sLYpnMPlmXL3wdB+HhqtEBIH8QaUCgUCvUXKlhMuR9zu8Q6sqC8lbykOCWhWU2pm0C5Ks3LPUPNo4apEOaUUF9RaUWNVtJEGd6C9LoJlKdqFVmTc1a3UdepLsrX8TKG8lOWDfk9la9jnesD5a9mSU6ZkwW5Z7UZ5ax0/2knMNsSydhDhlAeqmaoec2VlWWUp6ovdSfaLUINUSX0f2QHgO1oN4S6TgWLegqw5OzWbdTFShKh5y49fG26OUINUO3Wp83JyqO7IZSX0ljic91G+arulh81RklTb9yE7uxXUR6qq8ix3i+/rduoq9RJoFAoFOrn1Q3zZ0A5hJw3NgAAAABJRU5ErkJggg=="

@app.route('/')
def Home():
    return render_template("qr.html",data=val)
@app.route('/',methods=["POST"])
def generateQR():
    memory=BytesIO()
    data=request.form.get('link')
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(back_color=(255, 195, 235), fill_color=(55, 95, 35))
    img.save(memory)
    memory.seek(0)
    img.save("hllo.png")

    base64_img = "data:image/png;base64," + b64encode(memory.getvalue()).decode('ascii')
    return render_template("qr.html", data=base64_img)

if __name__=="__main__":
    app.run(debug=True)