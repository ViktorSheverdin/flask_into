class User:
    def __init__(self, name):
        self.name = name
        self.logged_in = False


def is_authenticated_decorator(function):
    def wrapper_function(*args, **kwargs):
        if args[0].logged_in == True:
            return function(args[0])
    return wrapper_function


@is_authenticated_decorator
def create_blog_post(user):
    print(f"User {user.name} has created a blog post")


new_user = User("Viktor")
new_user.logged_in = True
create_blog_post(new_user)
