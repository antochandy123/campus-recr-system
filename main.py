from flask import Flask
from public import public
from admin import admin
from career_guidance import career_guidance
from college import college
from student import student

app=Flask(__name__)
app.secret_key="remainsecret"

app.register_blueprint(public)
app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(career_guidance,url_prefix='/career_guidance')
app.register_blueprint(college,url_prefix='/college')
app.register_blueprint(student,url_prefix='/student')

# app.run(debug=True,port=5015,host="192.168.43.94")
app.run(debug=True,port=5015,host="0.0.0.0")