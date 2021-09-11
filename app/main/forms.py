from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, TextAreaField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Optional
from wtforms.widgets import html5 as h5widgets
from app.models import Acct_memb


class AcctSearchForm(FlaskForm):
    acct_numb = IntegerField('Account Number', widget=h5widgets.NumberInput(min=0, max=100000, step=.01))
    submit = SubmitField('Search Account')

    def validate_acct_numb(self, acct_numb):
        acct = Acct_memb.query.get(int(acct_numb.data))
        if acct is None:
            raise ValidationError("Account Not Found")

class AccountForm(FlaskForm):
    acct_numb = IntegerField("Account Number", validators=[DataRequired()], widget=h5widgets.NumberInput(min=0, max=100000, step=.01))
    first_name = StringField("First Name", validators=[DataRequired()], render_kw={"maxlength": "100"})
    middle_name = StringField("Middle Name", validators=[Optional()], render_kw={"maxlength": "100"})
    last_name = StringField("Last Name", validators=[DataRequired()], render_kw={"maxlength": "100"})
    phys_address = StringField("Physical Address", validators=[DataRequired()], render_kw={"maxlength": "50"})
    phys_city = StringField("Physical City", validators=[DataRequired()], render_kw={"maxlength": "50"})
    phys_state = StringField("Physical State", validators=[DataRequired()], render_kw={"maxlength": "50"})
    phys_zip = StringField("Physical Zip", validators=[DataRequired()], render_kw={"maxlength": "50"})
    mail_address = StringField("Mail Address", validators=[Optional()], render_kw={"maxlength": "50"})
    mail_city = StringField("Mail City", validators=[Optional()], render_kw={"maxlength": "50"})
    mail_state = StringField("Mail State", validators=[Optional()], render_kw={"maxlength": "50"})
    mail_zip = StringField("Mail Zip", validators=[Optional()], render_kw={"maxlength": "50"})
    phone = StringField("Phone", validators=[DataRequired()], render_kw={"maxlength": "20"})
    phone2 = StringField("Phone 2", validators=[Optional()], render_kw={"maxlength": "20"})
    submit = SubmitField("Create Account")

    def validate_acct_numb(self, acct_numb):
        acct = Acct_memb.query.get(int(acct_numb.data))
        if acct is not None:
            raise ValidationError("Account Number Already In Use.")

class AccountDetailForm(FlaskForm):
    detail = TextAreaField("Detail", render_kw={"maxlength": "1000"})
    submit = SubmitField("Submit Account Detail")


class AccountFollowUpForm(FlaskForm):
    # loan_numb = StringField("Loan Number", validators=[Optional()], render_kw={"maxlength": "25"})
    loan_numb = SelectField("Loan Number")
    delq_days = StringField("Delinquent Days", validators=[Optional()], render_kw={"maxlength": "20"})
    detail = TextAreaField("Detail", validators=[DataRequired()], render_kw={"maxlength": "5000"})
    submit = SubmitField("Create Follow Up")



class AccountAlertForm(FlaskForm):
    category = SelectField("Alert Category", choices=[("Bankruptcy","Bankruptcy"), ("Total Loss","Total Loss"), ("Repossession", "Repossession"),("Charged Off Loan", "Charged Off Loan")])
    detail = TextAreaField("Detail", validators=[DataRequired()], render_kw={"maxlength": "5000"})
    submit = SubmitField("Create Alert")

class AccountEditForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()], render_kw={"maxlength": "100"})
    middle_name = StringField("Middle Name", validators=[Optional()], render_kw={"maxlength": "100"})
    last_name = StringField("Last Name", validators=[DataRequired()], render_kw={"maxlength": "100"})
    phys_address = StringField("Physical Address", validators=[DataRequired()], render_kw={"maxlength": "50"})
    phys_city = StringField("Physical City", validators=[DataRequired()], render_kw={"maxlength": "50"})
    phys_state = StringField("Physical State", validators=[DataRequired()], render_kw={"maxlength": "50"})
    phys_zip = StringField("Physical Zip", validators=[DataRequired()], render_kw={"maxlength": "50"})
    mail_address = StringField("Mail Address", validators=[Optional()], render_kw={"maxlength": "50"})
    mail_city = StringField("Mail City", validators=[Optional()], render_kw={"maxlength": "50"})
    mail_state = StringField("Mail State", validators=[Optional()], render_kw={"maxlength": "50"})
    mail_zip = StringField("Mail Zip", validators=[Optional()], render_kw={"maxlength": "50"})
    phone = StringField("Phone", validators=[DataRequired()], render_kw={"maxlength": "20"})
    phone2 = StringField("Phone 2", validators=[Optional()], render_kw={"maxlength": "20"})
    submit = SubmitField("Edit Account")
