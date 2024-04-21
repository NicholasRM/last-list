from random import randint

class DateTime:
    def __init__(self,
                 year = 0,
                 month = 0,
                 day = 0,
                 hour = 0, 
                 minute = 0,
                 second = 0):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        
    def __int__ (self):
        #BIT LAYOUT
        #y = year (infinite bits)
        #M = month (3 bits)
        #d = day (4 bits)
        #h = hours (4 bits)
        #m = minutes (5 bits)
        #s = seconds (5 bits)
        #y......yMMMddddhhhhmmmmmsssss

        datetime = 0
        datetime |= self.second
        datetime |= self.minute << 5
        datetime |= self.hour << 10
        datetime |= self.day << 14
        datetime |= self.month << 18
        datetime |= self.year << 21
        
        return datetime
    
    def as_integer(self):
        return self.__int__()
    
    def set_integer(self, integer):
        self.second = integer & 0b11111
        integer >>= 5
        self.minute = integer & 0b11111
        integer >>= 5
        self.hour = integer & 0b1111
        integer >>= 4
        self.day = integer & 0b1111
        integer >>= 4
        self.month = integer & 0b111
        integer >>= 3
        self.year = integer
    
    def sql_format(self):
        y = self.year
        mo = self.month
        d = self.day
        h = self.hour
        m = self.minute
        s = self.second
        return f"'{y:4}-{mo:2}-{d:2} {h:2}:{m:2}:{s:2}'"
    
    @staticmethod
    def from_integer(integer):
        dt = DateTime()
        dt.set_integer(integer)
        return dt
    
class DateTimeGenerator:
    def __init__(self):
        self.min_day = 1
        self.max_day = 28
        self.min_month = 1
        self.max_month = 12
        self.min_year = 2000
        self.max_year = 2024
        self.min_hour = 9
        self.max_hour = 22
        self.min_minute = 0
        self.max_minute = 59
        self.min_second = 0
        self.max_second = 59
        self.max_datetime = DateTime(2024,4,20,23,59,59)
        
    def generate_datetime(self):
        dt = DateTime()
        dt.second = randint(self.min_second, self.max_second)
        dt.minute = randint(self.min_minute, self.max_minute)
        dt.hour = randint(self.min_hour, self.max_hour)
        dt.day = randint(self.min_day, self.max_day)
        dt.month = randint(self.min_month, self.max_month)
        dt.year = randint(self.min_year, self.max_year)
        
        if int(dt) > int(self.max_datetime):
            return self.max_datetime
        else:
            return dt
        