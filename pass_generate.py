import re
import secrets
import string

MIN_LENGTH = 8
OUTPUT_MIN_LENGTH = 200

ALL_CHARS = string.ascii_letters + string.digits + string.punctuation

PATTERNS = [
    r"[a-z]",
    r"[A-Z]",
    r"[0-9]",
    f"[{re.escape(string.punctuation)}]",
]


def get_user_input():
    while True:
        value = input(f"Enter your password (minimum {MIN_LENGTH} characters): ")
        if len(value) < MIN_LENGTH:
            print(f"Password is too short. Use at least {MIN_LENGTH} characters.\n")
            continue
        return value


def is_strong(password):
    return all(re.search(pattern, password) for pattern in PATTERNS)


def generate_password(length):
    while True:
        password = "".join(secrets.choice(ALL_CHARS) for _ in range(length))
        if is_strong(password):
            return password


def main():
    print("=" * 40)
    print("          PASSWORD GENERATOR")
    print("=" * 40)

    user_input = get_user_input()
    password = generate_password(max(len(user_input), OUTPUT_MIN_LENGTH))

    print("\nYour generated password is:")
    print(password)


if __name__ == "__main__":
    main()