from flask import *
from database import *
admin=Blueprint('admin',__name__)

@admin.route('/admin_home',methods=['get','post'])
def admin_home():
	if not session.get("lid") is None:

		return render_template("admin_home.html")
	else:
		return redirect(url_for('public.login'))






@admin.route('/admin_Manage_schools_and_colleges',methods=['get','post'])
def admin_Manage_schools_and_colleges():
	if not session.get("lid") is None:
		data={}
		q="SELECT * FROM `institutes` ORDER BY `institute_id` DESC"
		data['view']=select(q)
		if 'submit' in request.form:
			name=request.form['name']
			types=request.form['type']
			place=request.form['place']
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
				q="INSERT INTO `login`(`username`,`password`,`user_type`) VALUES ('%s','%s','institute')"%(uname,pwd)
				id=insert(q)
				q="INSERT INTO `institutes` (`login_id`,`name`,`type`,`place`,`pincode`,`phone`,`email`) VALUES ('%s','%s','%s','%s','%s','%s','%s')"%(id,name,types,place,pin,phone,email)
				insert(q)
				flash("REGISTERED")
				return redirect(url_for("admin.admin_Manage_schools_and_colleges"))
		if 'action' in request.args:
			action=request.args['action']
			id=request.args['id']
		else:
			action=None

		if action=='delete':
			q="DELETE FROM `login` WHERE `login_id`='%s'"%(id)
			delete(q)
			q="DELETE FROM `institutes` WHERE `login_id`='%s'"%(id)
			delete(q)
			return redirect(url_for("admin.admin_Manage_schools_and_colleges"))

		if action=='update':
			q="SELECT * FROM `institutes` WHERE `login_id`='%s'"%(id)
			data['updates']=select(q)
		if 'updatess' in request.form:
			name=request.form['name']
			types=request.form['type']
			place=request.form['place']
			pin=request.form['pin']
			phone=request.form['phone']
			email=request.form['email']
			q="UPDATE `institutes` SET `name`='%s',`type`='%s',`place`='%s',`pincode`='%s',`phone`='%s',`email`='%s' WHERE `login_id`='%s'"%(name,types,place,pin,phone,email,id)
			update(q)
			flash('UPDATED')
			return redirect(url_for("admin.admin_Manage_schools_and_colleges"))
		return render_template("admin_Manage_schools_and_colleges.html",data=data)
	else:
		return redirect(url_for('public.login'))






@admin.route('/admin_View_career_guidance_team',methods=['get','post'])
def admin_View_career_guidance_team():
	if not session.get("lid") is None:
		data={}
		q="SELECT * FROM `career_guidance` ORDER BY `career_guidance_id` DESC"
		data['view']=select(q)
		if not data['view']:
			flash('NO DATA FOUND')
		if 'action' in request.args:
			action=request.args['action']
			id=request.args['id']
		else:
			action=None

		if action=="accept":
			q="UPDATE `career_guidance` SET `status`='accepted' WHERE `login_id`='%s'"%(id)
			update(q)
			q="UPDATE `login` SET `user_type`='career_guidance' WHERE `login_id`='%s'"%(id)
			update(q)
			flash('ACCEPTED')
			return redirect(url_for("admin.admin_View_career_guidance_team"))
		if action=="reject":
			q="UPDATE `career_guidance` SET `status`='rejected' WHERE `login_id`='%s'"%(id)
			update(q)
			q="UPDATE `login` SET `user_type`='career_guidance_rejected' WHERE `login_id`='%s'"%(id)
			update(q)
			flash("REJECTED")
			return redirect(url_for("admin.admin_View_career_guidance_team"))

		return render_template("admin_View_career_guidance_team.html",data=data)
	else:
		return redirect(url_for('public.login'))






@admin.route('/admin_View_courses',methods=['get','post'])
def admin_View_courses():
	if not session.get("lid") is None:
		data={}
		q="SELECT * FROM `courses` INNER JOIN `institutes` USING (`institute_id`) ORDER BY `institute_id`"
		data['view']=select(q)
		if not data['view']:
			flash("NO COURCES REGISTERED")
		return render_template("admin_View_courses.html",data=data)
	else:
		return redirect(url_for('public.login'))






@admin.route('/admin_View_job_vacancies',methods=['get','post'])
def admin_View_job_vacancies():
	if not session.get("lid") is None:
		data={}
		q="SELECT *,`vacancies`.`status` AS vstatus FROM `vacancies` INNER JOIN `career_guidance` USING (`career_guidance_id`) ORDER BY `vstatus`"
		data['view']=select(q)
		if not data['view']:
			flash("NO VACANCIES REGISTERED")
		return render_template("admin_View_job_vacancies.html",data=data)
	else:
		return redirect(url_for('public.login'))






@admin.route('/admin_View_job_applications',methods=['get','post'])
def admin_View_job_applications():
	if not session.get("lid") is None:
		data={}
		q="SELECT *,`job_applications`.`date_time` AS job_date_time FROM `job_applications` INNER  JOIN `students` USING (`student_id`) INNER JOIN `vacancies` USING (`vacancy_id`) ORDER BY `vacancy_id`"
		data['view']=select(q)
		if not data['view']:
			flash("NO APPLICATIONS REGISTERED")
		return render_template("admin_View_job_applications.html",data=data)
	else:
		return redirect(url_for('public.login'))






@admin.route('/admin_View_students',methods=['get','post'])
def admin_View_students():
	if not session.get("lid") is None:
		data={}
		q='SELECT * FROM `students` INNER JOIN `courses` USING (`course_id`) ORDER BY `student_id` DESC'
		data['view']=select(q)
		if not data['view']:
			flash("NO STUDENTS REGISTERED")
		return render_template("admin_View_students.html",data=data)
	else:
		return redirect(url_for('public.login'))






@admin.route('/admin_View_ratings',methods=['get','post'])
def admin_View_ratings():
	if not session.get("lid") is None:
		data={}
		q="SELECT * FROM `ratings` INNER JOIN `students` USING (`student_id`) INNER JOIN `career_guidance` USING (`career_guidance_id`) ORDER BY `rate_id` DESC"
		data['view']=select(q)
		if not data['view']:
			flash("NO STUDENTS RATED")
		return render_template("admin_View_ratings.html",data=data)
	else:
		return redirect(url_for('public.login'))



