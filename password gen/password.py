import random
import string

def generate_password(length, use_letters=True, use_digits=True, use_symbols=True):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not (use_letters or use_digits or use_symbols):
        raise ValueError("At least one option (letters, digits, symbols) must be True.")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Command-Line Password Generator!")
    
    try:
        length = int(input("Enter the length of the password: "))
        if length <= 0:
            raise ValueError("Password length must be greater than zero.")
        
        use_letters = input("Include letters (yes/no)? ").strip().lower() in ['yes', 'y']
        use_digits = input("Include digits (yes/no)? ").strip().lower() in ['yes', 'y']
        use_symbols = input("Include symbols (yes/no)? ").strip().lower() in ['yes', 'y']
        
        password = generate_password(length, use_letters, use_digits, use_symbols)
        
        print("\nGenerated Password:", password)
    
    except ValueError as e:
        print("Error:", e)
        print("Please enter valid inputs.")

if __name__ == "__main__":
    main()
