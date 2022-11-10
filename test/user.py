user_dict = None

def register_user(
    first_name,
    last_name,
    birthdate,
    gender,
    email
):
    global user_dict
    
    user_dict = {
        'first_name': first_name,
        'last_name': last_name,
        'birthdate': birthdate,
        'gender':gender,
        'email':email
    }
    return 'User succesfully registered.'
    