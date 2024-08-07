# generate_password_hashes.py
import hashlib
import random
import string

def generate_random_string(length=8):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

def hash_password(password, salt=''):
    return hashlib.sha256((salt + password).encode('utf-8')).hexdigest()

def generate_password_hash_pairs(num_pairs=10, salt=True):
    pairs = []
    for _ in range(num_pairs):
        password = generate_random_string()
        salt_value = generate_random_string() if salt else ''
        hash_value = hash_password(password, salt_value)
        pairs.append((password, salt_value, hash_value))
    return pairs

def save_to_file(filename, pairs):
    with open(filename, 'w') as f:
        for password, salt, hash_value in pairs:
            f.write(f'{password},{salt},{hash_value}\n')

# Generate 1000 password hash pairs with salts
pairs = generate_password_hash_pairs(1000, salt=True)
save_to_file('password_hash_pairs.txt', pairs)

print("Password hash pairs generated and saved to password_hash_pairs.txt")
