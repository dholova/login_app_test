import time


def test_user_login(press_login_button, mail, password):
    app = press_login_button
    mail, is_correct_mail = mail
    password, is_correct_password = password
    is_correct_data = is_correct_mail and is_correct_password
    # app.login_page()
    # time.sleep(7)
    app.enter_email(mail)
    time.sleep(1)

    app.enter_password(password)
    time.sleep(1)

    app.login_try(is_correct_data)

