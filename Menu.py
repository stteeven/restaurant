# Steven Gong
# ITP 115, Fall 2019
# Final Project
# stevengo@usc.edu

# import MenuItem class from MenuItem file
from MenuItem import MenuItem

# Create Menu class
class Menu(object):

    # Static variable
    MENU_ITEM_TYPES = ["Drink", "Appetizer", "Entree", "Dessert"]

    # Name: __init__ ; this is the constructor
    # Input: fileName containing menu information
    # Output: none
    # Side effects: initializes lists for each menu item type, creates menu objects from the given file
    #               organizes the menu items by type
    # Description: creates the menu from the file
    def __init__(self, fileName):
        # Initialize empty lists for each menu item type
        self.menuItemDrinkList = []
        self.menuItemAppetizerList = []
        self.menuItemEntreeList = []
        self.menuItemDessertList = []
        # Set the file name
        fileName = "menu.csv"
        self.fileName = fileName
        # Open the file
        fileIn = open(fileName, "r")
        # Read the file
        for line in fileIn:
            # Strip each line of whitespace
            line = line.strip()
            # Split the line into a list
            line = line.split(",")
            # Create a new object from each line
            menuItemObject = MenuItem(line[0], line[1], line[2], line[3])
            # Append menu items to their corresponding category lists
            if menuItemObject.getItemType() == "Appetizer":
                self.menuItemAppetizerList.append(menuItemObject)
            elif menuItemObject.getItemType() == "Drink":
                self.menuItemDrinkList.append(menuItemObject)
            elif menuItemObject.getItemType() == "Entree":
                self.menuItemEntreeList.append(menuItemObject)
            elif menuItemObject.getItemType() == "Dessert":
                self.menuItemDessertList.append(menuItemObject)

    # Name: getMenuItem
    # Inputs: a string representing a type of menu item and an integer of the index position of a certain menu item
    # Outputs: a MenuItem object from one of the menuItem lists
    # Side effects: none
    # Description: gets menuItem objects using the menu item type and index number
    def getMenuItem(self, menuItemType, menuItemIndex):
        if menuItemType == "Appetizer":
            return self.menuItemAppetizerList[menuItemIndex]
        elif menuItemType == "Drink":
            return self.menuItemDrinkList[menuItemIndex]
        elif menuItemType == "Entree":
            return self.menuItemEntreeList[menuItemIndex]
        elif menuItemType == "Dessert":
            return self.menuItemDessertList[menuItemIndex]

    # Name: printMenuItemsByType
    # Inputs: a string representing a type of menu item
    # Outputs: none
    # Side effects: none
    # Description: prints a header with the type of menu items, followed by a numbered list
    # of all menu items of that type
    def printMenuItemsByType(self, menuItemType):
        print("-----" + menuItemType.upper() + "-----")
        if menuItemType == "Appetizer":
            menuItemList = self.menuItemAppetizerList
        elif menuItemType == "Drink":
            menuItemList = self.menuItemDrinkList
        elif menuItemType == "Entree":
            menuItemList = self.menuItemEntreeList
        elif menuItemType == "Dessert":
            menuItemList = self.menuItemDessertList
        else:
            print("Invalid input!")
        for num in range(0,len(menuItemList)):
            print(num, ") ", menuItemList[num])

    # Name: getNumMenuItemsByType
    # Inputs: a string representing a type of menu item
    # Outputs: an integer representing the number of menu items of the input type
    # Side effects: none
    # Description: prints a header with the type of menu items, followed by a numbered list of all menu items of that type
    def getNumMenuItemsByType(self, menuItemType):
        if menuItemType == "Appetizer":
            return len(self.menuItemAppetizerList)
        elif menuItemType == "Drink":
            return len(self.menuItemDrinkList)
        elif menuItemType == "Entree":
            return len(self.menuItemEntreeList)
        elif menuItemType == "Dessert":
            return len(self.menuItemDessertList)



