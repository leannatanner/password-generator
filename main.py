import secrets

password = []
shuffler = secrets.SystemRandom()

# Character pools
lower_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
upper_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
symbols = ["!","@","#","$","%","^","&","*"]

# Gets valid user inputs type int
def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")

password_length = get_int_input("How many characters (8-64): ")
lower_letter = get_int_input("How many lowercase letters: ")
upper_letter = get_int_input("How many uppercase letters: ")
symbol = get_int_input("How many symbols: ")

# Checks if password length input is between 8 and 64
if password_length < 8 or password_length > 64:
    while True:
        password_length = get_int_input("How many characters (8-64): ")
        if 8 <= password_length <= 64:
            break
        print("Invalid length.")

# Checks if sum of letters and symbols is less or equal to password length
if lower_letter + upper_letter + symbol > password_length:
    while True:
        print(f"Too many required characters. The sum of your letters and symbols must be equal to or less than {password_length}.\nPlease try again.")
        lower_letter = get_int_input("Lowercase letters: ")
        upper_letter = get_int_input("Uppercase letters: ")
        symbol = get_int_input("Symbols: ")
        if lower_letter + upper_letter + symbol <= password_length:
            break

# Adds characters based on inputs to the password list
for character in range(0,password_length):
    if lower_letter > 0:
        l_letter = secrets.choice(lower_letters)
        password.append(l_letter)
        lower_letter -= 1
    elif upper_letter > 0:
        u_letter = secrets.choice(upper_letters)
        password.append(u_letter)
        upper_letter -= 1
    elif symbol > 0:
        s_char = secrets.choice(symbols)
        password.append(s_char)
        symbol -= 1
    else:
        num = str(secrets.randbelow(10))
        password.append(num)

# Shuffles password list items
shuffler.shuffle(password)
# Creates the password string
password_result = "".join(password)
# Outputs password
print(password_result)