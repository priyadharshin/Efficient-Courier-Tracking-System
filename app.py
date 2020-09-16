
from flask import Flask,request,url_for,redirect,flash,session
from flask import render_template
import json 
from service import *
import os
app = Flask(__name__)




@app.route("/")
def homepage():
	return render_template("homepage.html") 
	
	


@app.route("/view_feedback.html")
def view_feedback():
	
	return render_template("view_feedback.html",data=getfeedback()) 
	
	

@app.route("/paymentbill.html")
def paymentBill():
	if 'username'  in session:
		username=session['username']
		role=session['role']
		result=getcouriorPayemnt(username,role)
		return render_template("paymentbill.html",data=result) 		
	else:
		return redirect("/")
	
@app.route("/bill.html")
def bill():
	if 'username'  in session:
		username=session['username']
		role=session['role']
		result=getcouriorPayemnt(username,role)
		return render_template("bill.html",data=result) 		
	else:
		return redirect("/")	
	
		
@app.route("/trackstatus.html")
def trackstatus():
	return render_template("trackstatus.html") 
	

@app.route("/feed.html")
def feedback():
	return render_template("feed.html")
	
		
@app.route("/Add_courier.html")
def addCouriorFile():
	return render_template("Add_courier.html") 
	

@app.route("/updatecd.html")
def updatecd():
	return render_template("updatecd.html") 
	
@app.route("/adminlogin.html")
def adminLogin():
	return render_template("/adminlogin.html")
	
@app.route("/formlogin.html")
def formLogin():
	return render_template("formlogin.html") 
	



@app.route("/viewstatus.html")
def viewstatus():
	return render_template("viewstatus.html") 
	
@app.route("/admindetails.html")
def admindetails():
	return render_template("admindetails.html") 
	
	

@app.route("/register.html")
def registerHtml():
	return render_template("register.html") 
	
@app.route("/userpage.html")
def userPage():
	return render_template("userpage.html") 


@app.route("/pcourier.html")
def pcourier():
	if 'username'  in session:
			username=session['username']
			data=getplaceUser(username)
			return render_template("pcourier.html",data=data) 
	return redirect("/")
	
@app.route("/payment.html")
def payment():
	return render_template("payment.html") 
		
@app.route("/admin.html")
def admin():
	return render_template("admin.html") 
	
@app.route("/logout")
def logout():
	return redirect("/") 
	
	
	
	
@app.route("/distlg.html")
def distlg():
	return render_template("distlg.html") 
	
	
@app.route("/Distdetails.html")
def Distdetails():
	return render_template("/Distdetails.html") 
	

@app.route("/Listshipment.html")
def Listshipment():
	return render_template("Listshipment.html") 


@app.route("/Add_track.html")
def Add_Track():
	return render_template("Add_track.html") 
	
	
	
@app.route("/Progress.html")
def Progress():
	return render_template("Progress.html") 
	
	


@app.route("/getCouriorStatus",methods=['POST','GET'])
def getCouriorStatus():
	if request.method == "POST":
		cid=request.form['cid']	
		data=getcourior(cid)
		
	return render_template("Progress.html",data=data)

	
@app.route("/register",methods=['POST','GET'])
def register():
	if request.method == "POST":		
		name=request.form['name']
		dob=request.form['dob']
		gender=request.form['gender']
		email=request.form['email']
		passwrd=request.form['passwrd']	
		mobileNo=request.form['mobileNo']	
		city=request.form['city']	
		address=request.form['address']			
		userRegister(name,dob,gender,email,passwrd,mobileNo,city,address)
	return redirect("/")


@app.route("/addCourior",methods=['POST','GET'])
def addCourior():
	if request.method == "POST":		
		senderName=request.form['senderName']
		senderMobNo=request.form['senderMobNo']
		senderCity=request.form['senderCity']
		senderAddress=request.form['senderAddress']
		recName=request.form['recName']	
		recMobile=request.form['recMobile']	
		recCity=request.form['recCity']	
		recAddrress=request.form['recAddrress']
		dateTime=request.form['dateTime']
		ShipmentType=request.form['ShipmentType']
		weight=request.form['weight']
		qtny=request.form['qtny']
		if 'username'  in session:
			username=session['username']
			cstatus="ready"				
			saveCourior(username,senderName,senderMobNo,senderCity,senderAddress,recName,recMobile,recCity,recAddrress,dateTime,ShipmentType,weight,qtny,cstatus)
		cost=int(weight)*55		
	return render_template("payment.html",data=cost)



