""" I'm sorry.
"""


def walk_stack_for(var_name):
    import inspect
    frame = None
    try:
        for f in inspect.stack()[1:]:
            frame = f[0]
            code = frame.f_code

            if code.co_varnames[:1] == (var_name, ):
                return frame.f_locals[var_name]
            elif code.co_varnames[:2] == ("self", var_name,):
                return frame.f_locals[var_name]
            elif code.co_varnames and code.co_varnames[0] == var_name:
                return frame.f_locals[var_name]
    finally:
        del frame


def current_user():
    """ Returns the current authenticated user, or None
    """
    curr_request = current_request()
    if curr_request:
        return curr_request.user


def current_request():
    """ Returns the current request, or None
    """
    return walk_stack_for('request')
