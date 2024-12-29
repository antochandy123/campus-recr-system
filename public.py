from flask import *
from database import *
import uuid
public=Blueprint('public',__name__)

@public.route('/')
def home():
	return render_template("home.html")


@public.route('/login',methods=['get','post'])
def login():
	session.clear()
	if 'submit' in request.form:
		username=request.form['username']
		password=request.form['password']
		q="SELECT * FROM `login` WHERE `username`='%s' AND `password`='%s'"%(username,password)
		res=select(q)
		if not res:
			flash('INCORRECT USERNAME OR PASSWORD')
		if res:
			session['lid']=res[0]['login_id']
			if res[0]['user_type']=='admin':
				flash('HELLO ADMIN')
				return redirect(url_for("admin.admin_home"))
			elif res[0]['user_type']=='career_guidance':
				lid=res[0]['login_id']
				q="SELECT * FROM `career_guidance` WHERE `login_id`='%s'"%(lid)
				re=select(q)
				session['id']=re[0]['career_guidance_id']
				flash('HELLO GUIDANCE TEAM')
				return redirect(url_for("career_guidance.career_guidance_home"))
			elif res[0]['user_type']=='institute':
				lid=res[0]['login_id']
				q="SELECT * FROM `institutes` WHERE `login_id`='%s'"%(lid)
				re=select(q)
				session['id']=re[0]['institute_id']
				flash('HELLO INSTITUTE')
				return redirect(url_for("college.college_home"))
			elif res[0]['user_type']=='student':
				lid=res[0]['login_id']
				q="SELECT * FROM `students` WHERE `login_id`='%s'"%(lid)
				re=select(q)
				session['id']=re[0]['student_id']
				flash('HELLO STUDENT')
				return redirect(url_for("student.student_home"))

	return render_template("login.html")


@public.route('/career_guidance_Register',methods=['get','post'])
def career_guidance_Register():
	if 'submit' in request.form:
		tname=request.form['tname']
		place=request.form['place']
		landmark=request.form['landmark']
		pin=request.form['pin']
		phone=request.form['phone']
		email=request.form['email']
		uname=request.form['uname']
		pwd=request.form['pwd']
		q="SELECT * FROM `login` WHERE `username`='%s'"%(uname)
		res=select(q)
		if res:
			flash('USERNAME ALREADY EXIST')
			return redirect(url_for("public.career_guidance_Register"))
		else:
			q="INSERT INTO `login`(`username`,`password`,`user_type`) VALUES ('%s','%s','career_guidance_pending')"%(uname,pwd)
			id=insert(q)
			q="INSERT INTO `career_guidance` (`login_id`,`team_name`,`office_place`,`land_mark`,`pincode`,`phone`,`email`,`status`) VALUES ('%s','%s','%s','%s','%s','%s','%s','pending')"%(id,tname,place,landmark,pin,phone,email)
			insert(q)
			flash('REGISTERED')
			return redirect(url_for("public.career_guidance_Register"))
	return render_template("career_guidance_Register.html")


