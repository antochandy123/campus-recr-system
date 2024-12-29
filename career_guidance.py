from flask import *
from database import *
career_guidance=Blueprint('career_guidance',__name__)

@career_guidance.route('/career_guidance_home',methods=['get','post'])
def career_guidance_home():
	if not session.get("lid") is None:

		return render_template("career_guidance_home.html")
	else:
		return redirect(url_for('public.login'))



@career_guidance.route('/career_guidance_Manage_seminars',methods=['get','post'])
def career_guidance_Manage_seminars():
	if not session.get("lid") is None:
		data={}
		id=session['id']
		q="SELECT * FROM `seminars` WHERE `career_guidance_id`='%s' ORDER BY `seminar_id` DESC"%(id)
		data['view']=select(q)

		if 'submit' in request.form:
			title=request.form['title']
			description=request.form['description']
			venue=request.form['venue']
			event=request.form['event']
			q="INSERT INTO `seminars`(`career_guidance_id`,`title`,`description`,`venue`,`event_date_time`,`date_time`,status) VALUES ('%s','%s','%s','%s','%s',NOW(),'planed')"%(id,title,description,venue,event)
			insert(q)
			flash('PLANED')
			return redirect(url_for("career_guidance.career_guidance_Manage_seminars"))
		if 'action' in request.args:
			action=request.args['action']
			id=request.args['id']

		else:
			action=None

		if action=='cancel':
			q="update `seminars` set status='cancelled' WHERE `seminar_id`='%s'"%(id)
			update(q)
			flash("SEMINAR CANCELLED")
			return redirect(url_for("career_guidance.career_guidance_Manage_seminars"))

		if action=='update':
			q="SELECT * FROM `seminars` WHERE `seminar_id`='%s'"%(id)
			data['updatez']=select(q)

		if 'updates' in request.form:
			title=request.form['title']
			description=request.form['description']
			venue=request.form['venue']
			event=request.form['event']
			q="UPDATE `seminars` SET `title`='%s',`description`='%s',`venue`='%s',`event_date_time`='%s' WHERE `seminar_id`='%s'"%(title,description,venue,event,id)
			update(q)
			flash('UPDATED')
			return redirect(url_for("career_guidance.career_guidance_Manage_seminars"))
		return render_template("career_guidance_Manage_seminars.html",data=data)
	else:
		return redirect(url_for('public.login'))



@career_guidance.route('/career_guidance_Manage_job_openings',methods=['get','post'])
def career_guidance_Manage_job_openings():
	if not session.get("lid") is None:
		data={}
		id=session['id']
		q="SELECT * FROM `vacancies` WHERE `career_guidance_id`='%s'  ORDER BY `vacancy_id` DESC"%(id)
		data['view']=select(q)
		if 'submit' in request.form:
			comapny=request.form['comapny']
			post=request.form['post']
			vacancy=request.form['vacancy']
			q="INSERT INTO `vacancies` (`career_guidance_id`,`company_name`,`post`,`vacancy_count`,`date_time`,`status`) VALUES ('%s','%s','%s','%s',NOW(),'active')"%(id,comapny,post,vacancy)
			insert(q)
			flash('REGISTERED')
			return redirect(url_for("career_guidance.career_guidance_Manage_job_openings"))
		if 'action' in request.args:
			action=request.args['action']
			id=request.args['id']
		else:
			action=None
		if action=='closed':
			q="UPDATE vacancies SET `status`='closed' WHERE `vacancy_id`='%s'"%(id)
			update(q)
			return redirect(url_for("career_guidance.career_guidance_Manage_job_openings"))

		if action=='active':
			q="UPDATE vacancies SET `status`='active' WHERE `vacancy_id`='%s'"%(id)
			update(q)
			return redirect(url_for("career_guidance.career_guidance_Manage_job_openings"))

		if action=='update':
			q="SELECT * FROM `vacancies` WHERE `vacancy_id`='%s'"%(id)
			data['updat']=select(q)
		if 'update' in request.form:
			comapny=request.form['comapny']
			post=request.form['post']
			vacancy=request.form['vacancy']
			q="UPDATE `vacancies` SET `company_name`='%s',`post`='%s',`vacancy_count`='%s' WHERE `vacancy_id`='%s'"%(comapny,post,vacancy,id)
			update(q)
			flash('UPDATED')
			return redirect(url_for("career_guidance.career_guidance_Manage_job_openings"))
		return render_template("career_guidance_Manage_job_openings.html",data=data)
	else:
		return redirect(url_for('public.login'))



