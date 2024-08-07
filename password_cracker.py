import hashlib

# Função para carregar a base de dados de senhas com salt
def load_password_database(filename='passwords.txt'):
    passwords_with_salt = {}

    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 3:
                password, salt, hash_value = parts
                passwords_with_salt[hash_value] = (password, salt)

    return passwords_with_salt

# Carregar a base de dados na memória
passwords_with_salt = load_password_database()

# Função para crackear hashes SHA-256 com salt
def crack_sha256_hash_with_salt(hash_value):
    for stored_hash, (password, salt) in passwords_with_salt.items():
        salted_password = salt + password
        if hashlib.sha256(salted_password.encode()).hexdigest() == hash_value:
            return password
    return 'PASSWORD NOT IN DATABASE'
