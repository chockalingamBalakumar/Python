SERVICE_CHARGE = 2;
TICKET_PRICE = 10

tickets_remaining = 100  


def calculate_price(num_of_tickets):
    return (num_of_tickets * TICKET_PRICE) + SERVICE_CHARGE

while tickets_remaining >= 1:
    print("There are {} tickets remaining".format(tickets_remaining))
    name = input("What is your name ")
    num_tickets = input("How many tickets would you like, {}? ".format(name))
    try:
        num_tickets = int(num_tickets)
        if tickets_remaining < num_tickets:
            raise ValueError("There are only {} tickets remaning".format(tickets_remaining))
    except ValueError as err:
        print("Oh no, we ran into an issue. {}. Please try again".format(err))
    else:
        amount_due = calculate_price(num_tickets)
        print("The total due is ${}".format(amount_due))
        proceed_flag = input("Whether would you like to proceed? Y/N " )
        proceed_flag = proceed_flag.lower()
        if proceed_flag == "y":
            #TODO: Gather credit card information and process it
            print("SOLD!")
            tickets_remaining -= num_tickets;
        else:
            print("Thank you anways {}".format(name))
print("Sorry All tickets are sold out!!! :(")