@app.route("/viewcd.html")
def viewcd():
	if 'role'  in session:
		username=session['username']
		role=session['role']
		data=getPcourier(role,username)
		print(role)
		return render_template("viewcd.html",data=data,role=role) 
		

@app.route("/paymentSave",methods=['POST','GET'])
def addPayment():
	if request.method == "POST":		
		if 'role'  in session:
			username=session['username']
			role=session['role']
			amount=request.form['amount']
			print(username)
			print(amount)
			insertPaymentSave(username,amount)
			print(role)
			return redirect("/userpage.html") 
				
@app.route("/editStatus",methods=['POST','GET'])
def editStatus():
	if request.method == "POST":		
		c_id=request.form['c_id']
		result=getcourior(c_id)
		return render_template("Add_track.html",data=result) 
	


	
@app.route("/addTrack",methods=['POST','GET'])
def addTrack():
	if request.method == "POST":		
		cid=request.form['cid']
		date=request.form['date']
		description=request.form['description']		
		updateCourior(cid,date,description)
	return redirect("/viewcd.html")
		

@app.route("/feedback",methods=['POST','GET'])
def addFeeback():
	if request.method == "POST":		
		cid=request.form['cid']
		email=request.form['email']
		description=request.form['sugestion']		
		insertFeedback(cid,email,description)
	return redirect("/feed.html")
		
		

@app.route("/login",methods=['POST','GET'])
def login():
	if request.method == "POST":	
		username=request.form['username']
		passwrd=request.form['password']
		if username=="admin@gmail.com":
			if passwrd=="admin":
				session["user_id"]=1
				session["username"]="admin@gmail.com"
				session["role"]="admin"
				return redirect("/admindetails.html")				
		result=getLogin(username,passwrd)
		print(len(result))
		if(len(result)>0):	
			session["userObj"]=result
			for x in result:
				print(x)
				session["user_id"]=x[0]
				session["username"]=x[1]
				session["role"]=x[4]
				print("------------------------role-------"+x[4])
				if(x[4]=="admin"):
					return redirect("/admindetails.html")					
			return redirect("/userpage.html")
		
		return render_template("formlogin.html",status="username or password is wrong")


def sentMail():
	msg = Message("Send Mail Tutorial!",
	sender="aravindkumark1997@gmail.com",
	recipients=["haifriends1997@gmail.com"])
	msg.body = "Yo!\nHave you heard the good word of Python???"           
	mail.send(msg)
	return 'Mail sent!'
	


@app.route("/adminlogin",methods=['POST','GET'])
def adminlogin():
	if request.method == "POST":
		username=request.form['username']
		passwrd=request.form['password']
		if username=="admin@gmail.com":
			if passwrd=="admin":
				session["user_id"]=1
				session["username"]="admin@gmail.com"
				session["role"]="admin"
				return redirect("/admindetails.html")				
		result=getLogin(username,passwrd)
		print(len(result))
		if(len(result)>0):	
			session["userObj"]=result
			for x in result:
				print(x)
				session["user_id"]=x[0]
				session["username"]=x[1]
				session["role"]=x[4]
				print("------------------------role-------"+x[2])
				if(x[4]=="admin"):
					return redirect("/admindetails.html")					
			
		
		return render_template("adminlogin.html",status="username or password is wrong")
	



@app.route("/distLogin",methods=['POST','GET'])
def distLogin():
	if request.method == "POST":
		username=request.form['username']
		passwrd=request.form['password']
		if username=="distributor@gmail.com":
			if passwrd=="distributor":
				session["user_id"]=1
				session["username"]="distributor@gmail.com"
				session["role"]="distributor"
				return redirect("/Distdetails.html")				
		result=getLogin(username,passwrd)
		print(len(result))
		if(len(result)>0):	
			session["userObj"]=result
			for x in result:
				print(x)
				session["user_id"]=x[0]
				session["username"]=x[1]
				session["role"]=x[4]
				print("------------------------role-------"+x[2])
				if(x[4]=="distributor"):
					return redirect("/Distdetails.html")					
			
		
		return render_template("distlg.html",status="username or password is wrong")
	
	
	
	

@app.route("/StudentSave",methods=['POST','GET'])
def StudentSave():
	if request.method == "POST":
		name=request.form['name']
		degree=request.form['degree']
		phone=request.form['phone']
		address=request.form['address']
		stdSave(name,degree,phone,address)
	return render_template("index.html")
	
@app.route("/studentget",methods=['POST','GET'])
def studentget():
	result = None
	if request.method == "GET":
		result=getstudent()
	
	return json.dumps({'result':result});
	



if __name__=="__main__":
	app.secret_key = "abc"  
	app.run(debug=True)
