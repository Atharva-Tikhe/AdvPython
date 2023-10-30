from flask import Flask, render_template, request, jsonify, redirect
import mysql.connector as conn
app = Flask(__name__)

connection = conn.connect(user = 'root', passwd = 'mitbio', host='127.0.0.1', db = 'login')

cursor = connection.cursor()


@app.route('/')
def hello():
    return redirect('/login')

# 27 Oct - practical 
# implement render template

@app.route('/login')
def serve_login():
    return render_template("login.html", error='')
 
@app.route('/login_process', methods = ["POST"])
def get_form_data():
    username = request.form.get("username")
    passwd = request.form.get("password")
    
    
    cursor.execute(f"select * from `login.users` where username = '{username}' and pass = '{passwd}';")
    result = cursor.fetchall()
    print(result)
    
    if len(result) == 1:
        cursor.execute(f'select * from `user.info` where username = "{username}"')
        user_details = cursor.fetchall()
        print(user_details)
        return render_template("user_info.html", username = result[0][0])
    else:
        return render_template("login.html", error = "Incorrect username or password")



    


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