@career_guidance.route('/career_guidance_View_job_applications',methods=['get','post'])
def career_guidance_View_job_applications():
	if not session.get("lid") is None:
		id=session['id']
		data={}
		q="SELECT *,`job_applications`.`date_time` AS job_date_time FROM `job_applications` INNER  JOIN `students` USING (`student_id`) INNER JOIN `vacancies` USING (`vacancy_id`) WHERE career_guidance_id='%s'  ORDER BY `vacancy_id` DESC"%(id)

		data['view']=select(q)
		if not data['view']:
			flash("NO APPLICATIONS REGISTERED")
		if 'action' in request.args:
			action=request.args['action']
			id=request.args['id']
		else:
			action=None

		if action=='student':
			q="SELECT * FROM `students` INNER JOIN `courses` USING (`course_id`) WHERE `student_id`='%s'"%(id)
			data['student']=select(q)
		return render_template("career_guidance_View_job_applications.html",data=data)
	else:
		return redirect(url_for('public.login'))



@career_guidance.route('/career_guidance_View_ratings',methods=['get','post'])
def career_guidance_View_ratings():
	if not session.get("lid") is None:
		data={}
		id=session['id']
		q="SELECT * FROM `ratings` INNER JOIN `students` USING (`student_id`) INNER JOIN `career_guidance` USING (`career_guidance_id`) WHERE career_guidance_id='%s'  ORDER BY `rate_id` DESC"%(id)
		data['view']=select(q)
		if not data['view']:
			flash("NO STUDENTS RATED")
		return render_template("career_guidance_View_ratings.html",data=data)
	else:
		return redirect(url_for('public.login'))



@career_guidance.route('/career_guidance_Chat_with_students',methods=['get','post'])
def career_guidance_Chat_with_students():
	if not session.get("lid") is None:
		data={}
		id=session['id']
		q="SELECT * FROM students WHERE student_id IN(SELECT DISTINCT(student_id) FROM `chats` INNER  JOIN `students` ON (`chats`.`sender_id`=`students`.`student_id`) WHERE `receiver_id`='%s' AND `receiver_type`='career_guidance'  ORDER BY `chat_id` DESC)"%(id)
		print(q)
		data['chat']=select(q)

		return render_template("career_guidance_Chat_with_students.html",data=data)
	else:
		return redirect(url_for('public.login'))


@career_guidance.route('/career_guidance_view_requests',methods=['get','post'])
def career_guidance_view_requests():
	if not session.get("lid") is None:
		data={}
		id=request.args['id']
		data['id']=id
		q="SELECT * FROM `seminar_request` INNER JOIN `students` USING (`student_id`) WHERE `seminar_id`='%s' ORDER BY `request_id` DESC"%(id)
		data['view']=select(q)
		if not data['view']:
			flash("NO REQUEST FOUNT")
		if 'action' in request.args:
			action=request.args['action']
			rid=request.args['rid']
		else:
			action=None

		if action=='accept':
			q="UPDATE `seminar_request` SET `status`='accepted' WHERE `request_id`='%s'"%(rid)
			update(q)
			flash("ACCEPTED")
			return redirect(url_for('career_guidance.career_guidance_view_requests',id=data['id']))
		if action=='reject':
			q="UPDATE `seminar_request` SET `status`='rejected' WHERE `request_id`='%s'"%(rid)
			update(q)
			flash("REJECTED")
			return redirect(url_for('career_guidance.career_guidance_view_requests',id=data['id']))
		return render_template("career_guidance_view_requests.html",data=data)
	else:
		return redirect(url_for('public.login'))

@career_guidance.route('/career_guidance_chat_box',methods=['get','post'])
def career_guidance_chat_box():
	if not session.get("lid") is None:
		data={}
		sid=request.args['id']
		data['sid']=sid
		ca_id=session['id']
		data['id']=ca_id
		q="SELECT * FROM `chats` WHERE ((`sender_id`='%s' AND `receiver_id`='%s') AND (`sender_type`='student' AND `receiver_type`='career_guidance')) OR ((`sender_id`='%s' AND `receiver_id`='%s') AND (`sender_type`='career_guidance' AND `receiver_type`='student'))"%(sid,ca_id,ca_id,sid)
		data['chat']=select(q)
		if 'submit' in request.form:
			message=request.form['message']
			q="INSERT INTO `chats` (`sender_id`,`sender_type`,`receiver_id`,`receiver_type`,`message`,`date_time`) VALUES ('%s','career_guidance','%s','student','%s',now())"%(ca_id,sid,message)
			insert(q)
			flash('DELIVERED')
			return redirect(url_for("career_guidance.career_guidance_chat_box",id=data['sid']))
		return render_template("career_guidance_chat_box.html",data=data)
	else:
		return redirect(url_for('public.login'))


