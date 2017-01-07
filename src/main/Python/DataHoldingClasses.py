""" This module containts the data holding classes for the project Hotelreception

"""

__author__ = "6345060: Nico Kotlenga, 6293280: Umut Yilmaz"
__copyright__ = "Copyright 2016 – EPR-Goethe-Uni"
__email__ = "nico.kotlenga@stud.uni-frankfurt.de"

from datetime import date

class Person:
    """ This class represents a Person

    """
    def __init__(self, firstname, lastname, birthday):
        """ This method initialize a person object
            firstname: String
            lastname: String
            birthday: Date
        """

        self.__firstname = firstname
        self.__lastname = lastname
        self.__birthday = birthday

    def getFirstname(self):
        """ This method will return the firstname of the Person

        """
        return self.__firstname

    def getLastname(self):
        """ This method will return the lastname of the Person

        """
        return self.__lastname

    def getBirthday(self):
        """ This method will return the Birthday of the Person

        """
        return self.__birthday


class ReceptionEmployee(Person):
    """ This class represents a ReceptionEmployee

    """
    def __init__(self,firstname, lastname, birthday, maxHoursOfWork,\
     minHoursOfWork, wagePerHour):
        """ This method initialize a ReceptionEmployee-object.
            firstname: String
            lastname: String
            birthday: Date
            maxHoursOfWork: int
            minHoursOfWork: int
            wagePerHour: Double
        """
        Person.__init__(self,firstname, lastname, birthday)
        self.__maxHoursOfWork = maxHoursOfWork
        self.__minHoursOfWork = minHoursOfWork
        self.__wagePerHour = wagePerHour

    def getMaxHoursOfWork(self):
        """ This method return the max. count of workhours peer week for this
            employee

        """
        return self.__maxHoursOfWork

    def getMinHoursOfWork(self):
        """ This method return the min. count of workhours peer week for this
            employee

        """
        return self.__minHoursOfWork

    def getWagePerHour(self):
        """ This method returns the hourly wage for this employee

        """
        return self.__wagePerHour

class Customer(Person):
    """ This class represents a hotel customer

    """
    customerIDCounter = 0

    def __init__(self, firstname, lastname, birthday):
        """ This method initialize a customer object
            firstname: String
            lastname: String
            birthday: Date
        """

        Person.__init__(self,firstname , lastname, birthday)
        self.__bookings = list()
        self.__keys = list()
        self.__customerID = Customer.customerIDCounter
        Customer.customerIDCounter += 1

    def getCustomerID(self):
        """ This method will return the customer ID

        """
        return self.__customerID

    def getBookings(self):
        """ This method will return a list of all bookings of this customer

        """
        return self.__bookings
    def getKeys(self):
        """ This method will return a list of all rented keys of this customer

        """
        return self.__keys

    def appendBooking(self, newBooking):
        """ This method will append a booking to a customer
            newBooking: Booking
        """
        self.__bookings.append(newBooking)

    def removeBooking(self, selectedBooking):
        """ This method will remove a booking from the customer. This method
            is necesary to give the customer the possibility to cancel a
            booking.
            selectedBooking: booking
        """
        self.__bookings.remove(selectedBooking)

    def addKey(self, newKey):
        """ This method will add a key to the customer. This will be used to
            indicate that a specific key is rented from a customer
            newKey: Key
        """
        self.__keys.append(newKey)
    def removeKey(self, selectedKey):
        """ This method will remove  key from the customer. This method will
            be called during the checkout-process
            selectedKey: Key
        """
        self.__keys.remove(selectedKey)

class Key():
    """ This class represents a key fot a hotelroom

    """

    def __init__(self, keyForRoom):
        """This method initialize a key Object
           keyForRoom: Room
        """

        self.__keyForRoom = keyForRoom

    def getKeyForRoom(self):
        """ This mehtod will return the assigend room for the key object

        """
        return self.__keyForRoom

class Problem():
    """ This class represents a problem in a room object. It's a data class
        with getter and setter-methods

    """
    def __init__(self, description, problemReporter, assignedRoom):
        """ This method will initialize a Problem object.
            description: String
            problemReporter: Person
            assignedRoom: Room
        """
        self.__description = description
        self.__problemReporter = problemReporter
        self.__assignedRoom = assignedRoom

    def getDescription(self):
        """ This method will return the description of the Problem

        """
        return self.__description

    def getProblemReporter(self):
        """ This method will return the person who has reported the problem

        """

        return self.__problemReporter

    def getAssignedRoom(self):
        """ This method will return the assigned room

        """
        return self.__assignedRoom

class Transaction:
    """ This class represents a manuell entered Transaction for the finance
        manager. It's a data class with setter and getter methods

    """

    def __init__(self, description, value, dateOfTransaction):
        """ This method will initialize a Transaction object.
            description: String
            value: Double
            dateOfTransaction: Date
        """
        self.__description = description
        self.__value = value
        self.__dateOfTransaction = dateOfTransaction
        self.__income = True if self.__value > 0 else False

    def getDescription(self):
        """ This method will return the description of the Transaction

        """
        return self.__description

    def getValue(self):
        """ This mehtod will return the value of the Transaction

        """
        return self.__value

    def getIsIncome(self):
        """ This method returns a boolean value which describes whether the
            transaction is a income or a expense.
            true: income
            false: expense
        """
        return self.__income

    def getDateOfTransaction(self):
        """ This method return the date of Transaction

        """
        return self.__dateOfTransaction


