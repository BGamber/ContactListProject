### Electronic Contact List - Ben Gamber
### Look up, create, and modify contact entries

import os, time, pickle

class Contact(object):
    def __init__(self, first, last, phone):
        self.first = first
        self.last = last
        self.full_name = "%s %s" % (self.first, self.last)
        self.phone = phone
    
    def getFirstName(self):
        return self.first
    
    def getLastName(self):
        return self.last

    def getFullName(self):
        return self.full_name

    def getPhoneNumber(self):
        return self.phone

def getContactFirst(contact):
    return contact.getFirstName()

def getContactLast(contact):
    return contact.getLastName()

def getContactNumber(contact):
    return contact.getPhoneNumber()

## Print program header
def printHeader():
    os.system('clear')
    print 'Contact List'
    print '====================='

## Look up an entry
def lookUpEntry(contactlist):
    printHeader()
    print "Look Up Entry"

    count = 0
    search = raw_input("Search for entry: ").capitalize()

    printHeader()

    sortedList = sorted(contactlist, key=getContactFirst)
    for contact in contactlist:
        first = contact.getFirstName()
        last = contact.getLastName()
        full = contact.getFullName()
        num = contact.getPhoneNumber()
        if search == first or search == last or search == full or search == num:
            print '%s %s: %s\n' % (first, last, num)
            count += 1
    if count == 0:
        print "No entry found for '%s'." % search
    raw_input("Press 'Enter' to continue...")
    

## Create an entry
def createEntry(contactlist):
    printHeader()
    print "Create Entry"

    count = 0
    name = raw_input("Enter name: ")
    nameSplit = name.split(" ")
    if len(nameSplit) > 1:
        first = nameSplit[0]
        last = " ".join(nameSplit[1:])
    else:
        first = name
        last = raw_input("Enter last name: ")
    phone = raw_input("Enter phone number: ")
    newcontact = Contact(first, last, phone)
    contactlist.append(newcontact)
    print "\nEntry set for %s %s: %s" % (first, last, phone)
    raw_input("Press 'Enter' to continue...")

## Delete an entry
def deleteEntry(contactlist):
    printHeader()
    print "Delete Entry"

    newContactList = []
    count = 0
    search = raw_input("Enter name: ").capitalize()
    for contact in contactlist:
        first = contact.getFirstName()
        last = contact.getLastName()
        full = contact.getFullName()
        nameAndNum = "%s (%s)" % (full, contact.getPhoneNumber())
        if search == first or search == last or search == full:
            if raw_input("Delete %s? (y/n): " % (nameAndNum)) == 'y':
                print "Entry deleted for %s." % (nameAndNum)
                count += 1
            else:
                print "Entry skipped."
                newContactList.append(contact)
                count += 1
        else:
            newContactList.append(contact)
    if count == 0:
        print "No entry found for '%s'." % search
    raw_input("Press 'Enter' to continue...")
    return newContactList

## List all entries
def listEntries(contactlist):
    select = ''
    sortedList = []
    printHeader()
    print "List Entries"
    print "Sort by:"
    print "1. First Name"
    print "2. Last Name"
    print "3. Phone Number"
    select = raw_input("Select an option: ")
    if select == '1':
        sortedList = sorted(contactlist, key=getContactFirst)
    elif select == '3':
        sortedList = sorted(contactlist, key=getContactNumber)
    else:
        sortedList = sorted(contactlist, key=getContactLast)

    printHeader()

    if len(sortedList) == 0:
        print "Contact list empty."
    else:
        for contact in sortedList:
            full = contact.getFullName()
            number = contact.getPhoneNumber()
            print '%s: %s\n' % (full, number)
    raw_input("Press 'Enter' to continue...")

def loadContactList():
    newContactList = []
    try:
        open('contactlist.pickle')
    except IOError:
        print "No saved contact list found."
    else:
        with open('contactlist.pickle', 'r') as f:
            newContactList = pickle.load(f)
        print "Contact list loaded."
        time.sleep(0.5)
    return newContactList

def saveContactList(contactlist):
    print "Saving contact list..."
    with open('contactlist.pickle', 'w') as f:
        pickle.dump(contactlist, f)
    time.sleep(0.5)
## Clear screen and list options
def printMenu():
    printHeader()
    print '1. Look up an entry'
    print '2. Create an entry'
    print '3. Delete an entry'
    print '4. List all entries'
    print '5. Quit'

userInput = ''
contactlist = loadContactList()

## Test Data
# test_user1 = Contact('Test', 'User', '555-5555')
# test_user2 = Contact('Default', 'User', '000-0000')
# contactlist.append(test_user1)
# contactlist.append(test_user2)

## Main loop
while userInput != '5':
    printMenu()
    userInput = raw_input("Select an option: ")
    if userInput == '1':
        lookUpEntry(contactlist)
    elif userInput == '2':
        createEntry(contactlist)
    elif userInput == '3':
        contactlist = deleteEntry(contactlist)
    elif userInput == '4':
        listEntries(contactlist)
    elif userInput == '5':
        saveContactList(contactlist)
        os.system('clear')