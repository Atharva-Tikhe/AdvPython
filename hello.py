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
    return render_template("login.html", error='', pw_error='')
 
@app.route('/login_process', methods = ["POST"])
def get_form_data():
    username = request.form.get("username")
    passwd = request.form.get("password")
    if username in members.keys():
        if members[username] == passwd:
            return f'Welcome {username}'
        else:
            return render_template("login.html", pw_error = "Incorrect password")
    else:
        return render_template("login.html", error = "Incorrect username")


    


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
