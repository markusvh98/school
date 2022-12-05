# Create a script called MyPhonebook.py The script is required to do the following:

# Define a dictionary consisting of five business names and their associated phone numbers. The business name should be used as the key.
business_number = {"pizzeria":47382939,"McDonalds":13789032,"Burgerkind":98347321,"Egon":75392834,"Idun":558394853}
print(business_number)
# Request the name and number of another business from the user and add it to the dictionary.
name = input("the name of the business:")
phone_number = input("the phone number of the business:")
business_number[name] = phone_number


# Ask the user to type in the name of a business that is in the list. Display the result to the user.
user_input = input("enter a name of the business in list:")
if user_input in business_number.keys():
    print("It exists")
else:
    print("It doesnt exist")





# Display the entire dictionary (names and phone numbers).

# Display only the business names (no phone numbers).
