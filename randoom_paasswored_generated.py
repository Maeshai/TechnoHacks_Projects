import random
import string

def generate_password(length):
        if length < 6:  # Setting a minimum length for security
                    return "Password length should be at least 6 characters"

                    # Combine all letters (uppercase and lowercase), digits, and punctuation
                        characters = string.ascii_letters + string.digits + string.punctuation

                            # Randomly choose characters from the combined string
                                password = ''.join(random.choice(characters) for i in range(length))

                                    return password

                                # Example Usage
                                password_length = int(input("Enter the length of the password: "))
                                password = generate_password(password_length)
                                print("Generated Password:", password)

