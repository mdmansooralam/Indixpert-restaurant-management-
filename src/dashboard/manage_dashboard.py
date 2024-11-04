


from src.controllers.user_controller.user_state import UserState
from src.dashboard.super_admin_dashboard import super_admin_dashboard
from src.dashboard.admin_dashboard import admin_dashboard
from src.dashboard.staff_dashboard import staff_dashboard

def dashboard():
    user_state = UserState().get_state()

    if(user_state['role'] == 'super_admin'):
        super_admin_dashboard()
    elif(user_state['role'] == 'admin'):
        admin_dashboard()
    elif(user_state['role'] == 'staff'):
        staff_dashboard()
    else:
        print('You are not authorized')