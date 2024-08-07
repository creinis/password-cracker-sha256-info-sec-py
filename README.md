## Password Cracker using SHA-256

###### Technologies:
<p align="center">
<img src="https://img.icons8.com/color/75/000000/python.png" width="75" height="75" alt="Python" style="margin: 10px 15px 0 15px;" />
<img src="https://ioflood.com/blog/wp-content/uploads/2023/09/Data-stream-converting-to-hash-Python-hashlib-code-snippets-Python-logo.jpg" width="75" height="75" alt="Python" style="margin: 10px 15px 0 15px;" />
</p>

### Try it!

To run the Password Cracker application, follow the instructions in the Setup section below.

## Project Structure

- `password_cracker.py`: Contains the implementation of the SHA-256 password cracking functions.
- `main.py`: Entry point to run the password cracking examples and tests.
- `known-salts.txt`: Contains a list of known salts.
- `passwords.txt`: Contains a list of common passwords.
- `test_module.py`: Contains unit tests for validating the password cracker.

## Setup

### Prerequisites

- Python 3 installed

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/creinis/password-cracker-sha256-info-sec-py.git
   cd password-cracker-sha256
   ```

2. Run the password cracker script:
   ```bash
   python3 main.py
   ```

## Password Cracker

### Functionality

The Password Cracker application is designed to crack SHA-256 hashed passwords. It supports both salted and unsalted hashes. The function iterates through a list of common passwords, optionally combining them with known salts, and compares the generated hash with the target hash to find a match.

### Functions

#### crack_sha256_hash

This function attempts to crack a given SHA-256 hash by comparing it against precomputed hashes of a list of common passwords. It can optionally use a list of known salts to enhance the cracking process.

### Practical Use Case

The Password Cracker is useful for security professionals and researchers who need to test the strength of hashed passwords by attempting to reverse them using common password lists and known salts.

### Benefits

- **Effective Testing:** Allows for testing password strength and hashing mechanisms.
- **Educational Value:** Provides insight into how password cracking techniques work and the importance of using strong, unique passwords and salts.

## How to Use

1. Start by running the `main.py` script to see the password cracker in action.
2. Modify the hash inputs in `main.py` to test with different hashes.
3. Explore the `test_module.py` to understand and run the unit tests for validating the functionality.

### Additional Information

- **Dataset:** The application uses `passwords.txt` for common passwords and `known-salts.txt` for known salts.
- **Comprehensive Analysis:** The application combines password and salt combinations to ensure thorough testing against the hash.
