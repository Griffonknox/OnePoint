"""
LOCATION FOR ORM MODELS AND SQL DB CONNECTION
"""
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login
from flask_login import UserMixin
from sqlalchemy import desc
import datetime



class Acct_memb(db.Model):
    __tablename__ = "memb_account"
    varClientKey = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(100))
    middle_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))

    phys_address = db.Column(db.String(50))
    phys_city = db.Column(db.String(50))
    phys_state = db.Column(db.String(50))
    phys_zip = db.Column(db.String(50))

    mail_address = db.Column(db.String(50))
    mail_city = db.Column(db.String(50))
    mail_state = db.Column(db.String(50))
    mail_zip = db.Column(db.String(50))

    phone = db.Column(db.String(20))
    phone2 = db.Column(db.String(20))
    detail = db.Column(db.String(1000)) # check out the length of production

    loans = db.relationship("Acct_loans", lazy="dynamic")
    alerts = db.relationship("Alert", lazy="dynamic")
    follow_ups = db.relationship("Follow_Up", lazy="dynamic")

    def get_follow_ups(self):
        return self.follow_ups.all()

    def get_last_follow(self):
        return self.follow_ups.order_by(desc(Follow_Up.key)).limit(5)

    def get_alerts(self):
        return self.alerts.all()

    def get_loans(self):
        return self.loans.all()



class Acct_loans(db.Model):
    __tablename__ = "acct_loans"
    key = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    varClientKey = db.Column(db.Integer(), db.ForeignKey("memb_account.varClientKey"))
    loan_numb = db.Column(db.String(25))
    acctnolnno = db.Column(db.Integer())
    balance = db.Column(db.String(20))

class Alert(db.Model):
    __tablename__ = "alert"
    key = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    varClientKey = db.Column(db.Integer(), db.ForeignKey("memb_account.varClientKey"))
    Alert_Cat = db.Column(db.String(20))
    varEnteredBy = db.Column(db.String(100))
    dateEntered = db.Column(db.DateTime, index=True, default=datetime.datetime.today())  # change to date type column
    Alert_Detail = db.Column(db.String(5000))


class Follow_Up(db.Model):
    __tablename__ = "follow_up"
    key = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    varClientKey = db.Column(db.Integer(), db.ForeignKey("memb_account.varClientKey"))
    varEnteredBy = db.Column(db.String(100))
    dateEntered = db.Column(db.DateTime, index=True, default=datetime.datetime.today())  # change to datetime column
    txtDetails = db.Column(db.String(5000))
    varLoanNo = db.Column(db.String(25))
    delq_days = db.Column(db.String(20))



@login.user_loader
def load_user(id):
    return User.query.get(int(id))



class User(db.Model, UserMixin):
    __tablename__ = "Usr"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30))
    password = db.Column(db.String(255))
    urole = db.Column(db.Integer)
    full_name = db.Column(db.String(150))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


