#Name: Sophia Philips
#GitHub Username: sophiacphilips
#Date: 1/23/23
#This code is designed to create a library simulator comprised of three classes; libraryitem, patron, and library.
# This can be used to create multiple libraries that have their own collections of items and patrons.
# The simulator allows the user to check items out to patrons, return items, move item locations, create fines, pay fines and add new patrons.


class LibraryItem:
    """Libraryitem class represents a library item that a patron can check out from a library"""
    def __init__(self, library_item_id, title): #taking library item id and title as parameters

        self._library_item_id = library_item_id #initializes lib item id
        self._title = title #initializes title of book to be checked out
        self._location= "ON_SHELF" #all books to be checked out start on the shelf
        self._checked_out_by = None #initialized checked out book to none
        self._requested_by = None #initialized requests to none
        self._date_checked_out= 0 #sets date of check out to zero (books, albums, films all have different check out lengths)

    def get_library_item_id(self):
        """returns library item's id"""
        return self._library_item_id

    def get_title(self):
        """returns library item's title"""
        return self._title

    def get_location(self):
        """returns library item's locations"""
        return self._location

    def set_location(self, location):
        """sets library item's location (on shelf, hold, or checked out)"""
        self._location = location

    def get_checked_out_by(self):
        """returns library item's check out patron"""
        return self._checked_out_by
    def set_checked_out_by(self, patron):
        """sets library item's check out patron"""
        self._checked_out_by = patron

    def get_requested_by(self):
        """returns patron that requested lib item"""
        return self._requested_by
    def set_requested_by(self, patron):
        """sets patron that requested lib item"""
        self._requested_by = patron

    def get_date_checked_out(self):
        """returns check out date of lib item"""
        return self._date_checked_out
    def set_date_checked_out(self, current_date):
        """sets check out date of lib item"""
        self._date_checked_out = current_date

class Book(LibraryItem):
    """inherits library item as a class and creates new class for books only"""
    def __init__(self, library_item_id, title, author): #initializes book's author
        super().__init__(library_item_id, title) #uses super() to pull initialization/parameters/methods from inherited class
        self._author = author #initializes author of books (not included in class libraryitem)

    def get_author(self):
        """returns get author for book"""
        return self._author

    def get_check_out_length(self):
        """returns length of time book is available for checkout"""
        return 21

class Album(LibraryItem):
    """inherits library item as a class and creates new class for albums only"""
    def __init__(self, library_item_id, title, artist): #initializes album artist
        super().__init__(library_item_id, title) #uses super() to pull init methods from inheritance class libraryitem
        self._artist = artist #initializes artist of album

    def get_artist(self):
        """returns get artist for album"""
        return self._artist

    def get_check_out_length(self):
        """returns check out length for albums"""
        return 14

class Movie(LibraryItem):
    """initializes library item as an inheritance class and creates new class for movies only"""
    def __init__(self, library_item_id, title, director): #initializes movie director for movie class
        super().__init__(library_item_id, title) #uses super() to pull init methods from inheritance class libraryitem
        self._director = director #initializes director of movie

    def get_director(self):
        """returns director of movie"""
        return self._director

    def get_check_out_length(self):
        """retuns check out length for movies"""
        return 7

class Patron:
    """represents patrons of a library and initializes their attributes"""
    def __init__(self, patron_id, name):
        self._patron_id = patron_id #init patron id number (specific to each patron)
        self._name = name #init patron name (could be repeats as names are not unique)
        self._checked_out_items = [] #init collection of library items that patron currently has checked out
        self._fine_amount = 0 #init fine amount that the patron owes the library in late fees

    def get_fine_amount(self):
        """returns fine amount"""
        return self._fine_amount
    def set_fine_amount(self, fine_amount):
        """sets new fine amount for patron"""
        self._fine_amount = fine_amount

    def get_patron_id(self):
        """returns patron id"""
        return self._patron_id
    def set_patron_id(self, patron_id):
        """sets patron id if they are not currently members of the library"""
        self._patron_id = patron_id

    def get_name(self):
        """returns patron name"""
        return self._name
    def set_name(self, name):
        """sets patron name for new members"""
        self._name = name

    def get_checked_out_items(self):
        """returns patron's checked out items"""
        return self._checked_out_items

    def add_library_item(self, item):
        """adds specified LibraryItem to patron's checked out items"""
        return self._checked_out_items.append(item)

    def remove_library_item(self, item):
        """removes specified LibraryItem from patron's checked out items"""
        return self._checked_out_items.remove(item)

    def amend_fine(self, fine):
        self._fine_amount += fine
        """allows fine to be added or subtracted from patron's account"""

