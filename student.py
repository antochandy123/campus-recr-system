from flask  import *
from database import *
import uuid
import fitz

student=Blueprint('student',__name__)

def detectpersonality():
	from transformers import pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pandas as pd

# Load sample MBTI dataset
def load_mbti_dataset():
    # Replace with actual dataset source if available
    data = {
        "text": [
            "I love exploring new theories and ideas.",
            "I prefer detailed schedules and plans.",
            "Social events energize me and I enjoy talking to new people.",
            "I enjoy working on creative projects alone.",
        ],
        "type": ["INTP", "ISTJ", "ENFP", "ISFP"],  # Example labels
    }
    return pd.DataFrame(data)

# NLP model to preprocess user input
def preprocess_text(text, model_name="bert-base-uncased"):
    nlp_model = pipeline("feature-extraction", model=model_name)
    embeddings = nlp_model(text)
    return embeddings[0]

# Train personality prediction model
def train_model(data):
    vectorizer = TfidfVectorizer(max_features=1000)
    X = vectorizer.fit_transform(data["text"])
    model = LogisticRegression()
    model.fit(X, data["type"])
    return vectorizer, model

# Predict personality type
def predict_personality(text, vectorizer, model):
    text_vectorized = vectorizer.transform([text])
    personality_type = model.predict(text_vectorized)[0]
    return personality_type
def getpersonout(user_text):
    # Load data and train the model
    mbti_data = load_mbti_dataset()
    vectorizer, personality_model = train_model(mbti_data)


    # Predict personality type
    predicted_type = predict_personality(user_text, vectorizer, personality_model)
    print(f"Predicted Personality Type: {predicted_type}")
    return predicted_type 


@student.route('/student_home')
def student_home():
    return render_template('student_home.html')


# @student.route('/stu_view_job_opening',methods=['get','post'])
# def stu_view_job_opening():
# 	if not session.get("lid") is None:
# 		data={}
# 		q="SELECT *,`vacancies`.`status` AS vstatus FROM `vacancies` INNER JOIN `career_guidance` USING (`career_guidance_id`) ORDER BY `vstatus`"
# 		data['view']=select(q)
# 		if not data['view']:
			
# 			flash("NO VACANCIES REGISTERED")
# 		return render_template("stu_view_job_opening.html",data=data)
# 	else:
# 		return redirect(url_for('public.login'))
	

# @student.route('/stu_view_job_opening', methods=['get', 'post'])
# def stu_view_job_opening():
#     if session.get("lid") is None:
#         return redirect(url_for('public.login'))

#     data = {}
#     student_id = session.get("lid")  # Get student ID from session

#     # Fetch job vacancies
#     q = """
#         SELECT *, `vacancies`.`status` AS vstatus 
#         FROM `vacancies` 
#         INNER JOIN `career_guidance` USING (`career_guidance_id`) 
#         ORDER BY `vstatus`
#     """
#     data['view'] = select(q)

#     # Handle the apply action
#     if request.method == 'POST' and 'vacancy_id' in request.form:
#         vacancy_id = request.form['vacancy_id']

#         # Check if the job is still active
#         q_check_status = "SELECT status FROM vacancies WHERE vacancy_id = %s"
#         vacancy_status = select(q_check_status, (vacancy_id,))
#         if not vacancy_status or vacancy_status[0]['status'] != 'Active':
#             flash("The job is no longer active.")
#             return render_template("stu_view_job_opening.html", data=data)

#         # Check if the student has already applied for the job
#         q_check_application = """
#             SELECT * FROM job_application 
#             WHERE vacancy_id = %s AND student_id = %s
#         """
#         application_exists = select(q_check_application, (vacancy_id, student_id))
#         if application_exists:
#             flash("You have already applied for this job.")
#             return render_template("stu_view_job_opening.html", data=data)

#         # Insert into job_application table
#         q_insert = """
#             INSERT INTO job_application (student_id, vacancy_id, application_date)
#             VALUES (%s, %s, CURDATE())
#         """
#         insert(q_insert, (student_id, vacancy_id))
#         flash("Job application submitted successfully.")

#     return render_template("stu_view_job_opening.html", data=data)



