from flask import *
from database import *
college=Blueprint('college',__name__)

@college.route('/college_home',methods=['get','post'])
def college_home():
	if not session.get("lid") is None:

		return render_template("college_home.html")
	else:
		return redirect(url_for('public.login'))



@college.route('/college_Manage_courses',methods=['get','post'])
def college_Manage_courses():
	if not session.get("lid") is None:
		data={}
		id=session['id']
		q="SELECT * FROM `courses` INNER JOIN `institutes` USING (`institute_id`) WHERE `institute_id`='%s'"%(id)
		data['view']=select(q)
		if not data['view']:
			flash("NO COURCES REGISTERED")
		if 'submit' in request.form:
			course=request.form['course']
			des=request.form['des']
			q="INSERT INTO `courses`(`institute_id`,`course_name`,`description`) VALUES ('%s','%s','%s')"%(id,course,des)
			insert(q)
			flash('COURSE ADDED')
			return redirect(url_for("college.college_Manage_courses"))
		if 'action' in request.args:
			action=request.args['action']
			id=request.args['id']
		else:
			action=None
		if action=='delete':
			q="DELETE FROM `courses` WHERE `course_id`='%s'"%(id)
			delete(q)
			flash("deleted")
			return redirect(url_for("college.college_Manage_courses"))
		return render_template("college_Manage_courses.html",data=data)
	else:
		return redirect(url_for('public.login'))



@college.route('/college_Manage_students',methods=['get','post'])
def college_Manage_students():
	if not session.get("lid") is None:
		data={}
		id=session['id']
		q="SELECT * FROM `students` INNER JOIN `courses` USING (`course_id`) WHERE `institute_id`='%s' ORDER BY `student_id` DESC"%(id)
		data['students']=select(q)
		q="SELECT * FROM `courses` WHERE `institute_id`='%s'"%(id)
		data['course']=select(q)
		if 'submit' in request.form:
			fname=request.form['fname']
			lname=request.form['lname']
			hname=request.form['hname']
			place=request.form['place']
			pin=request.form['pin']
			course=request.form['course']
			phone=request.form['phone']
			email=request.form['email']
			uname=request.form['uname']
			pwd=request.form['pwd']
			q="SELECT * FROM `login` WHERE `username`='%s'"%(uname)
			res=select(q)
			if res:
				flash('USERNAME ALREADY EXIST')
				return redirect(url_for("college.college_Manage_students"))
			else:
				q="INSERT INTO `login`(`username`,`password`,user_type) VALUES ('%s','%s','student')"%(uname,pwd)
				lid=insert(q)
				q="INSERT INTO `students`(`login_id`,`first_name`,`last_name`,`house_name`,`place`,`pincode`,`course_id`,`phone`,`email`) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(lid,fname,lname,hname,place,pin,course,phone,email)
				insert(q)
				flash('REGISTERED')
				return redirect(url_for("college.college_Manage_students"))
		if 'action' in request.args:
			action=request.args['action']
			lid=request.args['id']
		else:
			action=None
		if action=='delete':
			q="DELETE FROM `login` WHERE `login_id`='%s'"%(lid)
			delete(q)
			q="DELETE FROM `students` WHERE `login_id`='%s'"%(lid)
			delete(q)
			return redirect(url_for("college.college_Manage_students"))
		if action=='update':
			q="SELECT * FROM `students` WHERE `login_id`='%s'"%(lid)
			data['updatess']=select(q)
			cid=data['updatess'][0]['course_id']
			print(cid)
			q="SELECT `course_id`,`course_name`,(`course_id`='%s') AS sel FROM `courses` where institute_id='%s' ORDER BY sel DESC,`course_id` ASC"%(cid,id)
			print(q)
			data['course_up']=select(q)
		if 'updat' in request.form:
			fname=request.form['fname']
			lname=request.form['lname']
			hname=request.form['hname']
			place=request.form['place']
			pin=request.form['pin']
			course=request.form['course']
			phone=request.form['phone']
			email=request.form['email']
			q="UPDATE `students` SET `first_name`='%s',`last_name`='%s',`house_name`='%s',`place`='%s',`pincode`='%s',`course_id`='%s',`phone`='%s',`email`='%s' WHERE `login_id`='%s'"%(fname,lname,hname,place,pin,course,phone,email,lid)
			update(q)
			flash("UPDATED")
			return redirect(url_for("college.college_Manage_students"))
		return render_template("college_Manage_students.html",data=data)
	else:
		return redirect(url_for('public.login'))



@college.route('/college_View_job_opening',methods=['get','post'])
def college_View_job_opening():
	if not session.get("lid") is None:
		data={}
		q="SELECT *,`vacancies`.`status` AS vstatus FROM `vacancies` INNER JOIN `career_guidance` USING (`career_guidance_id`) ORDER BY `vstatus`"
		data['view']=select(q)
		if not data['view']:
			flash("NO VACANCIES REGISTERED")
		return render_template("college_View_job_opening.html",data=data)
	else:
		return redirect(url_for('public.login'))



@college.route('/college_View_rating',methods=['get','post'])
def college_View_rating():
	if not session.get("lid") is None:
		data={}
		q="SELECT * FROM `ratings` INNER JOIN `students` USING (`student_id`) INNER JOIN `career_guidance` USING (`career_guidance_id`) ORDER BY `rate_id` DESC"
		data['view']=select(q)
		if not data['view']:
			flash("NO STUDENTS RATED")
		return render_template("college_View_rating.html",data=data)
	else:
		return redirect(url_for('public.login'))



@college.route('/college_View_seminars',methods=['get','post'])
def college_View_seminars():
	if not session.get("lid") is None:
		data={}
		
		q="SELECT * FROM `seminars`  ORDER BY `seminar_id` DESC"
		data['view']=select(q)
		return render_template("college_View_seminars.html",data=data)
	else:
		return redirect(url_for('public.login'))



# @college.route('/college_home',methods=['get','post'])
# def college_home():
# 	if not session.get("lid") is None:

# 		return render_template("college_home.html")
# 	else:
# 		return redirect(url_for('public.login'))


