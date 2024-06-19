import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."

    
    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    # Generate the remaining characters randomly
    password += random.choices(characters, k=length - 4)
    
    # Shuffle the password list to ensure randomness
    random.shuffle(password)
    
    # Convert the list to a string and return
    return ''.join(password)

def main():
    print("Password Generator")
    
    while True:
        try:
            length = int(input("Enter the desired password length: "))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
            continue
        
        password = generate_password(length)
        print(f"Generated Password: {password}")
        
        another = input("Do you want to generate another password? (yes/no): ")
        if another.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
