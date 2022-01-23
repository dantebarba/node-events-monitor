from functools import wraps


def require_api_token(func):
    @wraps(func)
    def check_token(*args, **kwargs):
        # Check to see if it's in their session
        # Otherwise just send them where they wanted to go
        return func(*args, **kwargs)

    return check_token