class Workday:
    """ This class represents a workday. It contains the three workshifts of
        one workday and includes the ReceptionEmployee which is working on
        the specific shift.
        shift 1: 00:00 - 08:00
        shift 2: 08:00 - 16:00
        shift 3: 16:00 - 0:00

    """
    def __init__(self,dateOfDay, workshiftOne = list(), workshiftTwo = list(), workshiftThree = list()):
        """ This method initialize a workday
            workshiftOne: List<ReceptionEmployee>
            workshiftTwo: List<ReceptionEmployee>
            workshiftThree: List<ReceptionEmployee>
            dateOfDay: Date
        """
        self.__workshiftOne = workshiftOne
        self.__workshiftTwo = workshiftTwo
        self.__workshiftThree = workshiftThree
        self.dateOfDay = dateOfDay

    def addToWorkshift(self, shiftNr, receptionEmployee):
        """ This method will add a selected receptionEmployee to a shift
            shiftNr: int
            receptionEmployee: ReceptionEmployee
        """
        if(shiftNr == 1):
            self.__workshiftOne.append(receptionEmployee)
        elif(shiftNr == 2):
            self.__workshiftTwo.append(receptionEmployee)
        elif(shiftNr == 3):
            self.__workshiftThree.append(receptionEmployee)

    def getWorkshiftOne(self):
        """ This method will return the first workshift

        """
        return self.__workshiftOne

    def getWorkshiftTwo(self):
        """ This method will return the second workshift

        """
        return self.__workshiftTwo

    def getWorkshifThree(self):
        """ This method will return the third workshift

        """
        return self.__workshiftThree


class Booking:
    """ This method represents a booking item. The class has a static attribute
        which helps to generate a unique ID

    """
    bookingIdIncrement = 0
    def __init__(self, rentedRoom, dateOfArrival, dateOfDepature, price, paid,\
    curCustomer):
        """ This method will initialize a booking object.
            rentedRoom: Room
            dateOfArrival: Date
            dateOfDepature: Date
            price: Double
            paid: Boolean
            curCustomer: Customer
        """
        self.__rentedRoom = rentedRoom
        self.__dateOfArrival = dateOfArrival
        self.__dateOfDepature = dateOfDepature
        self.__price = price
        self.__paid = paid
        self.__curCustomer = curCustomer

    def getRentedRoom(self):
        """ This method returns the rented room of this booking

        """
        return self.__rentedRoom

    def getDateOfArrival(self):
        """ This method returns the date of arrival

        """
        return self.__dateOfArrival

    def getDateOfDepature(self):
        """ This method returns the date of depature

        """
        return self.__dateOfDepature

    def getPrice(self):
        """ This method returns the price of the booking

        """
        return self.__price

    def isPaid(self):
        """ This method will return a boolean value which describes whether
            the booking was paid by the customer

        """
        return self.__paid
    def setPaid(self, isPaid):
        """ This method will set the paid attribute

        """
        self.__paid = isPaid

    def getCurCustomer(self):
        """ This method returns the customer who created the booking

        """
        return self.__curCustomer


class Room:
    """ This class represents a hotelroom. It's a data class with getter
        and setter methods. It also has methods to check whether the room
        is free for a specific timespan.
    """

    def __init__(self, roomNumber, pricePerDay, description, keys):
        """ This mehtod initialize a room Object.
            roomNumber: int
            pricePerDay: Double
            descritpion: String
            keys: List<Key>
        """
        self.__roomNumber = roomNumber
        self._pricePerDay = pricePerDay
        self.__description = description
        self.__keys = keys
        self.__bookings = list()
        self.__lastCleaned = date.today()
        self.__problems = list()

    def isFree(self, arrivalDate, depatureDate):
        """ This method checks whether the room is free for this timespan.
            arrivalDate: Date
            depatureDate: Date
            The return value is a boolean:
            True: The room is free for the timespan
            False: The room isn't free for the timespan
        """
        for curBooking in self.__bookings:
            if(curBooking.getDateOfArrival() <= depatureDate or \
             curBooking.getDateOfDepature >= arrivalDate):
             return False

        return True

    def addBooking(self, newBooking):
        """ This method will append a new booking to the bookings list
            newBooking: Booking
        """
        self.__bookings.append(newBooking)

    def removeBooking(self, selectedBooking):
        """ This method will remove a selected booking from the booking list

        """
        self.__bookings.remove(selectedBooking)

    def needACleanup(self):
        """ This method returns a boolean value whether a cleanup is necesary
            A cleanup is necesary after 48 hours or after a person has
            checkout from a room
        """
        timedifference = date.today() - self.__lastCleaned
        if(timedifference.days >= 2):
            return True
        # now check for a checkout

        for curBooking in self.__bookings:
            if(curBooking.getDateOfDepature() > self.__lastCleaned):
                return True

        return False

    def setLastCleaned(self, cleaningDate):
        """ This method sets the last cleaning date. It has no return value
            cleaningDate: Date
        """

        self.__lastCleaned = cleaningDate
    def getProblems(self):
        """ This method will return the list of Problems

        """
        return self.__problems

    def getBookings(self):
        """ This method will return a list of all bookings

        """
        return self.__bookings

    def addProblem(self, newProblem):
        """ This method will apend a new Problem to the problem list
            newProblem: Problem
        """
        self.__problems.append(newProblem)

    def removeProblem(self, selectedProblem):
        """ This mehtod will remove a problem from the given problem list

        """
        self.__problems.remove(selectedProblem)

    def getKeys(self):
        """ This mehtod will return a list with all room keys

        """
        return self.__keys
        
    def getRoomNumber(self):
        """ This method will return the room number

        """
        return self.__roomNumber
