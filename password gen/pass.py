import random
import string

def generate_password(length, use_lowercase=True, use_uppercase=True, use_digits=True, use_symbols=True):
    characters = ''
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not (use_lowercase or use_uppercase or use_digits or use_symbols):
        raise ValueError("At least one option (lowercase, uppercase, digits, symbols) must be True.")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Command-Line Password Generator!")
    
    try:
        length = int(input("Enter the length of the password: "))
        if length <= 0:
            raise ValueError("Password length must be greater than zero.")
        
        use_lowercase = input("Include lowercase letters (yes/no)? ").strip().lower() in ['yes', 'y']
        use_uppercase = input("Include uppercase letters (yes/no)? ").strip().lower() in ['yes', 'y']
        use_digits = input("Include digits (yes/no)? ").strip().lower() in ['yes', 'y']
        use_symbols = input("Include symbols (yes/no)? ").strip().lower() in ['yes', 'y']
        
        password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_symbols)
        
        print("\nGenerated Password:", password)
    
    except ValueError as e:
        print("Error:", e)
        print("Please enter valid inputs.")

if __name__ == "__main__":
    main() 
""" this can be one type of code for this particular project """
