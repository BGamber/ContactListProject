### Electronic Phonebook - Ben Gamber
### Look up, create, and modify contact entries

import os

running = True
userInput = ''
phonebook = [
    {'first': 'Default', 'last': 'User', 'number': '555-5555'},
    {'first': 'Test', 'last': 'User', 'number': '444-4444'}
]

## Print program header
def printHeader():
    os.system('clear')
    print 'Contact List'
    print '====================='

## Return entry's first name
def getFirstName(entry):
    return entry['first']

## Return entry's last name
def getLastName(entry):
    return entry['last']

## Return entry's phone number
def getPhoneNumber(entry):
    return entry['number']

## Look up an entry
def lookUpEntry():
    printHeader()
    print "Look Up Entry"

    count = 0
    search = raw_input("Search for entry: ").lower()

    printHeader()

    sortedList = sorted(phonebook, key=getFirstName)
    for i in xrange(len(phonebook)):
        first = phonebook[i]['first']
        last = phonebook[i]['last']
        full = "%s %s" % (phonebook[i]['first'], phonebook[i]['last'])
        num = phonebook[i]['number']
        if search == (first.lower()) or search == (last.lower()) or search == (full.lower()) or search == num:
            first = phonebook[i]['first']
            last = phonebook[i]['last']
            number = phonebook[i]['number']
            print '%s %s: %s\n' % (first, last, number)
            count += 1
    if count == 0:
        print "No entry found for '%s'." % search.capitalize()
    raw_input("Press 'Enter' to continue...")
    

## Create an entry
def createEntry():
    printHeader()
    print "Create Entry"

    count = 0
    name = raw_input("Enter name: ")
    if len(name.split(" ")) > 1:
        first = name.split(' ')[0]
        last = name.split(' ')[1]
    else:
        first = name
        last = raw_input("Enter last name: ")
    phone = raw_input("Enter phone number: ")
    phonebook.append({'first': first.capitalize(), 'last': last.capitalize(), 'number': phone})
    print "\nEntry set for %s %s: %s" % (first, last, phone)
    raw_input("Press 'Enter' to continue...")

## Delete an entry
def deleteEntry():
    printHeader()
    print "Delete Entry"

    count = 0
    search = raw_input("Enter full name: ")
    i = 0
    listLength = len(phonebook)
    while i < listLength:
        full = "%s %s" % (phonebook[i]['first'], phonebook[i]['last'])
        if search == full:
            if raw_input("Delete %s (%s)? (y/n): " % (full, phonebook[i]['number'])) == 'y':
                phonebook.pop(i)
                print "Entry deleted for %s." % search
                listLength -= 1
                i -= 1
                count += 1
            else:
                print "Entry skipped."
                count += 1
        i += 1
    if count == 0:
        print "No entry found for '%s'." % search
    raw_input("Press 'Enter' to continue...")

## List all entries
def listEntries():
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
        sortedList = sorted(phonebook, key=getFirstName)
    elif select == '3':
        sortedList = sorted(phonebook, key=getPhoneNumber)
    else:
        sortedList = sorted(phonebook, key=getLastName)

    printHeader()

    if len(sortedList) == 0:
        print "Contact list empty."
    else:
        for i in range(len(sortedList)):
            first = sortedList[i]['first']
            last = sortedList[i]['last']
            number = sortedList[i]['number']
            print '%s %s: %s\n' % (first, last, number)
    raw_input("Press 'Enter' to continue...")

## Clear screen and list options
def printMenu():
    printHeader()
    print '1. Look up an entry'
    print '2. Create an entry'
    print '3. Delete an entry'
    print '4. List all entries'
    print '5. Quit'

## Main loop
while running:
    printMenu()
    userInput = raw_input("Select an option: ")
    if userInput == '1':
        lookUpEntry()
    elif userInput == '2':
        createEntry()
    elif userInput == '3':
        deleteEntry()
    elif userInput == '4':
        listEntries()
    elif userInput == '5':
        running = False
        os.system('clear')