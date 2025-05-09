# Class imports
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

# Class initializations
data_manager = DataManager()
flight_search = FlightSearch()
flight_data = FlightData()
notification = NotificationManager()


def new_user():
    # New user
    print("Welcome to GabzWrld International Flight Deals program🫱🏾‍🫲🏿")
    answer = input("Are you a new user....Yes or No? ").lower()
    if answer == "no":
        start_program()
    else:
        print("Please note that this is the first version of the app and as such All flights will begin from the Lagos Airport in Nigeria 🆖")
        answer = input("Do you still wish to continue with the registration...Yes or No? ").lower()
        if answer == "yes":
            first_name = input("\nFirst Name: ").title()
            last_name = input("Last Name: ").title()
            email = input("Email: ").lower()
            confirm_email = input("Please confirm Email: ").lower()
            while email != confirm_email:
                confirm_email = input("Sorry, Your email is not co-responding❌\nPlease enter your email again: ").lower()
            print("Weldone🎊 You have successfully completed your registration✅, Enjoy our services🚀")
            data_manager.add_user(first_name, last_name, email)
            start_program()
        else:
            print("\nWe are deeply sorry as this program isn't suitable for you")
            print("Please check in as we may have brought out a better version in the future")
            print("Goodbye👋🏾, hopefully seeing you soon")



def start_program():
    # Getting the values in the google sheet
    print("Starting the program...")
    print("Please Dont interrupt the program execution till you see a 'Program Ended Message.'")
    print("Getting list of cities...")
    sheety_data = data_manager.getprices()

    for item in sheety_data:
        # Updating the city iataCode if empty
        if item["iataCode"] == "":
            item["iataCode"] = flight_search.get_iataCode(item["city"])
            new_data = {
                "id": item["id"],
                "iataCode": item["iataCode"]
            }
            print(f"\nUpdating the iataCode for {item['city']}...")
            data_manager.update_iataCode(new_data)

        # This gets the lowest flight data
        print(f"\nSearching for flights to {item['city']}...")
        flight = flight_data.search_flights(item["iataCode"])

        #This checks if the flight price is lower than the lowest price
        if flight["price"] < item["lowestPrice"]:
            new_data = {
                "id": item["id"],
                "lowestPrice": flight["price"]
            }

            #This updates the lowest price to the flight price
            print(f"Found a match for {item['city']}")
            print("Updating lowest price..")
            data_manager.update_lowestprice(new_data)

            # This sends a message once we get a low budget price
            print("Sending Emails to our Users..")
            notification.send_notification(flight)
        else:
            print(f"No match for {item['city']}, Lowest price currently at ₦{item['lowestPrice']}")


new_user()
print("\nComment down this post at ...... if you will like me to increase the lowest prices or add more cities")
print("Your feedback is much appreciated")
print("Program Ended✅")