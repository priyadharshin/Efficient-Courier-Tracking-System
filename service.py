from connection import *
import smtplib 




def userRegister(name,dob,gender,email,passwrd,mobileNo,city,address):
	mycursor = conn.cursor()
	sql = "INSERT INTO userRegisteration (name,dob,gender,email,mobileNo,city,address) VALUES (%s, %s, %s, %s ,%s ,%s,%s)"
	val = (name,dob,gender,email,mobileNo,city,address)
	mycursor.execute(sql, val)
	conn.commit()
	loginSave(email,passwrd,"user","active")
	
	

def loginSave(email,password,uRole,status):
	mycursor = conn.cursor()
	sql = "INSERT INTO login (username,passwrd,uRole,status) VALUES (%s, %s, %s, %s)"
	val = (email,password,uRole,status)
	mycursor.execute(sql, val)
	conn.commit()
	
	
def getLogin(username,passwrd):
	mycursor = conn.cursor()
	query="SELECT * FROM login where username='"+username+"'  and passwrd='"+passwrd+"' "
	print(query)
	mycursor.execute(query)
	myresult = mycursor.fetchall()
	#print("-------------------------"+myresult[0])
	for x in myresult:
		print(x)  
	return myresult

def stdSave(name,degree,phone,address):
	mycursor = conn.cursor()
	sql = "INSERT INTO student (name, degree,phone,address) VALUES (%s, %s, %s, %s)"
	val = (name,degree,phone,address)
	mycursor.execute(sql, val)
	conn.commit()
	
def getstudent():
	mycursor = conn.cursor()
	mycursor.execute("SELECT * FROM student")
	myresult = mycursor.fetchall()
	return myresult

def saveCourior(username,senderName,senderMobNo,senderCity,senderAddress,recName,recMobile,recCity,recAddrress,dateTime,ShipmentType,weight,qtny,cstatus):
	mycursor = conn.cursor()
	sql = "INSERT INTO placeCourier (cstatus,username,senderName,senderMobNo,senderCity,senderAddress,recName,recMobile,recCity,recAddrress,dateTime,ShipmentType,weight,qtny) VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s)"
	val = (cstatus,username,senderName,senderMobNo,senderCity,senderAddress,recName,recMobile,recCity,recAddrress,dateTime,ShipmentType,weight,qtny)
	mycursor.execute(sql, val)
	conn.commit()
	
def getPcourier(role,username):
	query=""
	if role=="admin" or role=="distributor":
		query="SELECT id,senderName,recName,dateTime,cstatus FROM placeCourier"
	else:
		query="SELECT id,senderName,recName,dateTime,cstatus FROM placeCourier where username='"+username+"'"
	mycursor = conn.cursor()
	mycursor.execute(query)
	myresult = mycursor.fetchall()
	return myresult


def getStatus(cid,date,description):
	query="SELECT id,senderName,recName,dateTime,cstatus FROM placeCourier where id='"+cid+"'"
	mycursor = conn.cursor()
	mycursor.execute(query)
	myresult = mycursor.fetchone()
	return myresult
	
def getfeedback():
	query="SELECT * from feedback"
	mycursor = conn.cursor()
	mycursor.execute(query)
	myresult = mycursor.fetchall()
	return myresult
	
	
	
	
	
	
def getcourior(c_id):
	query="SELECT id,senderName,recName,dateTime,cstatus FROM placeCourier where id='"+c_id+"'"
	mycursor = conn.cursor()
	mycursor.execute(query)
	myresult = mycursor.fetchone()
	return myresult
	
def updateCourior(cid,date,description):
	query="update placeCourier set dateTime='"+date+"',cstatus='"+description+"' where id="+cid+""
	mycursor = conn.cursor()
	mycursor.execute(query)
	
	
def insertFeedback(cid,email,description):
	mycursor = conn.cursor()
	sql = "INSERT INTO feedback (courier_id,email,description,username) VALUES (%s, %s, %s, %s )"
	val = (cid,email,description,email)
	mycursor.execute(sql, val)
	conn.commit()
	
	
def getcouriorPayemnt(username,role):
	query=""
	if role in "admin":
		query="select id,senderName,ShipmentType,amount from placeCourier"
	else:
		query="SELECT id,senderName,ShipmentType,amount FROM placeCourier where username='"+username+"'"
	print(query)
	mycursor = conn.cursor()
	mycursor.execute(query)
	myresult = mycursor.fetchall()
	return myresult
	

def insertPaymentSave(username,amount):
	query="update placeCourier set amount='"+amount+"' where username='"+username+"'"
	print(query)
	mycursor = conn.cursor()
	mycursor.execute(query)
	conn.commit()
	

def getplaceUser(username):
	query="select name,mobileno,city,address from userRegisteration where email='"+username+"'"
	print(query)
	mycursor = conn.cursor()
	mycursor.execute(query)
	myresult = mycursor.fetchone()
	return myresult
	
