



from src.controllers.user_controller.user_state import UserState
from src.dashboard.manage_dashboard import dashboard


def super_admin(email, password):
    id = 'sp01'
    role = 'super_admin'
    name = 'super admin'
    super_admin = {
        "role":role,
        "email":email,
        "password":password,
        "id":id,
        "name":name

    }
    UserState().update_state(super_admin)
    dashboard()
