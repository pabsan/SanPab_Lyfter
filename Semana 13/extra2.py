user_logged_in = False

def requires_login(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not arg:
                raise PermissionError("Usuario no autenticado.")
        for key, value in kwargs.items():
            if not value:
                raise PermissionError("Usuario no autenticado.")
        return func(*args, **kwargs)
    return wrapper


@requires_login
def view_profile(user):
    print("Mostrando perfil del usuario")

try:
    view_profile(user_logged_in)
except PermissionError as e:
    print(e)

user_logged_in = True
view_profile(user_logged_in)