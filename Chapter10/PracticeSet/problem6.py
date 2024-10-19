from random import randint

class Train:
    def __init__(udoy, trainNo):
        udoy.trainNo = trainNo

    def book(udoy, fro, to):
        print(f"Ticket is booked in train no: {udoy.trainNo} from {fro} to {to}")

    def getStatus(udoy):
        print(f"Train no: {udoy.trainNo} is running on time")

    def getFare(udoy, fro, to):
        print(f"Ticket fare in train no: {udoy.trainNo} from {fro} to {to} is {randint(222, 5555)}") 

t = Train(436)

t.book("Sylhet", "Dhaka")
t.getStatus()
t.getFare("Sylhet", "Dhaka")