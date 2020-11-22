#
# ps8pr2.py  (Problem Set 8, Problem 2)
#
# A class to represent calendar dates       
#

class Date:
    """ A class that stores and manipulates dates that are
        represented by a day, month, and year.
    """

    # The constructor for the Date class.
    def __init__(self, init_month, init_day, init_year):
        """ constructor that initializes the three attributes  
            in every Date object (month, day, and year)
        """
        self.month = init_month
        self.day = init_day
        self.year = init_year


    # The function for the Date class that returns a string
    # representation of a Date object.
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that it is called on (named self).

            ** Note that this *can* be called explicitly, but
              it more often is used implicitly via printing or evaluating.
        """
        s = '%02d/%02d/%04d' % (self.month, self.day, self.year)
        return s

    def is_leap_year(self):
        """ Returns True if the called object is
            in a leap year, and False otherwise.
        """
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False

    def copy(self):
        """ Returns a new object with the same month, day, and year
            as the called object (self).
        """
        new_date = Date(self.month, self.day, self.year)
        return new_date

    #### Put your code for problem 2 below. ####
    #### Make sure that it is indented by an appropriate amount. ####

    def advance_one(self):
        '''This function changes the called object so that it represents
        one calendary day after the daye that it originally represented'''
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.is_leap_year()==True:
            days_in_month[2] = 29
        if self.day >= days_in_month[self.month] and self.month >= 12:
            self.day = 1
            self.month = 1
            self.year += 1
        elif self.day >=days_in_month[self.month]:
            self.day = 1
            self.month += 1
        else:
            self.day += 1
            
    def advance_n(self, n):
        '''This function changes the calling obkect so that it represents
        n calendar days after the date it was originally represented in. It also
        prints all the dates from the starting date to the ending one'''
        if n==0:
            print(self)
        else:
            print(self)
            for i in range(n):
                self.advance_one()
                print(self)
                
                
    def __eq__(self, other):
        '''This function returns True if the called object and the arguement
        represent the same calendar date, otherwise false'''
        if self.day == other.day and self.month == other.month and self.year == other.year:
            return True
        else:
            return False
    
    def is_before(self, other):
        '''This function returns True if the called object represents a calendar
        date that occurs before the calendar date that is represented by 'other'''
        if self.year < other.year:
            return True
        if self.year > other.year:
            return False
        if self.month<other.month:
            return True
        if self.month>other.month:
            return False
        if self.day<other.day:
            return True
        if self.day>other.day:
            return False
        else:
            return False
        
    def is_after(self, other):
        '''This function returns True si the calling object represents a calendar 
        date that occurs after the calendar date that is represented by 'other'''
        if self==other:
            return False
        elif self.is_before(other) == False:
            return True
        else:
            return False
        
        
    def days_between(self, other):
        '''This function returns an integer that represents the number of days between
        self and other'''
        j = self.copy()
        v = other.copy()
        if self == other:
            return 0
        x = 0
        if j.is_before(v) == True:
            while j.is_before(v):
                j.advance_one()
                x -= 1
        else: 
            while j.is_after(v):
                v.advance_one()
                x += 1
        return x
    
    def day_name(self):
        '''This function returns a string that indicates the name of the day of the week
        of them Date object that calls it.'''
        day_names = ['Monday', 'Tuesday', 'Wednesday', 
             'Thursday', 'Friday', 'Saturday', 'Sunday']
        req = self.days_between(Date(11, 9, 2020))%7
        return day_names[req]
            