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

class FinanceManager:
    """ This class is a finance manager

    """
    def __init__(self):
        """ This method initialize a finance manager object
            It will get the manual transaction from the mySql Server.
            Also all bookings and a list of all ReceptionEmployee will be get
            from the server
        """
        try:
            self.__curSqlManager = SqlConnector()
            self.__transactions = self.__curSqlManager.getTransactions()
            self.__receptionEmployee = self.__curSqlManager.getReceptionEmployee()
            self.__bookings = self.__curSqlManager.getBookings()
        except RuntimeError:
            self.__transactions = list()
            self.__receptionEmployee = list()
            self.__bookings = list()

    def addTransaction(self, newTransaction):
        """ This method will add a transaction. If a database connection is
            established the transaction will also be saved into the database
            newTransaction: Transaction
        """
        self.__transactions.append(newTransaction)
        self.__curSqlManager.addTransactionToDatabase(newTransaction)

    def getBalanceFor(self, year, month):
        """ This method will return a double value wich represents the balance
            for a month and year
            year:int
            month: int
        """

        expenses = self.getExpensesFrom(year, month)
        incomes = self.getIncomeFrom(year, month)

        balance = 0

        for curExpenseTransaction in expenses:
            balance += curExpenseTransaction.getValue()

        for curIncomeTransaction in incomes:
            balance += curIncomeTransaction.getValue()

        return balance


    def getExpensesFrom(self, year, month):
        """ This method will return a list of transaction with expenses

        """
        returnValue = list()

        for curTransaction in self.__transactions:
            if(curTransaction.getDateOfTransaction().year == year and \
            curTransaction.getDateOfTransaction().month == month and \
            curTransaction.getIsIncome() == False):
                returnValue.append(curTransaction)

        return returnValue

    def getIncomeFrom(self, year, month):
        """ This method will return a list of all transaction with income

        """
        returnValue = list()

        # get the bookings for this month
        for curBooking in self.__bookings:
            if(curBooking.getDateOfArrival().year() == year and \
                curBooking.getDateOfArrival().month == month):
                newTransaction = Transaction("Rent of Room: " + \
                str(curBooking.getRentedRoom().getRoomNumber()), \
                curBooking.getPrice(), curBooking.getDateOfArrival())
                returnValue.append(newTransaction)

        for curTransaction in self.__transactions:
            if(curTransaction.getDateOfTransaction().year == year and \
            curTransaction.getDateOfTransaction().month == month and \
            curTransaction.getIsIncome()):
                returnValue.append(curTransaction)


class EmployeeManager:
    """ This class handles the management of employees
        It has functions to autogenerate a shiftplan and also to add and remove
        an employee

    """
    def __init__(self):
        """This method initialize an Employee manager object. It connect to a
           sql database to get the list of employees
        """
        try:
            self.__curSqlManager = SqlConnector()
            self.__receptionEmployees = self.__curSqlManager.getReceptionEmployees()
        except RuntimeError:
            self.__receptionEmployees = list()

        self.__generatedDays = list()

    def getGeneratedDays(self):
        """ This method will return the list with autogenerated days

        """
        return self.__generatedDays

    def setGeneratedDays(self, autogeneratedDays):
        """ This mehtod will set the autogenerated days. This method will be used
            from the IOTimeManager
        """
        self.__generatedDays = autogeneratedDays

    def exportAt(self, path):
        """ This method will export the autogenerated days into a textfile

        """
        curIOManager = IOTimeManager()
        curIOManager.exportToFile(path, self)

    def importFrom(self, path):
        """ This method import the autogenerated days from a file

        """
        curIOManager = IOTimeManager()
        curIOManager.importFromFile(path, self)

    def addReceptionEmployee(self, newEmployee):
        """ This method will add a reception employee. If a databaseConnection
            is established it also will be saved to the database
        """
        self.__receptionEmployees.append(newEmployee)
        if(self.__curSqlManager != None):
            self.__curSqlManager.addReceptionEmployeeToDatabase(newEmployee)

    def removeReceptionEmployee(self, selectedEmployee):
        """ This mehtod will remove a selected employee

        """
        self.__receptionEmployees.remove(selectedEmployee)
        if(self.__curSqlManager != None):
            self.__curSqlManager.removeReceptionEmployeeFromDatabase(selectedEmployee)

    def getReceptionEmployees(self):
        """ This method will return the Reception employees

        """
        return self.__receptionEmployees

    def autoGenerateForWeek(self, startDate, stopDate):
        """ This method will autogenerate a shiftplan for the given timespan
            It will return a boolean value wether the autp generating was possible
        """

        # check if the max employeeHourCount is possible
        listOfEmployees = list()
        maxHoursOfWork = 0
        for curEmployee in self.__receptionEmployees:
            listOfEmployees.append((curEmployee, \
            curEmployee.getMinHoursOfWork(), curEmployee.getMaxHoursOfWork(), 0))                maxHoursOfWork += curEmployee.getMaxHoursOfWork()
        if(maxHoursOfWork >= 24 * 7):
            for i in range(0,7,1):
                




        return False
