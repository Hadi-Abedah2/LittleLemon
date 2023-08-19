{
    "menu_items_endpoints": ['api/menu-items', 'api/menu-items/{menu-itemsId}'],
    "booking_endpoints": ['api/booking/tables', 'api/booking/tables/{tableId}'],
    "user_registration_endpoints": ['api/users', 'api/users/{Id}'],
    "djoser_endpoints_for_user_management": 'use djoser provided endpoints like: auth/users/me or /auth/token/login'
}


Note:
I used python venv module to make my virtual environment.
You need to make virtual environment using python -m venv <name_of_venv> (I used workspace for naming my venv)
run this command after activating your venv using: source /workspace/Scripts/activate 
pip3 install django 
pip3 install djangorestframework
pip3 install djoser
