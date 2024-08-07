from password_cracker import crack_sha256_hash_with_salt

# Exemplo de uso para hashes com salt
hash_to_crack_with_salt = '2c6a798af53b6fef328bdcba90835ab22d90da8d4027e0a14173d0b8b93ddc4f'
print('Password found is:', crack_sha256_hash_with_salt(hash_to_crack_with_salt))  # Deve retornar 'hNf8hQnl'

hash_to_crack_with_salt = 'cd610f5b6e6681e58ee643c737c8a1e6fe063f27dc589ab8c23695e20e660e51'
print('Password found is:', crack_sha256_hash_with_salt(hash_to_crack_with_salt))  # Deve retornar 'g91B1TAA'

hash_to_crack_with_salt = '958f49edca14e4675a8b747cbf9afaea8f34e09da511497d6a05c599b90c0b11'
print('Password found is:', crack_sha256_hash_with_salt(hash_to_crack_with_salt))  # Deve retornar 'm09gTmmV'

hash_to_crack_with_salt = '3541cf4f58d6a223223939bddc084cdc53c6cec1d74d4d43fe9f754f637868b0'
print('Password found is:', crack_sha256_hash_with_salt(hash_to_crack_with_salt))  # Deve retornar 'nN8bnKyN'

