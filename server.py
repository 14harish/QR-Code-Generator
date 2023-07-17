from flask import Flask,render_template,request
import qrcode
from io import BytesIO
from base64 import b64encode

app=Flask(__name__)

@app.route('/')
def Home():
    return render_template("qr.html")
@app.route('/',methods=["POST"])
def generateQR():
    memory=BytesIO()
    data=request.form.get('link')
    img=qrcode.make(data)
    img.save(memory)
    memory.seek(0)
    img.save("hllo.png")

    base64_img = "data:image/png;base64," + b64encode(memory.getvalue()).decode('ascii')
    return render_template("qr.html", data=base64_img)

if __name__=="__main__":
    app.run(debug=True)