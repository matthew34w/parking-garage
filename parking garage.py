class ParkingGarage:
    def __init__(self, total_tickets, total_parking_spaces):
        self.tickets = list(range(1, total_tickets + 1))
        self.parkingSpaces = list(range(1, total_parking_spaces + 1))
        self.currentTicket = {}

    def takeTicket(self):
        if not self.tickets or not self.parkingSpaces:
            print("Sorry, the parking garage is full.")
            return

        ticket = self.tickets.pop(0)
        parking_space = self.parkingSpaces.pop(0)
        self.currentTicket = {"ticket_number": ticket, "parking_space": parking_space, "paid": False}
        print(f"Ticket {ticket} issued. Parking space {parking_space} is reserved.")

    def payForParking(self):
        if not self.currentTicket:
            print("No ticket taken. Please take a ticket first.")
            return

        amount = input("Enter the payment amount: ")
        if amount:
            print("Payment successful. You have 15 minutes to leave.")
            self.currentTicket["paid"] = True
        else:
            print("Payment failed. Please try again.")

    def leaveGarage(self):
        if not self.currentTicket:
            print("No ticket taken. Please take a ticket first.")
            return

        if self.currentTicket["paid"]:
            print("Thank you, have a nice day!")
        else:
            payment = input("Payment pending. Please enter the payment amount: ")
            if payment:
                print("Payment successful. Thank you, have a nice day!")
                self.currentTicket["paid"] = True
            else:
                print("Payment failed. Please try again.")

        
        self.parkingSpaces.append(self.currentTicket["parking_space"])
        self.tickets.append(self.currentTicket["ticket_number"])
        self.currentTicket = {}



parking_garage = ParkingGarage(total_tickets=10, total_parking_spaces=10)


parking_garage.takeTicket()

parking_garage.payForParking()


parking_garage.leaveGarage()