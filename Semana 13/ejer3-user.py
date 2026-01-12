class User:
    def __init__(self, name, date_of_birth):
        self._name = name
        self._date_of_birth = date_of_birth
    
    @property
    def age(self):
        from datetime import datetime
        today = datetime.today()
        birth_date = datetime.strptime(self._date_of_birth, "%Y-%m-%d")
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age

def validate_age(func):
    def wrapper(user, *args, **kwargs):
        age = user.age
        if age < 18:
            raise ValueError(f"Error! User {user._name} is underage: {age} years old.")
        return func(user, *args, **kwargs)
    return wrapper
    
@validate_age
def access_restricted_area(user):
    print(f"Access granted to {user._name}, age {user.age}.")



try:
    my_user = User("Carlos", "2015-05-15")
    access_restricted_area(my_user)
except ValueError as e:
    print(e)

my_user2 = User("María", "2000-01-04")
access_restricted_area(my_user2)