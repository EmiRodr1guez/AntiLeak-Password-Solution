import hashlib
import random
import string
from time import sleep
import requests
from colorama import Fore
from password_strength import PasswordStats
import stdiomask


# Function to check for leaked password
def checkLeak(password, api_key):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1password[:5]
    suffix = sha1password[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    hashes = (line.split(':') for line in response.text.splitlines())
    count = next((int(count) for t, count in hashes if t == suffix), 0)
    return count


# function that generates random digits to end of password
def randomdigitPass(length):
    characters = string.digits + string.punctuation
    result_str = ''.join(random.choice(characters) for i in range(length))
    return result_str

# Initial Sequence
print("Did you know that 20% of passwords are compromised?\n")
sleep(1)
print("Lets turn your password into the other 80%.\n")
sleep(1)
print("First, Lets check if your password is compromised.\n")
sleep(2)
userPass = stdiomask.getpass(prompt="Please enter your current password : ")

# API Key
api_key = 'a2fd0d73ba7a4ac8ad990c37a6f3ffcb' # < ******* Please enter your own API key. *******
count = checkLeak(userPass, api_key)

if count <= 0:
    print("Your password has not been compromised. Pat yourself on the back\n")
    sleep(1)
    print("That being said, true security matters. Hence why you should come back periodically to ensure your passwords are safe\n")
    sleep(1)
    print(Fore.CYAN + "Take care, and much ❣️. -Emiliano R.")


else:
    bluruserPassword = userPass[:-4] + "****"
    with open('LeakedPass.txt', 'w') as f:
        print(f"{bluruserPassword} has been compromised {count} times.", file=f)
    print(f"Your password has been compromised {count} times. You should change it ASAP.\n")
    sleep(2)
    print("Dont worry. We generated a couple passwords for you that are similar to your current password. Just so you "
    "wont forget.\n")
    sleep(2)
    print("These passwords are in ascending order or least complex to most complex\n")
    sleep(2)
    password1 = randomdigitPass(2)
    sleep(1)
    password2 = randomdigitPass(3)
    sleep(1)
    password3 = randomdigitPass(4)
    sleep(1)
    password4 = randomdigitPass(5)
    sleep(2)

    print("At the end of the password, the decimal is the strength of the password. anything above .66 is considered a "
    "STRONG password\n")
    sleep(1)
    print("I recommend always opting for a password that has a score above .66\n")
    sleep(1)
    stats = PasswordStats(userPass + password1)
    print(Fore.RED + f"Password 1: {userPass + password1} // Strength of this password is => {round(stats.strength(), 2)}")
    sleep(1)
    stats = PasswordStats(userPass + password2)
    print(Fore.BLUE + f"Password 2: {userPass + password2} // Strength of this password is => {round(stats.strength(), 2)}")
    sleep(1)
    stats = PasswordStats(userPass + password3)
    print(Fore.GREEN + f"Password 3: {userPass + password3} // Strength of this password is => {round(stats.strength(), 2)}")
    sleep(1)
    stats = PasswordStats(userPass + password4)
    print(Fore.CYAN + f"Password 4: {userPass + password4} // Strength of this password is => {round(stats.strength(), 2)}")
    saveToFile = bool(input("Would you like to save these passwords to a file? (y/n): "))

    while saveToFile:
        with open('UnleakedPass.txt', 'w') as f:
            sleep(1)
            print(Fore.RED + f"Password 1: {userPass + password1} // Strength of this password is => {round(stats.strength(), 2)}", file=f)
            print(Fore.BLUE + f"Password 2: {userPass + password2} // Strength of this password is => {round(stats.strength(), 2)}", file=f)
            print(Fore.GREEN + f"Password 3: {userPass + password3} // Strength of this password is => {round(stats.strength(), 2)}", file=f)
            print(Fore.CYAN + f"Password 4: {userPass + password4} // Strength of this password is => {round(stats.strength(), 2)}", file=f)
            sleep(2)
        print('Passwords have been printed to UnleakedPass.txt\n')
        break

    else:
        print('No worries. You can always restart the program if you wish to generate new passwords.\n')
        sleep(1)
        print("That being said, true security matters. Hence why you should come back periodically to ensure your passwords are safe\n")
        sleep(1)
        print(Fore.CYAN + "Take care, and much ❣️. -Emiliano R.")
