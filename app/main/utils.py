

def populate_acct_form(form, acct):
    form.first_name.data = acct.first_name
    form.middle_name.data = acct.middle_name
    form.last_name.data = acct.last_name
    form.phys_address.data = acct.phys_address
    form.phys_city.data = acct.phys_city
    form.phys_state.data = acct.phys_state
    form.phys_zip.data = acct.phys_zip
    form.mail_address.data = acct.mail_address
    form.mail_city.data = acct.mail_city
    form.mail_state.data = acct.mail_state
    form.mail_zip.data = acct.mail_zip
    form.phone.data = acct.phone
    form.phone2.data = acct.phone2
    return form

def edit_account_model(form, acct):
    acct.first_name = form.first_name.data
    acct.middle_name = form.middle_name.data
    acct.last_name = form.last_name.data
    acct.phys_address = form.phys_address.data
    acct.phys_city = form.phys_city.data
    acct.phys_state = form.phys_state.data
    acct.phys_zip = form.phys_zip.data
    acct.mail_address = form.mail_address.data
    acct.mail_city = form.mail_city.data
    acct.mail_state = form.mail_state.data
    acct.mail_zip = form.mail_zip.data
    acct.phone = form.phone.data
    acct.phone2 = form.phone2.data
    return acct