@student.route('/stu_view_job_opening',methods=['get','post'])
def stu_view_job_opening():
	if not session.get("lid") is None:
		data={}
		q="SELECT * FROM `vacancies` inner join career_guidance using (career_guidance_id)"
		data['view']=select(q)
		if not data['view']:
			flash('NO DATA FOUND')

		return render_template("stu_view_job_opening.html",data=data)
	else:
		return redirect(url_for('public.login'))
	
@student.route('/stu_view_seminar',methods=['get','post'])
def stu_view_seminar():
	if not session.get("lid") is None:
		data={}
		q="SELECT * FROM `seminars`"
		data['view']=select(q)
		if not data['view']:
			flash('NO DATA FOUND')

		return render_template("stu_view_seminar.html",data=data)
	else:
		return redirect(url_for('public.login'))

@student.route('/stu_view_career_gui_team',methods=['get','post'])
def stu_view_career_gui_team():
	if not session.get("lid") is None:
		data={}
		q="SELECT * FROM `career_guidance`"
		data['view']=select(q)
		if not data['view']:
			flash('NO DATA FOUND')

		return render_template("stu_view_career_gui_team.html",data=data)
	else:
		return redirect(url_for('public.login'))


	
# @student.route('/stu_view_job_opening', methods=['POST','get'])
# def stu_view_job_opening():
#     # Extract the student_id from the session and vacancy_id from the request
#     student_id = session.get('student_id')  # Ensure student_id is stored in the session
#     vacancy_id = request.json.get('vacancy_id')  # Use JSON input for the vacancy_id

#     if not student_id:
#         return jsonify({'status': 'error', 'message': 'User not logged in.'})
    
#     # Check if the student has already applied for this job
#     q_check = "SELECT * FROM job_application WHERE vacancy_id = %s AND student_id = %s"
#     existing = select(q_check, (vacancy_id, student_id))
    
#     if existing:
#         return jsonify({'status': 'error', 'message': 'You have already applied for this job.'})
    
#     # Insert the job application into the database
#     q_insert = """
#         INSERT INTO job_application (student_id, vacancy_id, application_date)
#         VALUES (%s, %s, CURDATE())
#     """
#     insert(q_insert, (student_id, vacancy_id))
    
#     return jsonify({'status': 'success', 'message': 'Job application submitted successfully.'})


@student.route('/stu_chat_box',methods=['get','post'])
def stu_chat_box():
	if not session.get("lid") is None:
		data={}
		career_guidance_id=request.args['career_guidance_id']
		data['cid']=career_guidance_id
		sid=session['id']
		data['id']=sid
		q="SELECT * FROM `chats` WHERE ((`sender_id`='%s' AND `receiver_id`='%s') AND (`sender_type`='career_guidance' AND `receiver_type`='student')) OR ((`sender_id`='%s' AND `receiver_id`='%s') AND (`sender_type`='student' AND `receiver_type`='career_guidance'))"%(career_guidance_id,sid,sid,career_guidance_id)
		data['chat']=select(q)
		if 'submit' in request.form:
			message=request.form['message']
			q="INSERT INTO `chats` (`sender_id`,`sender_type`,`receiver_id`,`receiver_type`,`message`,`date_time`) VALUES ('%s','student','%s','career_guidance','%s',now())"%(sid,sid,message)
			insert(q)
			flash('DELIVERED')
			return redirect(url_for("student.stu_chat_box",id=data['sid']))
		return render_template("stu_chat_box.html",data=data)
	else:
		return redirect(url_for('public.login'))


@student.route('/stu_rating',methods=['get','post'])
def stu_rating():
    data={}
    career_guidance_id=request.args['career_guidance_id']
	
    f="select * from ratings inner join career_guidance using (career_guidance_id) where rate_id='%s'"%(career_guidance_id)
    data['pi']=select(f)
    
    if data['pi']:
        career_guidance_id=data['pi'][0]['career_guidance_id']
        y="select * from ratings inner join career_guidance using (career_guidance_id) where career_guidance_id='%s'"%(career_guidance_id)
        data['dd']=select(y)
  
    if 'submit' in request.form:
        career_guidance=request.form['team_name']
        rate=request.form['rate']
        review=request.form['review']
        p="insert into ratings values(null,'%s','%s','%s','%s',curdate())"%(session['id'],career_guidance,rate,review)
        insert(p)
        return redirect(url_for('student.stu_rating',career_guidance_id=career_guidance_id))
    return render_template('stu_rating.html',data=data)



