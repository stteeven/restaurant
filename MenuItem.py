# Steven Gong
# ITP 115, Fall 2019
# Final Project
# stevengo@usc.edu

# Create MenuItem class
class MenuItem(object):
    # Constructor for the class, with the following attributes
    def __init__(self, name, itemType, price, description):
        self.name = name
        self.itemType = itemType
        self.price = price
        self.description = description

    # Define getter methods for each attribute

    # Name: getName
    # Input: none
    # Output: returns a string with the MenuItem's name
    # Side effects: none
    # Description: gets MenuItem's name
    def getName(self):
        return self.name

    # Name: getItemType
    # Input: none
    # Output: returns a string with the item type
    # Side effects: none
    # Description: gets the item type of the item
    def getItemType(self):
        return self.itemType

    # Name: getPrice
    # Input: none
    # Output: returns a float with the price of the item
    # Side effects: none
    # Description: gets the item price
    def getPrice(self):
        return float(self.price)

    # Name: getDescription
    # Input: none
    # Output: returns a string with the description of the item
    # Side effects: none
    # Description: gets the item description
    def getDescription(self):
        return self.description

    # Define setter methods for each attribute

    # Name: setName
    # Input: a new name to set the item name to (string)
    # Output: none
    # Side effects: # Set name to new name if new name is alphabetical
    # Description: sets the name of the item
    def setName(self, newName):
        if newName.isalpha():
            self.name = newName
        else:
            print("Invalid input!")

    # Name: setItemType
    # Input: a new item type (string)
    # Output: none
    # Side effects: change item type of an item if the new item type is one of the given item types
    # Description: sets the item type of an item
    def setItemType(self, newItemType):
        if newItemType == "Appetizer" or "Drink" or "Dessert" or "Entree":
            self.itemType = newItemType
        else:
            print("Invalid input!")

    # Name: setPrice
    # Input: a new price to set the item price to
    # Output: none
    # Side effects: changes the price if the new price is a non-negative number
    # Description: sets the price of the item
    def setPrice(self, newPrice):
        if newPrice >= 0:
            self.price = newPrice
        else:
            print("Invalid input!")

    # Name: setDescription
    # Input: a new description for the item
    # Output: none
    # Side effects: Changes the description if the new description is alphabetical
    # Description: sets the item description
    def setDescription(self, newDescription):
        if newDescription.isalpha():
            self.description = newDescription
        else:
            print("Invalid input!")

    # Name: __str__
    # Input: none
    # Output: returns a string displaying the attributes of objects created
    # Side effects: none
    # Description: prints a message displaying the attributes of objects created
    def __str__(self):
        msg = self.name + " (" + self.itemType + "): $" + str(self.price)
        msg += "\n\t" + self.description
        return msg

