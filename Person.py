class Person:
    """ This class represents Person. It's a data class with
        getter methods for all attributes
    """

    def __init__(self, first_name, last_name, birthdate):
        """ This method will be called to initilialize an object of this class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate

    def get_Person(self):
        """ This method will return the attribute of a Person
        """
        return(self.first_name, self.last_name, self.birthdate)


    def get_first_name(self):
        """ This method will return the attribute first_name
        """
        return self.first_name

    def get_last_name(self):
        """ This method will return the last_name
        """
        return self.last_name

    def get_birthdate(self):
        """ This method will return the birthdate
        """
        return self.birthdate
