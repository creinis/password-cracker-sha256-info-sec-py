import unittest
from password_cracker import crack_sha256_hash_with_salt

class TestPasswordCracker(unittest.TestCase):
    def test_crack_sha256_hash_with_salt(self):
        self.assertEqual(crack_sha256_hash_with_salt('2c6a798af53b6fef328bdcba90835ab22d90da8d4027e0a14173d0b8b93ddc4f'), 'hNf8hQnl')
        self.assertEqual(crack_sha256_hash_with_salt('cd610f5b6e6681e58ee643c737c8a1e6fe063f27dc589ab8c23695e20e660e51'), 'g91B1TAA')
        self.assertEqual(crack_sha256_hash_with_salt('958f49edca14e4675a8b747cbf9afaea8f34e09da511497d6a05c599b90c0b11'), 'm09gTmmV')
        self.assertEqual(crack_sha256_hash_with_salt('3541cf4f58d6a223223939bddc084cdc53c6cec1d74d4d43fe9f754f637868b0'), 'nN8bnKyN')

if __name__ == '__main__':
    unittest.main()
