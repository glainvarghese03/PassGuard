import hashlib
import re
import secrets
import string
import sys

# ANSI color codes for professional terminal output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def check_password_strength(password: str) -> tuple:
    """
    Evaluates the strength of a given password.
    Returns a tuple of (score, feedback_list).
    """
    score = 0
    feedback = []

    # 1. Length Check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
        feedback.append("Password should be at least 12 characters long for better security.")
    else:
        feedback.append("Password is too short. Use at least 8 characters.")

    # 2. Complexity Checks (Regex)
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")
        
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")
        
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add numbers.")
        
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters (e.g., !@#$%).")

    # Calculate final strength rating (Max score is 6)
    if score >= 6:
        strength = f"{Colors.GREEN}Very Strong{Colors.ENDC}"
    elif score >= 4:
        strength = f"{Colors.CYAN}Strong{Colors.ENDC}"
    elif score >= 3:
        strength = f"{Colors.WARNING}Moderate{Colors.ENDC}"
    else:
        strength = f"{Colors.FAIL}Weak{Colors.ENDC}"

    return strength, feedback

def generate_secure_hash(password: str, salt: str = None) -> tuple:
    """
    Generates a secure SHA-256 hash of the password using a salt.
    Salt prevents Rainbow Table attacks.
    """
    if salt is None:
        # Generate a random 16-byte salt
        salt = secrets.token_hex(16)
    
    # Combine password and salt, then encode to bytes
    salted_password = (password + salt).encode('utf-8')
    
    # Generate hash
    hash_object = hashlib.sha256(salted_password)
    hashed_password = hash_object.hexdigest()
    
    return hashed_password, salt

def generate_strong_password(length: int = 16) -> str:
    """
    Generates a cryptographically secure random password.
    """
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def main():
    print(f"{Colors.HEADER}{Colors.BOLD}========================================={Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}   Welcome to PassGuard Security Suite   {Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}========================================={Colors.ENDC}\n")

    while True:
        print("Please select an option:")
        print("1. Check Password Strength")
        print("2. Generate Secure Hash (SHA-256 + Salt)")
        print("3. Generate a Strong Random Password")
        print("4. Exit")
        
        choice = input(f"\n{Colors.BLUE}Enter choice (1-4): {Colors.ENDC}")

        if choice == '1':
            pwd = input("Enter password to test: ")
            strength, feedback = check_password_strength(pwd)
            print(f"\nStrength: {strength}")
            if feedback:
                print(f"{Colors.WARNING}Suggestions for improvement:{Colors.ENDC}")
                for tip in feedback:
                    print(f" - {tip}")
            print("\n")

        elif choice == '2':
            pwd = input("Enter password to hash: ")
            hashed, salt = generate_secure_hash(pwd)
            print(f"\n{Colors.GREEN}Hash Generated Successfully:{Colors.ENDC}")
            print(f"Salt: {salt}")
            print(f"SHA-256 Hash: {hashed}")
            print(f"{Colors.CYAN}Note: Store both the salt and the hash in your database.{Colors.ENDC}\n")

        elif choice == '3':
            try:
                length = int(input("Enter desired password length (default 16): ") or 16)
                if length < 8:
                    print(f"{Colors.FAIL}Length too short. Minimum is 8.{Colors.ENDC}\n")
                    continue
                new_pwd = generate_strong_password(length)
                print(f"\n{Colors.GREEN}Generated Password: {Colors.BOLD}{new_pwd}{Colors.ENDC}\n")
            except ValueError:
                print(f"{Colors.FAIL}Invalid input. Please enter a number.{Colors.ENDC}\n")

        elif choice == '4':
            print(f"{Colors.HEADER}Exiting PassGuard. Stay secure!{Colors.ENDC}")
            sys.exit(0)
        else:
            print(f"{Colors.FAIL}Invalid choice. Please select 1-4.{Colors.ENDC}\n")

if __name__ == "__main__":
    main()