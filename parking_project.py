class Parking():
    def __init__(self):
        self.tickets = [60]
        self.parkingSpaces = [60]
        self.currentTicket = {}
        self.license_num = ""

    #Saad did this method
    def takeTicket(self):
        if self.tickets[0] > 0 and self.parkingSpaces[0] > 0:
            take_a_ticket = input("Would you like to take a ticket? Promise we won't over charge \U0001F601. Write 'y' for yes and 'n' for no ").lower()
            self.license_num = input("What is your car's license number so we can verify it is your car at the end when you are ready to leave? ")
            if take_a_ticket == 'y':
                self.tickets = [x - 1 for x in self.tickets]
                self.parkingSpaces = [i - 1 for i in self.parkingSpaces]
                return "\nThank you for trusting our services, we will not dissapoint you.\nStay as long as you want and once you are ready to leave head to option '3' "
            else:
                return "Come back whenever you want!"
        else:
            return "There is no parking availability. Try your luck later."
    
    #Saad did this method
    def checkForSpace(self):
        return f"The total number of tickets available are {self.tickets} and the number of parking spaces left are {self.parkingSpaces}"

    #Saad did this method
    def payForParking(self):
        pay = float(input("In order to purchase a ticket the total amount you have to pay is $15.50. "))
        if pay == 15.50:
                self.currentTicket['paid'] = True
                return "Thank you for paying your bill. Please move on to the '4' step. "
        if pay > 15.50:
            total = pay - 15.50
            print(f"You paid more than you had to and I am assuming that isn't a tip \U0001F612, so here is your change: ${total}")
            self.currentTicket['paid'] = True
            return "Your ticket has been paid and you have 15 mins to leave."
        elif pay < 15.50:
            total_1 = 15.50 - pay
            self.currentTicket['paid'] = False 
            return f"You still owe us ${total_1}, please pay the remaining or we are keepig your car forever! \N{angry face}"
        else:
            return "You still owe us $15.50 and you cannot leave without paying it"
            
    #Saad did this method
    def leaveGarage(self):
        verification = input("For verification reason's please enter your licence number ")
        for value_ in self.currentTicket.values():
            if value_ == True:
                if self.license_num == verification:
                    return "Thank you for using our services and have a nice day! Also, please complete a quick survey. "
                else:
                    return "Either you entered the wrong license number or you are a THIEF."
        if self.currentTicket == {}:
            payment = float(input("It is very unfortunate but our services aren't free, so pay your bill.\nYour total is $15.50 "))
            if payment == 15.50:
                return "Thank you for using our services. Please come back again. Also if you don't mind, would you like to fill out a quick survey. "
            elif payment > 15.50:
                total = payment - 15.50
                print(f"You paid more than you had to and I am assuming that isn't a tip \U0001F612, so here is your change: ${total}")
                self.tickets = [x + 1 for x in self.tickets]
                self.parkingSpaces = [i + 1 for i in self.parkingSpaces]
                return "Thank you for FINALLY paying your bill. Please come use our services again! Can you also complete a quick surey. "
            elif payment < 15.50:
                total_1 = 15.50 - payment
                self.currentTicket['paid'] = False 
                return f"You still owe us ${total_1}, please pay the remaining or we are keepig your car forever! \N{angry face}"
   
    #Chris did this method
    def surveyTip(self):
        survey = input("Would you like to take our survey?(y or n)")
        if survey == "y":
            A = str(input("How did you feel about our services? "))
            print(f'Thank you for leaving a responce. We apperciate you as a cutomer. ')
            tip = input("Would you like to leave us a tip? Write 'y' for yes and 'n' for no")
            if tip == 'y':
                E = input('how much would you like to tip? ')
                return f'Thank you for your tip of ${E}'
            else:
                return "Thank you for taking our survey."
        else:
            return "Thank u for your buisness."

saad_parking = Parking()

#Chris did this method
def run():
        
    while True:
        choice = input("""
            Welcome to our garage, would you like to park your car?
            Here are your options:
            [1] Check for parking availability
            [2] Get a ticket
            [3] Pay for parking
            [4] Leave garage
            [5] Take a survey
            [6] Quit
            """)
        if choice == "1":
            print(saad_parking.checkForSpace())
        if choice == "2":
            print(saad_parking.takeTicket())
        elif choice == "3":
            print(saad_parking.payForParking())
        elif choice =="4":
            print(saad_parking.leaveGarage())
        elif choice == "5":
            print(saad_parking.surveyTip())
        elif choice == "6":
            print("Thank you for trusting us with your car. Come back whenever! ")
            break


run()