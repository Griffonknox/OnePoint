from app.main import bp
from flask import render_template, request, flash, url_for, redirect
from flask_login import current_user, login_required
from app.main.forms import AcctSearchForm, AccountForm, AccountDetailForm, AccountFollowUpForm, AccountAlertForm, AccountEditForm
from app import db
from app.models import Acct_memb, Follow_Up, Alert
from datetime import datetime
from app.main.utils import populate_acct_form, edit_account_model

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    return render_template("home.html")


@bp.route("/search_account", methods=["GET", "POST"])
@login_required
def search_account():
    form = AcctSearchForm()
    if form.validate_on_submit():
        return redirect(url_for("main.display_account", id=int(form.acct_numb.data)))
    return render_template("search_account.html", form=form)

@bp.route("/display_account/<id>", methods=["GET", "POST"])
@login_required
def display_account(id):
    form = AcctSearchForm()
    acct = Acct_memb.query.get(int(id))
    detail_form = AccountDetailForm()
    if detail_form.validate_on_submit():
        print(detail_form.detail.data)
        acct.detail = detail_form.detail.data
        db.session.commit()
        flash("Detail Added to Account.")
        return redirect(url_for("main.display_account", id=int(id)))

    detail_form.detail.data = acct.detail
    return render_template("display_account.html", acct=acct, form=form, detail_form=detail_form)


@bp.route("/create_account", methods=["GET", "POST"])
@login_required
def create_account():
    form = AccountForm()
    if form.validate_on_submit():
        acct = Acct_memb(varClientKey=form.acct_numb.data, first_name=form.first_name.data, middle_name=form.middle_name.data,
                         last_name=form.last_name.data, phys_address=form.phys_address.data, phys_state=form.phys_state.data,
                         phys_city=form.phys_city.data, phys_zip=form.phys_zip.data,
                         mail_address=form.mail_address.data, mail_city=form.mail_city.data, mail_state=form.mail_state.data,
                         mail_zip=form.mail_zip.data, phone=form.phone.data, phone2=form.phone2.data, detail="")
        db.session.add(acct)
        db.session.commit()
        flash("Account Created.")
        return redirect(url_for("main.display_account", id=int(form.acct_numb.data)))
    return render_template("create_account.html", form=form)


@bp.route("/edit_account/<id>", methods=["GET", "POST"])
@login_required
def edit_account(id):
    acct = Acct_memb.query.get(int(id))
    form = AccountEditForm()
    if form.validate_on_submit():
        acct = edit_account_model(form, acct)
        db.session.commit()
        return redirect(url_for("main.display_account", id=int(id)))
    form = populate_acct_form(form, acct)
    return render_template("edit_account.html", form=form)


"""ACCOUNT NAVIGATION"""

@bp.route("/follow_ups/<id>", methods=["GET", "POST"])
@login_required
def follow_ups(id):
    acct = Acct_memb.query.get(int(id))
    form = AcctSearchForm()
    follow_form = AccountFollowUpForm()
    if follow_form.validate_on_submit():
        follow = Follow_Up(varClientKey=int(id), txtDetails=follow_form.detail.data, varLoanNo=follow_form.loan_numb.data,
                           delq_days=follow_form.delq_days.data, varEnteredBy=current_user.username, dateEntered=datetime.today().strftime("%m/%d/%Y"))
        db.session.add(follow)
        db.session.commit()
        flash("Follow Up Successfully Created.")
        return redirect(url_for("main.follow_ups", id=int(id)))
    return render_template("follow_ups.html", acct=acct, form=form, follow_form=follow_form)

@bp.route("/follow_view/<id>", methods=["GET", "POST"])
@login_required
def follow_view(id):
    follow_up = Follow_Up.query.get(int(id))
    return render_template("follow_view.html", follow=follow_up)

@bp.route("/alerts/<id>", methods=["GET", "POST"])
@login_required
def alerts(id):
    acct = Acct_memb.query.get(int(id))
    form = AcctSearchForm()
    alert_form = AccountAlertForm()
    if alert_form.validate_on_submit():
        alert = Alert(varClientKey=int(id), varEnteredBy=current_user.username, Alert_Detail=alert_form.detail.data,
                      Alert_Cat=alert_form.category.data, dateEntered=datetime.today().strftime("%m/%d/%Y"))
        db.session.add(alert)
        db.session.commit()
        flash("Alert Successfully Created.")
        return redirect(url_for("main.alerts", id=int(id)))
    return render_template("alerts.html", acct=acct, form=form, alert_form=alert_form)

@bp.route("/loans/<id>", methods=["GET", "POST"])
@login_required
def loans(id):
    form = AcctSearchForm()
    acct = Acct_memb.query.get(int(id))
    return render_template("loans.html", acct=acct, form=form)
