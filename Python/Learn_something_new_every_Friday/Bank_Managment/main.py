from flask import Flask,render_template,session,request
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app=Flask(__name__)

#Secret key
app.secret_key='super-secret-key'

#Databse connection details
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='parag123'
app.config['MYSQL_DB']='bank_management'

#Inititalize MYSQL
mysql=MySQL(app)

@app.route('/',methods=['GET','POST'])
def login():
    msg=''
    if request.method=='POST' and 'username' in request.form and 'password' in request.form :
        username=request.form['username']
        password=request.form['password']
        cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('select * from accounts where username=%s and password=%s',(username,password))
        account=cursor.fetchone()
        if account:
            #create session data
            session['loggedin']=True
            session['id']=account['account_id']
            return 'Logged in succesfully'
        else:
            msg = 'Incorrect username or password'
    return render_template('index.html',msg=msg)

@app.route('/register',methods=['GET','POST'])
def register():
    msg=''
    if request.method=='POST' and 'firstname' in request.form and 'lastname' in request.form and 'age' in request.form  and 'username' in request.form and 'password' in request.form:
        firstname=request.form['firstname']
        lastname=request.form['lastname']
        age=request.form['age']
        username=request.form['username']
        password=request.form['password']
        email=request.form['email']
        print(firstname,lastname,age,username,password,email)
        cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("select * from accounts where username=%s",(username,))
        account=cursor.fetchone()

        if account:
            msg='Account already exit'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+',email):
            msg='Invalid email address'
        elif not re.match(r'[A-Za-z0-9]+',username):
            msg='Username must contain only characters and nubers!!'
        elif not username or not password or not email:
            msg='Please fill out the form'
        else:
            cursor.execute('INSERT INTO details VALUES (NULL, %s,%s,%s,%s,%s,%s)',(firstname,lastname,age,username,password,email))
            mysql.connection.commit()
            msg='You have successfully registered please login'
            return render_template('index.html',msg=msg)

    elif request.method=='POST':
        msg='Fill the form BSDK'
    return render_template('register.html',msg=msg)

app.run(debug=True)