import hashlib

"""
password_list : list - A list of byte strings to be encrypted
encryption_type : str - The type of encryption (md5, sha1, sha224, sha256, sha384, sha512)
"""
def hash_passwords(password_list : list, encryption_type : str):
    hashed_password_dict = {}

    for password in password_list:

        match encryption_type:
            case "md5":
                hashed_password = hashlib.md5(password)
            case "sha1":
                hashed_password = hashlib.sha1(password)
            case "sha224":
                hashed_password = hashlib.sha224(password)
            case "sha256":
                hashed_password = hashlib.sha256(password)
            case "sha384":
                hashed_password = hashlib.sha384(password)
            case "sha512":
                hashed_password = hashlib.sha512(password)
            case _:
                raise ValueError("Invalid value for encryption_type parameter")

        hashed_password_dict[password] = hashed_password.hexdigest()

    return hashed_password_dict