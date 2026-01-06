user_logged_in = False

def requires_login(func):
    def wrapper():
        if not user_logged_in:
            raise PermissionError("Usuario no autenticado.")
        return func()
    return wrapper


@requires_login
def view_profile():
    print("Mostrando perfil del usuario")

try:
    view_profile()
except PermissionError as e:
    print(e)

user_logged_in = True
view_profile()