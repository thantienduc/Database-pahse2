from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

class insertForm(FlaskForm):
    InstructorId = IntegerField('InstructorId', validators=[DataRequired()])
    FName = StringField('First Name', validators=[DataRequired(), Length(min=1, max=20)])
    LName = StringField('Last Name', validators=[DataRequired(), Length(min=1, max=20)])
    StartDate = StringField('Start Date')
    Degree = StringField('Degree', validators=[DataRequired()])
    Rank = StringField('Rank', validators=[DataRequired(), Length(max = 20)])
    Type = StringField('Type', validators=[DataRequired(), Length(max = 10)])
    CId = IntegerField('CourseId', validators=[DataRequired()])
    SId = IntegerField('StudentId', validators=[DataRequired()])
    submit = SubmitField('Insert')

class updateForm(FlaskForm):
    StudentId = IntegerField('InstructorId', validators=[DataRequired()])
    FName = StringField('First Name', validators=[DataRequired(), Length(min=1, max=20)])
    LName = StringField('Last Name', validators=[DataRequired(), Length(min=1, max=20)])
    submit = SubmitField('Update')

class displayForm(FlaskForm):
    StudentId = IntegerField('StudentId', validators=[DataRequired()])
    submit = SubmitField('Display')
