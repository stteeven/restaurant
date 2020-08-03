# Steven Gong
# ITP 115, Fall 2019
# Final Project
# stevengo@usc.edu

# Import classes from Diner.py and Menu.py
from Diner import Diner
from Menu import Menu


# Create Waiter class
class Waiter(object):
    # Name: constructor
    # Input: a Menu object
    # Output: none
    # Side effects: initializes a list of diners, assigns menu object input to the corresponding attribute
    # Description: Creates waiter object
    def __init__(self, menuObject):
        self.diners = []
        self.menu = menuObject

    # Name: addDiner
    # Input: a Diner object
    # Output: none
    # Side effects: adds the new Diner object to the list of diners
    # Description: adds the new Diner object to the list of diners
    def addDiner(self, dinerObject):
        self.diners.append(dinerObject)

    # Name: getNumDiners
    # Input: none
    # Output: an integer representing the number of diners the waiter is currently keeping track of
    # Side effects: none
    # Description: Gets the number of diners the waiter is keeping track of
    def getNumDiners(self):
        return len(self.diners)

    # Name: printDinerStatuses
    # Input: none
    # Output: none
    # Side effects: loops through each of the possible dining status a Diner has and prints the active diners by status
    # Description: prints all the diners the waiter is keeping track of, grouped by their statuses
    def printDinerStatuses(self):

        # Print all of the diners, grouped by status
        print("Diners who are seated:")
        for dinerObject in self.diners:
            if dinerObject.getStatus() == "seated":
                print("\t", dinerObject)
        print("Diners who are ordering:")
        for dinerObject in self.diners:
            if dinerObject.getStatus() == "ordering":
                print("\t", dinerObject)
        print("Diners who are eating:")
        for dinerObject in self.diners:
            if dinerObject.getStatus() == "eating":
                print("\t", dinerObject)
        print("Diners who are paying:")
        for dinerObject in self.diners:
            if dinerObject.getStatus() == "paying":
                print("\t", dinerObject)
        print("Diners who are leaving:")
        for dinerObject in self.diners:
            if dinerObject.getStatus() == "leaving":
                print("\t", dinerObject)

    # Name: takeOrders
    # Input: none
    # Output: none
    # Side effects: loops through the diner and checks if the diner's status is "ordering"
    #              loops through the different menu types for each diner that's ordering
    #              prints the menu items of each type and asks the diner to order an itme
    #              adds the item to the diner and prints the orders once the diner orders
    #              one menu item of each type
    # Description: takes orders of diners whose status is "ordering"

    def takeOrder(self):
        # loop through each diner in the list of diner objects
        for dinerObject in self.diners:
            # Do the following actions if the diner is "ordering"
            if dinerObject.getStatus() == "ordering":
                # For each menu item type...
                for menuItemType in Menu.MENU_ITEM_TYPES:
                    # Print the menu items of that type
                    Menu("menu.csv").printMenuItemsByType(menuItemType)
                    # Ask the user to select from the menu
                    print(dinerObject.getName() + ", please select a(n) " + menuItemType + " menu item number.")
                    userMenuSelection = int(input("> "))
                    # Error checking: ask for another user input if their selection is not in the range of numbers displayed in the menu
                    while userMenuSelection not in range(Menu("menu.csv").getNumMenuItemsByType(menuItemType)):
                        print("Invalid selection! Please choose again.")
                        userMenuSelection = int(input("> "))
                    # Assign the user's menu selection to the corresponding menu item object
                    if menuItemType == "Drink":
                        menuItemObject = Menu("menu.csv").menuItemDrinkList[userMenuSelection]
                    elif menuItemType == "Appetizer":
                        menuItemObject = Menu("menu.csv").menuItemAppetizerList[userMenuSelection]
                    elif menuItemType == "Entree":
                        menuItemObject = Menu("menu.csv").menuItemEntreeList[userMenuSelection]
                    elif menuItemType == "Dessert":
                        menuItemObject = Menu("menu.csv").menuItemDessertList[userMenuSelection]
                    # Append orders to the diner object's order list
                    dinerObject.addToOrder(menuItemObject)
                    # Print diner's order
                print(dinerObject.getName() + " ordered:")
                dinerObject.printOrder()

    # Name: ringUpDiners
    # Input: none
    # Output: none
    # Side effects: Loops through the list of diners and checks if the diner's status is "paying"
    #               calculates the meal cost of each diner who's paying and prints this in a message
    # Description: Calculates the diner's meal cost and prints it in a message
    def ringUpDiners(self):
        for dinerObject in self.diners:
            # Print the total cost in a statement if the diner's status is "paying"
            if dinerObject.getStatus() == "paying":
                print(dinerObject.getName() + ", your meal cost: $" + str(dinerObject.calculateMealCost()))

    # Name: removeDoneDiners
    # Input: none
    # Output: none
    # Side effects: loops through the list of diners and checks if the diner's status is "leaving"
    #               prints a message thanking the diner for each diner that's leaving
    #               loops through the list of diners backwards, and and removes each diner that's leaving
    # Description: finds diners that are leaving, prints a message thanking them, removes diners who are leaving
    def removeDoneDiners(self):
        for dinerObject in self.diners:
            # if the diner's status is "leaving"...
            if dinerObject.getStatus() == "leaving":
                # Print the total cost in a statement
                print(dinerObject.getName() + ", thank you for dining with us! Please come again!")
        # Remove diners who are leaving from the list by looping backwards through the diner list
        for num in range((len(self.diners) - 1), -1, -1):
            # If the status of the diner object is 4, remove the diner from the diners list
            if self.diners[num].getStatus() == "leaving":
                del self.diners[num]

    # Name: advanceDiners
    # Input: none
    # Output: none
    # Side effects: calls the printDinerStatuses() method, then call takeOrders(), ringUpDiners(),
    #               and removeDiners(). Then, update each diner's status.
    # Description: allows waiters to attend to the diners at their various stages as well as move
    #               each diner to the next stage
    def advanceDiners(self):
        self.printDinerStatuses()
        self.takeOrder()
        self.ringUpDiners()
        self.removeDoneDiners()
        # Update diner statuses
        for i in self.diners:
            i.updateStatus()
