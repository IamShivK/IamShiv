from flask import Flask,render_template, request
from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'shiv95'
app.config['MYSQL_DB'] = 'flask'
 
mysql = MySQL(app)

"""@app.route('/login',methods=['POST'])
def form():
	if request.method =='POST':
		print("Data : ",request.form)
		Username= request.form['Username']
		Email = request.form['Email']
		password=request.form['password']

		cur=mysql.connection.cursor()
		cur.execute("INSERT INTO logins (Username,Email,password) VALUES (%s,%s,%s)",(Username,Email,password))
		mysql.connection.commit()
		cur.close()
		return "sucess"
	return render_template('form.component.html')"""



@app.route('/form')
def form():
    return render_template('form.componenet.html')
 
@app.route('/create', methods = ['POST', 'GET'])
def create():

	if request.method == 'GET':
		    return "Login via the login Form"
     
	if request.method == 'POST':
		Username = request.form['Username']
		Email = request.form['Email']
		password = request.form['password']
		cursor = mysql.connection.cursor()
		cursor.execute(''' INSERT INTO logins VALUES(%s,%s,%s)''',(Username,Email,password))
		mysql.connection.commit()
		cursor.close()
		return "Done!!"
 
app.run(host='localhost', port=5000)
