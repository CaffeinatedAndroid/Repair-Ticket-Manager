import os

statusList = ["Pending","Finished","NotStarted"]

class Ticket:
    def __init__(self, customerName, dropOffDate, pickUpDate, device, repairs, repairTime, status):
        self.customerName = customerName
        self.dropOffDate = dropOffDate
        self.pickUpDate = pickUpDate
        self.device = device
        self.repairs = repairs
        self.repairTime = repairTime
        self.status = status

class Repairs:###################MUST DO!!!
    def __init__():
        return


def AddNew():
    customerName = str(input("Name? "))
    dropOffDate = int(input("Drop off date? ")) #format date
    pickUpDate = int(input("Pick up date? ")) #format date
    device = str(input("Device? "))
    repairs = str(input("Repairs? "))
    repairTime = float(input("Time? "))

    count = 0
    for option in statusList:#SHOW STATUS OPTIONS
        print(count,".",option, sep='',end='   ')
        count +=1
    print("\n")

    status = int(input("Status?"))#Gets int and selects status from list
    statusTitle = statusList[status]

    ticket = Ticket(customerName,dropOffDate,pickUpDate,device,repairs,repairTime,statusTitle)
    #
    #PRINT DETAILS and continue
    #


    with open('Tickets/'+ticket.customerName, 'w') as f:#Open local folder and write ticket to file
        f.write(ticket.customerName)
        f.write(str(int(ticket.dropOffDate)))
        f.write(str(int(ticket.pickUpDate)))
        f.write(ticket.device)
        f.write(ticket.repairs)
        f.write(str(float(ticket.repairTime)))
        f.write(statusTitle)
        f.close


def ShowAll():#Show all Tickets in folder
    allTickets = os.listdir("Tickets")
    for num in allTickets:
        print(num)

def Edit():
    #open and Edit with context menu
    return

def Delete():
    #delete Ticket
    return

def Select():
    #Select and show ticket
    return

def Export():
    #Change Directories
    filename = str("Bobby")
    new_file = open(filename+".txt","w")#Open selected Ticket
    new_file.close
    #Output Reciept
    return

def Filter():
    #find by input
    return






def RepairTypes():
    #select repair RepairTypes and append to ticket
    return

def CalcCost():
    #Calculate total cost, parts+Labour+tax
    return

def Summary():
    #summarise open/closed Tickets
    return


######################################################################LOGIC##############################################

#print("\x1b[31mThis is red text\x1b[0m") #ASNI Escape codes for bold text and colour, so f-ing cool! :0
#AddNew()
#ShowAll()
#Output()

