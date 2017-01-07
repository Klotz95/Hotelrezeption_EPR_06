""" This module contains the manager classes for the project Hotelreception

"""

__author__ = "6345060: Nico Kotlenga, 6293280: Umut Yilmaz"
__copyright__ = "Copyright 2016 – EPR-Goethe-Uni"
__email__ = "nico.kotlenga@stud.uni-frankfurt.de"

from datetime import date

from DataHoldingClasses.py import Customer, Person, ReceptionEmployee, Key, \
Problem, Transaction, Workday, Booking, Room

class BookingManager:
    """ This class handles the creation and deletion of bookings.
        It also offers some RoomManagement methods like
        'give a list for all rooms which need a cleanup' and so on
    """

    def __init__(self):
        """ This method will initialize the BookingManager. Please be patient
            that if no connection to the sql server could be established an
            empty data set will be created
        """
        try:
            self.__curSqlManager = SqlConnector()
            self.__rooms = self.__curSqlManager.getRooms()
            self.__bookings = __curSqlManager.getBookings()
            self.__customers = __curSqlManager.getCustomers()
            self.__problems = list()
        except RuntimeError:
            print("Couldn't load sql Connector. A empyt data set will be created")
            self.__rooms = list()
            self.__bookings = list()
            self.__customers = list()
            self.__problems = list()

    def getRooms(self):
        """ This mehtod will return a list of all rooms

        """
        return self.__rooms

    def getBookings(self):
        """ This method will return a list with all bookings

        """
        return self.__bookings

    def getCustomers(self):
        """ This method will return a list with all customers

        """
        return self.__customers

    def makeBooking(self, customer, selectedRoom, dateOfArrival, dateOfDepature, \
    paid):
        """ This method will create a booking. As a result will be a Double
            value which represents the price of the booking
            customer: Customer
            selectedRoom: Room
            dateOfArrival: Date
            dateOfDepature: Date
            paid: boolean
        """
        dayCount = dateOfDepature - dateOfArrival
        price = dayCount.days * selectedRoom.getPrice()

        newBooking = Booking(selectedRoom, dateOfArrival, dateOfDepature, price, paid)
        customer.appendBooking(newBooking)
        selectedRoom.addBooking(newBooking)
        self.__bookings.append(newBooking)

        #save the booking into the database
        if(self.__curSqlManager != None):
            self.__curSqlManager.addBookingToDatabase(newBooking)

    def payBooking(self, selectedBooking):
        """ This method will set the selectedBooking as paid
            selectedBooking: Booking
        """
        selectedBooking.setPaid(True)

    def cancelBooking(self, selectedBooking):
        """ This method will cancel a selected Booking and delete all references
            selectedBooking: Booking
        """

        associatedRoom = selectedBooking.getRentedRoom()
        associatedCustomer = selectedBooking.getCurCustomer()
        self.__bookings.remove(selectedBooking)
        associatedRoom.removeBooking(selectedBooking)
        associatedCuStomer.removeBooking(selectedBooking)
        if(self.__curSqlManager != None):
            self.__curSqlManager.removeBookingFromDatabase(selectedBooking)

    def addCustomer(self, newCustomer):
        """ This method will add a new customer

        """
        self.__customers.append(newCustomer)
        if(self.__curSqlManager != None):
            self.__curSqlManager.addCustomerToDatabase(newCustomer)

    def addRoom(self, newRoom):
        """ This methd will add a new room

        """
        self.__rooms.append(newRoom)
        if(self.__curSqlManager != None):
            self.__curSqlManager.addRoomToDatabase(newRoom)

    def getFreeRoomsForTimespan(self, dateOfArrival, dateOfDepature):
        """ This mehtod will return a list of all free rooms for a timespan
            dateOfArrival: Date
            dateOfDepature: Date

        """
        returnValue = list()

        for curRoom in self.__rooms:
            if(curRoom.isFree(dateOfArrival, dateOfDepature)):
                returnValue.append(curRoom)

        return returnValue

    def getListOfProblems(self):
        """ This method will return the list of problems

        """
        return self.__problems

    def addProblem(self, selectedRoom, description, problemReporter):
        """ This mehtod will add a problem to the list

        """
        newProblem = Problem(description, problemReporter, selectedRoom)
        self.__problems.append(newProblem)
        selectedRoom.addProblem(newProblem)

    def removeProblem(self, selectedProblem):
        """ This method will remove a problem with all associations

        """
        selectedProblem.getAssignedRoom().removeProblem(selectedProblem)
        self.__problems.remove(selectedProblem)

    def getListOfToCleanRooms(self):
        """ This method will return a list of rooms which need a cleanup

        """
        returnValue = list()

        for curRoom in self.__rooms:
            if(curRoom.needACleanup()):
                returnValue.append(curRoom)

    
