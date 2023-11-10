from flask import Flask, render_template, request,url_for,redirect,session,flash;
#from flask_mysqldb import MySQL
from pymysql import connections
import os
from config import *
from sql import *
from ipregistry import IpregistryClient


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

@app.route("/EditAdmin/<string:id>", methods=['GET','POST'])
def EditAdmin(id):

    cursor = db_conn.cursor()

    if(request.method == 'GET'):


        try:
            cursor.execute(getAdminById,(id))
            
            data = cursor.fetchone()
  
            if(data):
 
                return render_template('editAdmin.html',data = data)

            cursor.close()
        except Exception as e:
            print(e.__traceback__)
            cursor.close()
            return redirect(url_for('Error'))
        
    elif(request.method == 'POST'):
        print(id)
        print("post")
        edit_password = request.form['password']
        new_role = request.form.getlist('permission-item')
        edit_role = "{" + ", ".join(new_role ) + "}"
        print(edit_role)
        
        cursor.execute(updateAdminDetail,(edit_password,edit_role,"7"))
        db_conn.commit()

        return redirect(request.referrer)


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
            

            # client = IpregistryClient("checkin")  
            # ipInfo = client.lookup() 
            # ip = ipInfo.ip
            # print(ipInfo)

            # cursor.execute(updateAdminDevice,(ip,data[0]))
            # db_conn.commit()
            cursor.close()
            return redirect(url_for('Home'))
        else:
            flash('Login unsuccesful')
            cursor.close()
            return redirect(url_for('Login'))
        
    except Exception as e:
        print(e.__cause__)
        cursor.close()
        return redirect(url_for('Error'))
        
    

@app.route("/AddAdmin", methods=['POST'])
def AddAdmin():
    register_id = request.form['username']
    register_password = request.form['password']
    checked_permission = request.form.getlist('permission-item')
    register_permission = "{" + ", ".join(checked_permission ) + "}"

    cursor = db_conn.cursor()

    try:
        cursor.execute(addAdmin,(1,register_id,register_password,register_permission))
        flash('Admin Added Successfully')
        db_conn.commit()
        cursor.close()

        return redirect(url_for('Admin'))

        
    except Exception as e:
        cursor.close()
        print(e.__cause__)
        return redirect(url_for('Error'))
        


@app.route("/DeleteAdmin/<string:id>")
def DeleteAdmin(id):
    cursor = db_conn.cursor()

    try:
        cursor.execute(deleteAdmin,(id))
        flash('Admin Added Successfully')
        db_conn.commit()
        cursor.close()

        client = IpregistryClient("tryout")  
        ipInfo = client.lookup() 
        print(ipInfo)

        return redirect(url_for('Admin'))

        
    except Exception as e:
        cursor.close()
        print(e.__cause__)
        return redirect(url_for('Error'))


@app.route("/AddShop", methods=['POST'])
def AddShop():
    new_name = request.form['name']
    new_location = request.form['location']
    new_desc = request.form['description']
    checked_permission = request.form.getlist('permission-item')
    register_permission = "{" + ", ".join(checked_permission ) + "}"

    url = "https://mall-assistant-system.s3.amazonaws.com/adminLogin-bg.jpg"
    tag = "testing"

    cursor = db_conn.cursor()


    cursor.execute(addShop,('1',new_name, new_location, new_desc, url ,tag))

    flash('Shop Added Successfully')
    db_conn.commit()
    cursor.close()
    return redirect(url_for('Shop'))

@app.route("/DeleteShop/<string:id>")
def DeleteShop(id):
    cursor = db_conn.cursor()

    try:
        cursor.execute(deleteAdmin,(id))
        flash('Shop Deleted Successfully')
        db_conn.commit()
        cursor.close()

        return redirect(url_for('Shop'))

        
    except Exception as e:
        cursor.close()
        print(e.__cause__)
        return redirect(url_for('Error'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)