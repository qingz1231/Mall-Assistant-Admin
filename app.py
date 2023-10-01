from flask import Flask, render_template, request,url_for,redirect,session,flash;
#from flask_mysqldb import MySQL
from pymysql import connections
import os
from config import *
from sql import *

app = Flask(__name__)
app.secret_key = 'admin'
app.config['MYSQL_HOST']= customhost
app.config['MYSQL_USER']= customuser
app.config['MYSQL_PASSWORD']= custompass
app.config['MYSQL_DB']= customdb
db_conn = connections.Connection(
    host=customhost,
    port=3306,
    user=customuser,
    password=custompass,
    db=customdb
)
output = {}
studentTable = 'student'
companyTable = 'company'

#pages
@app.route("/")
def Register():
    return render_template('login.html')



@app.route("/Login")
def Login():
    return render_template('Login.html')

@app.route("/Error")
def Error():
    return render_template('error.html')

@app.route("/Home")
def Home():
    return render_template('index.html')

@app.route("/Admin")
def Admin():
    cursor = db_conn.cursor()
    try:
        cursor.execute(getAllAdmin)
        data  = cursor.fetchall()

    except Exception as e:
        cursor.close()
        return redirect(url_for('Error'))
    

    cursor.close()
    return render_template('admin.html',admins=data)

@app.route("/Shop")
def Shop():
    cursor = db_conn.cursor()
    try:
        cursor.execute(getAllShop)
        data  = cursor.fetchall()

    except Exception as e:
        cursor.close()
        return redirect(url_for('Error'))
    

    cursor.close()
    return render_template('shop.html',shops=data)



# @app.route("/CompanyDetailsPage/<string:id>")
# def CompanyDetailsPage(id):
#     cursor = db_conn.cursor()
#     getById_sql = "SELECT * FROM company WHERE id=%s"
#     cursor.execute(getById_sql,(id))
#     company = cursor.fetchone()
#     cursor.close()
#     return render_template('CompanyDetailsPage.html',company=company)
@app.route("/LoginAdmin", methods=['POST'])
def LoginAdmin():
    login_id = request.form['username']
    login_pass = request.form['password']

    cursor = db_conn.cursor()

    try:
        cursor.execute(getAdminByLogin,(login_id,login_pass))
        data = cursor.fetchone()

        if(data):
            flash('Login succesful')
            session["user"] = data
            cursor.close()
            return redirect(url_for('Home'))
        else:
            flash('Login unsuccesful')
            cursor.close()
            return redirect(url_for('Login'))
        
    except Exception as e:
        cursor.close()
        return redirect(url_for('Error'))
        
    

   
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)