@student.route('/stu_view_profile',methods=['get','post'])
def stu_view_profile():
	if not session.get("lid") is None:
		data={}
		q="SELECT * FROM `students` INNER JOIN `courses` USING (`course_id`) WHERE student_id='%s'"%(session['id'])
		print(q)
		data['view']=select(q)
		if not data['view']:
			flash("NO STUDENTS REGISTERED")
		return render_template("stu_view_profile.html",data=data)
	else:
		return redirect(url_for('public.login'))
	

# @student.route('/student_upload_resume',methods=['get','post'])
# def student_upload_resume():
# 	if not session.get("lid") is None:
# 		data={}
		
# 		q="SELECT * FROM `seminars`  ORDER BY `seminar_id` DESC"
# 		data['view']=select(q)
# 		return render_template("student_upload_resume.html",data=data)
# 	else:
# 		return redirect(url_for('public.login'))
	

# @student.route('/student_upload_resume',methods=['post','get'])
# def student_upload_resume():
#     data={}

#     if 'action' in request.args:
#         action=request.args['action']
#         vacancy_id=request.args['vacancy_id']
#     else:
#         action=None
        
#     if action=="update":
#         s="SELECT * FROM `librabrians` WHERE login_id='%s'"%(vacancy_id)
#         res=select(s)
        
#         data['up']=res


#     if 'update' in request.form:
#         fname=request.form['fname']
#         lname=request.form['lname']
#         gender=request.form['lname']
#         phone=request.form['phone']
#         email=request.form['email']
#         address=request.form['address']
    
#         q="update librabrians set fname='%s',lname='%s','gender='%s',phone='%s',email='%s',address='%s' where librarian_id='%s'"%(fname,lname,gender,phone,email,address)
#         update(q)
#         flash("Successfully Updated")
#         return redirect(url_for('student.student_upload_resume'))
    
#     if action=='delete':
#         n="delete from librabrians where login_id='%s'"%(id)
#         delete(n)
#         flash("Successfully Deleted ")
#         return redirect(url_for('student.student_upload_resume'))
    
#     if 'btn' in request.form:
#         fname=request.form['fname']
#         lname=request.form['lname']
#         gender=request.form['lname']
#         phone=request.form['phone']
#         email=request.form['email']
#         address=request.form['address']
#         uname=request.form['uname']
#         pwd=request.form['pwd']

#         q="insert into login (uname,pwd,user_type) values ('%s','%s','lib')"%(uname,pwd)
#         lid=insert(q)

#         q1="insert into librabrians values(null,'%s','%s','%s','%s','%s','%s','%s')"%(lid,fname,lname,gender,phone,email,address)
#         insert(q1)
#         flash("Succesfully Inserted")
#         return redirect(url_for('student.student_upload_resume'))
    
#     s="select * from librabrians"
#     res=select(s)
#     data['librarian']=res


#     return render_template('student_upload_resume.html',data=data)



@student.route('/student_upload_resume',methods=['post','get'])
def student_upload_resume():
    data={}

    vacancy_id=request.args['vacancy_id']
    
    if 'submit' in request.form:
        resume=request.files['resume']
        path="static/images/"+str(uuid.uuid4())+resume.filename
        resume.save(path)
		
        # Open the PDF file in read-binary mode
        with open(path, 'rb') as pdf_file:
            # Create a PyPDF2 PdfReader object
            pdf_reader = fitz.open(pdf_file)

            # Get the number of pages in the PDF file
            num_pages = pdf_reader.page_count

            # Iterate through all the pages and extract the text
            text = ''
            for page_num in range(num_pages):
                page = pdf_reader.load_page(page_num)
                page_text = page.get_text()
                text += page_text

        print(text)
        
        # Sample resume text
        resume_text = text.replace("'", "''")
        out=getpersonout(resume_text)



        q1="insert into resume values(null,'%s','%s','%s')"%(vacancy_id,path,out)
        insert(q1)
        flash("Succesfully Inserted")
        return redirect(url_for('student.student_upload_resume',vacancy_id=vacancy_id))
    
    s="select * from resume inner join vacancies using (vacancy_id)"
    res=select(s)
    data['resume']=res


    return render_template('student_upload_resume.html',data=data,vacancy_id=vacancy_id)