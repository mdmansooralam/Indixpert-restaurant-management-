



from src.controllers.user_controller.user_state import UserState
from src.models.user_model import UserModel
from src.dashboard.manage_dashboard import dashboard


def super_admin(email, password):
    id = 'sp01'
    role = 'super_admin'
    name = 'super admin'
    super_admin = UserModel(id, name, email, password, role).__dict__
    UserState().update_state(super_admin)
    dashboard()
