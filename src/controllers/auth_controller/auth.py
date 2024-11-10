import uuid
from datetime import date

from src.database.collections.user import User
from src.models.user_model import UserModel
from src.utility.check_user import check_user
from src.controllers.user_controller.super_admin import super_admin
from src.controllers.user_controller.user_state import UserState
from src.dashboard.manage_dashboard import dashboard
from src.utility.log_error import LogError
from src.utility.error_message import ErrorMessage




def user_signup(name, email, password, date_of_birth, mobile_number, address, gender):
        try:
            err_msg = ErrorMessage()
            USER = User()
            user = check_user(email)
            if(user):
                print(err_msg.email_already_resister)     
            else:
                id = str(uuid.uuid4())[:10]
                role = 'staff'
                employment_type = 'full time'
                shift_preferences = 'day'
                benefits = ['health insurance', 'meals']
                date_of_joining = date.today().strftime("%d-%m-%Y")
                status = 'active'
                salary = 18000
                

                new_user = UserModel(
                     id,
                     name,
                     email,
                     password,
                     date_of_birth,
                     mobile_number,
                     address,
                     salary,
                     date_of_joining,
                     role,
                     employment_type,
                     shift_preferences,
                     status,
                     benefits,
                     gender
                     
                ).__dict__
                USER.users.append(new_user)
                USER.save_user()
                print(err_msg.signup_success)
        except Exception as error:
             LogError().err.exception(error)
             print(error)


def user_login(email, password):
        try:
            err_msg = ErrorMessage()
            USER = User()
            if(email == 'super@admin.com' and password == 'Super@123'):
                super_admin(email, password)
            else:
                user = check_user(email)
                if(not user):
                    print(err_msg.user_not_exist)
                else:
                    for user in USER.users:
                        if(user['email'] == email):
                            if(user['status'] == 'active'):
                                if(user['password'] == password):
                                    UserState().update_state(user)
                                    dashboard()
                                else:
                                    print(err_msg.wrong_credential)
                            else:
                                 print(err_msg.account_deactive)
        except Exception as error:
            LogError().err.exception(error)
            print(error)
             