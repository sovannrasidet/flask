
# Activate virtual environment (cd to project directory)
#   > python -m venv .venv
#   > .\\.venv\\Scripts\\activate.bat       (CMD)
#   > .\\.venv\\Scripts\\Activate.ps1       (powershell)
#   > source .venv/Scripts/activate         (Git bash)
#   > source .venv/bin/activate             (Bash on Linux)

# Install all packages 
#   > pip install -r requirements.txt 

# Then run 'initdb' first: 
#   > python initdb.py

# Run 'readdb' to print out contents of the database: 
#   > python readdb.py


from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, IntegerField, TextAreaField
from wtforms.validators import InputRequired, Length, ValidationError, NumberRange
from flask_bcrypt import Bcrypt
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    dob = db.Column(db.Date, nullable=False)
    address = db.Column(db.String(200), nullable=False)

class RegisterForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField('Register')

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                'That username already exists. Please choose a different one.')

class LoginForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField('Login')

class StudentForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Length(min=2, max=100)], 
                      render_kw={"placeholder": "Enter student name"})
    age = IntegerField('Age', validators=[InputRequired(), NumberRange(min=1, max=120)], 
                      render_kw={"placeholder": "Enter age"})
    dob = DateField('Date of Birth', validators=[InputRequired()], 
                   render_kw={"type": "date"})
    address = TextAreaField('Address', validators=[InputRequired(), Length(min=5, max=200)], 
                          render_kw={"placeholder": "Enter full address", "rows": 3})
    submit = SubmitField('Add Student')


@app.route('/')
def home():
    
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('dashboard'))
    return render_template('login.html', form=form)

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/students', methods=['GET'])
@login_required
def students():
    student_list = Student.query.all()
    return render_template('student.html', students=student_list)

@app.route('/add_student', methods=['GET', 'POST'])
@login_required
def add_student():
    form = StudentForm()
    if form.validate_on_submit():
        new_student = Student(
            name=form.name.data,
            age=form.age.data,
            dob=form.dob.data,
            address=form.address.data
        )
        db.session.add(new_student)
        db.session.commit()
        return redirect(url_for('students'))
    return render_template('add_student.html', form=form)

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9999, debug= True)




# from flask import Flask, render_template, url_for

# app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')


# @app.route('/')
# def index():
#     name = 'Btk'
#     age = 20
#     score = [11, 45, 56, 67, 33]
#     return render_template('index.html', name = name, old = age, list = score)

# @app.route('/login')
# def login():
#     return render_template('login.html')

# @app.route('/calculator')
# def calculator_app():
#     return render_template('cal_app.html')



# if __name__ == '__main__':
#     app.run(host='127.0.0.1', port=9999, debug= True)
