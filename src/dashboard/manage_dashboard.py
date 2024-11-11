


from src.controllers.user_controller.user_state import UserState
from src.dashboard.super_admin_dashboard import super_admin_dashboard
from src.dashboard.admin_dashboard import admin_dashboard
from src.dashboard.staff_dashboard import staff_dashboard
from src.utility.error_message import ErrorMessage
def dashboard():
    err_msg = ErrorMessage()
    user_state = UserState().get_state()

    if(user_state['role'] == 'super_admin'):
        super_admin_dashboard()
    elif(user_state['role'] == 'admin'):
        admin_dashboard()
    elif(user_state['role'] == 'staff'):
        staff_dashboard()
    else:
        print(err_msg.not_authorized)