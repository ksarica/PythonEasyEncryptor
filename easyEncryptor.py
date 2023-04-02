# Creating an alphabet consisting of letters, numbers and special characters
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_±=?"

# Finding the length of the alphabet
length = len(alphabet)

# Assigning a different shift value for each letter
shifts = [3, 5, 7, 9, 11, 13]

def encrypt(text):
    encrypted_text = ""
    # For each letter in the text
    for i in range(len(text)):
        # Finding the letter in the alphabet
        index = alphabet.find(text[i])
        # If the letter is not in the alphabet, we leave it as it is
        if index == -1:
            encrypted_text += text[i]
        else:
            # Choosing the shift value
            shift = shifts[i % len(shifts)]
            # Moving the letter forward by the shift value
            new_index = (index + shift) % length
            # Adding the new letter
            encrypted_text += alphabet[new_index]
    return encrypted_text

def decrypt(text):
    decrypted_text = ""
    # For each letter in the text
    for i in range(len(text)):
        # Finding the letter in the alphabet
        index = alphabet.find(text[i])
        # If the letter is not in the alphabet, we leave it as it is
        if index == -1:
            decrypted_text += text[i]
        else:
            # Choosing the shift value
            shift = shifts[i % len(shifts)]
            # Moving the letter backward by the shift value
            new_index = (index - shift) % length
            # Adding the new letter
            decrypted_text += alphabet[new_index]
    return decrypted_text

mode = input("Enter 'e' to encrypt or 'd' to decrypt: ")

if mode == "e":
    input_file_name = input("Enter the name of the text file you want to encrypt: ")
    
    try:
        with open(input_file_name + ".txt", "r", encoding="utf-8") as f:
            text = f.read()
        
        encrypted_text = encrypt(text)

        output_file_name = input("Enter a name for saving your encrypted text file: ")
        
        with open(output_file_name + ".txt", "w", encoding="utf-8") as f:
            f.write(encrypted_text)
    
    except FileNotFoundError:
        print("The file you entered does not exist. Please check your spelling and try again.")

elif mode == "d":
    input_file_name = input("Enter a name for saving your decrypted text file: ")
    
    try:
        with open(input_file_name + ".txt", "r", encoding="utf-8") as f:
            encrypted_text = f.read()
        
        decrypted_text = decrypt(encrypted_text)
        
        output_file_name = input("Enter a name for saving your decrypted text file: ")
        
        with open(output_file_name + ".txt", "w", encoding="utf-8") as f:
                f.write(decrypted_text)
    
    except FileNotFoundError:
         print("The file you entered does not exist. Please check your spelling and try again.")