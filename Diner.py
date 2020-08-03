# Steven Gong
# ITP 115, Fall 2019
# Final Project
# stevengo@usc.edu

from MenuItem import MenuItem

class Diner(object):

    # Initialize class variable
    STATUSES = ["seated", "ordering", "eating", "paying", "leaving"]

    # Constructor
    def __init__(self, name):
        self.name = name
        self.order = []
        self.status = 0

    # Define getters

    # Name: getName
    # Input: none
    # Output: returns the name of the diner
    # Side effects: none
    # Description: gets diner's name
    def getName(self):
        return self.name

    # Name: getOrder
    # Input: none
    # Output: returns the order of the diner
    # Side effects: none
    # Description: gets diner's order
    def getOrder(self):
        return self.order

    # Name: getStatus
    # Input: none
    # Output: returns a string representing the diner's status
    # Side effects: none
    # Description: gets the status of the diner
    def getStatus(self):
        # Only get the diner's status if it is one of the statuses in the status list
        if self.status in range(5):
            # Assign the diner's status number to its corresponding position in the list to get the status description
            statusDescription = Diner.STATUSES[self.status]
            return statusDescription

    # Define setters

    # Name: updateStatus
    # Input: none
    # Return value: none
    # Side effects: increases the diner's status by 1
    # Description: increases the diner's status by 1, which effectively updates the status
    def updateStatus(self):
        self.status += 1

    # Name: addToOrder
    # Input: a MenuItem object
    # Return value: none
    # Side effects: adds the menu item to the end of the list of menu items
    # Description: Adds the menu item to the end of the list of menu items, effectively adding to the order
    def addToOrder(self, menuItemObject):
        self.order.append(menuItemObject)

    # Name: printOrder
    # Input: none
    # Return value: none
    # Side effects: prints a message w/ all menu items
    # Description: prints a message containing all the menu items the diner ordered
    def printOrder(self):
        for i in self.order:
            print(i)

    # Name: calculateMealCost
    # Input: none
    # Return value: a float representing the total cost of the diner's meal
    # Side effects: none
    # Description: totals up the cost of each of the menu items the diner ordered
    def calculateMealCost(self):
        totalCost = 0
        for i in self.order:
            totalCost += i.getPrice()
        return totalCost

    # Name: __str__
    # Input: none
    # Output: returns a string displaying the attributes of objects created
    # Side effects: none
    # Description: prints a message displaying the attributes of objects created
    def __str__(self):
        # Assign the diner's status number to its corresponding position in the list to get the status description
        status = Diner.STATUSES[self.status]
        # Create message
        msg = "Diner " + str(self.name) + " is currently " + str(status) + "."
        return msg
