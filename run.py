ENCRYPTION = "md5" # The type of encryption (md5, sha1, sha224, sha256, sha384, sha512)
HASH = "5d41402abc4b2a76b9719d911017c592" # The hash that will be checked
FILE = "passwords.txt" # The file name (must be in the same directory)
DELIMITER = " " # The character that splits the passwords in FILE

#

from hash_passwords import hash_passwords
from check_hash import check_hash

f = open(FILE, "rb")
file = f.read().split(bytes(DELIMITER, "utf-8"))

hashed_passwords = hash_passwords(file, ENCRYPTION)

print(check_hash(hashed_passwords, HASH))