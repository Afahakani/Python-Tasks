import random
import string


user_full_details = []
user_input = ""


def user_details_dict():
    user_details = dict()
    user_details['First Name'] = first_name
    user_details['Last Name'] = last_name
    user_details['Email'] = email
    return user_details


def password():
    initial_password = first_name[:2].lower() + last_name[-2:].lower()
    string_length = 5
    letters = string.ascii_lowercase
    random_character_list = [random.choice(letters) for i in range(string_length)]
    random_password = "".join(random_character_list)
    your_password = initial_password + random_password
    return your_password


while True:
    user_input = input("Are you a new user? (Yes or No): ").lower()
    if user_input == "yes":
        first_name = input("Enter your First Name: ")
        last_name = input("Enter your Last Name: ")
        email = input("Enter your Email Address: ")
        print("Your Password is: ", password())

        password_agreement = input("Do you accept this password? (Yes or No): ")
        if password_agreement.lower() == "yes":
            user_full_details.append(user_details_dict())
            continue
        else:
            self_password = input("Please enter your own Password: ")
            if len(self_password) >= 7:
                user_full_details.append(user_details_dict())
                print("Password Accepted!")
            else:
                self_password = input("Please enter 7 or more characters: ")
                user_full_details.append(user_details_dict())
            continue
    else:
        break


user_counter = 0
print("\nThe User Details Are:")
for user in user_full_details:
    user_counter += 1
    print(user_counter, ": ", user)
