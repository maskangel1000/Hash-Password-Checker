def check_hash(password_dict: dict, hash: str):
    for i in password_dict:
        if password_dict[i] == hash:
            return i
    return None