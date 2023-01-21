import random

print("Hello! Let's generate a password")

### List of character
characters = "ZXCVBNM,./ASDFGHJKL;'QWERTYUIOPzxcvbnmasdfghjklqwertyuiop"

### Prompt the user
passwordLength = int(input("How long would you like your password to be?"))

### Generate a random password
newPassword = []
for x in range(passwordLength):
    ### Append a random character to the password string
    newPassword.append(random.choice(characters))
    
### Convert array to string
finalPassword = ''.join(map(str, newPassword))

print("\nYour generated password is: \n",finalPassword)
