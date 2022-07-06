from ast import keyword
from queue import Empty
import pymongo

from datetime import date

from pymongo import MongoClient

from flask import Flask, render_template, request,url_for, redirect, session



app = Flask(__name__)

app.secret_key = "secret"

client = MongoClient(host='mongodb',
                         port=27017,)
db = client["DigitalNotes"]

 



@app.route("/", methods=['post', 'get'])     
def index():
    admin_found = db.users.find_one({"username": "admin"})
    if not admin_found:
        db.users.insert_one({'email': 'admin@gmail.com', 'username': "admin", 'password': 'admin', 'type': "admin_user"})
    message = ''

    if request.method == "POST":
            if request.form["bt"] == "Sign Up":
                email = request.form.get('email')
                username = request.form.get('username')
                fullname = request.form.get('fullname')
                password = request.form.get('password')
                
            
                user_found = db.users.find_one({"username": username})
                email_found = db.users.find_one({"email": email})
                if user_found:
                    message = 'This username already exists'
                    return render_template('home.html', message=message)
                if email_found:
                    message = 'This email already exists'
                    return render_template('home.html', message=message)
                else:
                    user_input = {'email': email, 'username': username, 'fullname': fullname, 'password': password, 'type': "simple_user"}
                    db.users.insert_one(user_input)
                    
                    user_data = db.users.find_one({"username": username})
                    new_username = user_data['username']

                    session["user"] = new_username
                    
                    return redirect(url_for("user"))
            else:
                email = request.form.get("email_username")
                password_l = request.form.get('password_l')
                username = request.form.get('email_username')
                admin_check = db.users.find_one({"username": username, 'type': "admin_user"})
                admin_check_mail = db.users.find_one({"email": username, 'type': "admin_user"})

                username_found = db.users.find_one({"username": username})
                email_found = db.users.find_one({"email": email})
                
                if email_found:
                    email_val = email_found['email']
                    passwordcheck = email_found['password']

                    if password_l == passwordcheck: 
                        
                        if admin_check_mail:
                            session["user"] = email_found['username']
                            return redirect(url_for('admin'))
                        else:
                            session["user"] = email_found['username']
                            return redirect(url_for('user'))
                    else:
                        message = 'Wrong password'
                        return render_template('home.html', message1=message)
                elif username_found:
                    username_val = username_found["username"]
                    passwordcheck = username_found['password']

                    if password_l == passwordcheck: 
                        if admin_check:
                            session["user"] = username_val
                            return redirect(url_for('admin'))
                        else:
                            session["user"] = username_val
                            return redirect(url_for('user'))
                    else:
                        message = 'Wrong password'
                        return render_template('home.html', message1=message)
                else:
                    message = 'Email or Username not found'
                    return render_template('home.html', message1=message)
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template('home.html')



@app.route('/user',methods=['POST','GET'])
def user():
    simple_user_check = db.users.find_one({"username": session["user"], 'type': "simple_user"})
    if "user" in session and simple_user_check:
        user = session["user"]
        today = str(date.today())
        
        textbox = request.form.get('textbox')

        if request.method == "POST":
        
            if request.form.get("bt3") == "Create":
                title = request.form.get('title')
                noteText = request.form.get('noteText')
                keywords = request.form.get('keywords')
                note_input = {'username': user, 'title': title, 'noteText': noteText, 'keywords': keywords, 'date': today}
                db.notes.insert_one(note_input)
            elif request.form.get("bt6") == "Delete by Title":
                db.notes.delete_one({"title":textbox})
                
                 
        return render_template('logged_in.html', username=user)
    else:
        return redirect("/")


@app.route('/admin',methods=['POST','GET'])
def admin():
    if "user" in session:
        message1 = ""
        user = session["user"]
        if request.method == "POST":
            if request.form.get("bt1") == "Create Admin":
                username = request.form.get('username')
                email = request.form.get('email')
                temppass = request.form.get('password')
                db.users.insert_one({'email': email, 'username': username, 'password': temppass, 'type': "admin_user"})
            elif request.form.get("bt2") == "Delete User":
                user_to_delete = request.form.get('userdelete')
                admin_check = db.users.find_one({"username": user_to_delete, 'type': "admin_user"})
                user_to_delete_found = db.users.find_one({"username": user_to_delete})
                if user_to_delete_found and not admin_check:
                    db.users.delete_one({"username":user_to_delete})
                else:
                    message1 = 'Username not found'
                    return render_template('admin_home.html', message= message1, username=user)
                    
                
        return render_template('admin_home.html', username=user, message = message1 )
    else:
        return redirect("/")



@app.route('/logout')
def logout():
    session.pop("user", None)
    return redirect("/")


@app.route('/delete')
def delete():
    user = session["user"]
    db.users.delete_one({"username":user})
    session.pop("user", None)
    return redirect("/")



if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
    