class Library:
    """represents a library and its items (holdings)/patrons(members)"""
    def __init__(self):
        self._holdings = [] #inits items that belong to the library
        self._members = [] #inits patrons that hold library membership
        self._current_date = 0 #initialization of date that library object was created

    def add_library_item(self, LibraryItem):
        """takes a LibraryItem object and adds it to holdings"""
        self._holdings.append(LibraryItem)

    def add_patron(self, Patron):
        """takes a patron object and adds it to members"""
        self._members.append(Patron)

    def lookup_library_item_from_id(self, library_item):
        """allows user to check if a library item is in holdings"""
        for l_i in self._holdings: #iterates through holdings to see if library item id is present, if present returns item if not in holdings returns none
            if l_i._get_library_item_id() == library_item:
                return l_i
            else:
                return None

    def lookup_patron_from_id(self, patron):
        """checks if patron id is in members collection, returns none if they are not a member"""
        for p in self._members:
            if p._get_patron_id() == patron:
                return p
            else:
                return None

    def check_out_library_item(self, patron_id, library_item_id):
        """allows library item to be checked out, and"""
        for p in self._members:
            if p.get_patron_id() != patron_id: #checks if patron is library member
                return "patron not found"
            else:
                for i in self._holdings:
                    if i.get_library_item_id() != library_item_id: #checks if item is in library holdings
                        return "item not found"
                    else:
                        if i.get_location() == "CHECKED_OUT": #checks if item is already checked out
                            return "item already checked out"
                        else:
                            if i.get_location() == "ON_HOLD_SHELF": #checks if item is on hold
                                return "item on hold by other patron"
                            else:
                                if i.get_requested_by() == p: #if on hold, item added to patron's requests
                                    i.set_requested_by(None)

                                    i.set_checked_out_by(p) #if not on hold or checked out, item checked out to patron
                                    i.set_date_checked_out(self._current_date) #date of checkout set
                                    i.set_location("CHECKED_OUT") #location of item set
                                    p.add_library_item(i) #item added to patron's checked out list
                                    return "check out successful" #when able to be checked out this message is returned

    def return_library_item(self, library_item_id):
        """allows patron to return library item"""
        for i in self._holdings: #determines if item belongs to library's holdings
            if i.get_library_item_id() != library_item_id: #returns message if item not in holdings
                return "item not found"
            else:
                if i.get_location() == "ON_SHELF" or "ON_HOLD_SHELF": #if item is on shelf or held, returns following message
                    return "item already in library"
                else:
                    if i.get_location() == "CHECKED_OUT":
                        patron= i.get_checked_out_by() #gets list of items checked out by patron
                        patron.remove_library_item(i) #removes returned item from list of patron's checked out items

                        if i.get_requested_by() == None: #sets new location of item
                            return i.set_location("ON_SHELF")
                        else:
                            return i.set_location("ON_HOLD_SHELF")

            return "return successful"

    def request_library_item(self, patron_id, library_item_id):
        """requests a library item to be put on hold/requested for a patron"""
        for p in self._members:
            if p.get_patron_id() != patron_id:
                return "patron not found" #checks for patron in members list

            for i in self._holdings: #iterates through holdings for item
                if i.get_library_item_id() != library_item_id:
                    return "item not found"
                else: #If item already on hold
                    if i.get_location() == "ON_HOLD_SHELF":
                        return "item already on hold"
                    i._set_requested_by(p) #add on hold item to requested by patron

                    if i.get_location() == "ON_SHELF": #if item available on shelf, update to on hold
                        return i.set_location("ON_HOLD_SHELF")
        return "request successful"

    def pay_fine(self, patron_id, amount_paid):
        """allows patron to pay fine existing for their items"""
        for p in self._members:
            if p.get_patron_id() != patron_id: #checks for patron in members
                return "patron not found"
            p.amend_fine.remove(amount_paid) #removes total amount paid from existing fine balance
        return "payment succesful"

    def increment_current_date(self):
        """increases patron's fines by 10 cents for each overdue day"""
        self._current_date +=1 #adds 1 day each day from check out
        for p in self._members:
            for i in p.get_checked_out_items():
                if (self._current_date - i.get_date_checked_out()) > i.get_check_out_length():
                    p.amend_fine(+0.10)


b1 = Book("345", "Phantom Tollbooth", "Juster")
b2= Book("666", "Persuasion", "Jane Austen")
print(b1.get_author())
print(b2.get_author())

p1 = Patron("abc", "Felicity")
p2 = Patron("bcd", "Waldo")

lib = Library()
lib.add_library_item(b1)
lib.add_library_item(b2)
lib.add_patron(p1)
lib.add_patron(p2)

lib.check_out_library_item("bcd", "456")
for _ in range(7):
    lib.increment_current_date()  # 7 days pass
    lib.check_out_library_item("abc", "567")
    loc = b1.get_location()
    lib.request_library_item("abc", "456")
for _ in range(57):
    lib.increment_current_date()  # 57 days pass
    p2_fine = p2.get_fine_amount()
    lib.pay_fine("bcd", p2_fine)
    lib.return_library_item("456")
























