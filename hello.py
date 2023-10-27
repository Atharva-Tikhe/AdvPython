from flask import Flask, render_template, request, jsonify, redirect

app = Flask(__name__)

members = {
    'atharva': '2213',
    'abc': '000',
    'xyz': '123'
}


@app.route('/')
def hello():
    return redirect('/login')

# 27 Oct - practical 
# implement render template

@app.route('/login')
def serve_login():
    return render_template("login.html")
 
@app.route('/login_process', methods = ["POST"])
def get_form_data():
    return jsonify({"username": request.form.get("username"), "password": request.form.get("password")})


    


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
