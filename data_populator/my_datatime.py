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
        #M = month (4 bits)
        #d = day (5 bits)
        #h = hours (5 bits)
        #m = minutes (6 bits)
        #s = seconds (6 bits)
        #y......yMMMddddhhhhmmmmmsssss
        
        datetime = 0
        datetime |= self.second
        datetime |= self.minute << 6
        datetime |= self.hour << 12
        datetime |= self.day << 17
        datetime |= self.month << 22
        datetime |= self.year << 26
        
        return datetime
    
    def as_integer(self):
        return self.__int__()
    
    def set_integer(self, integer):
        #BIT LAYOUT
        #y = year (infinite bits)
        #M = month (4 bits)
        #d = day (5 bits)
        #h = hours (5 bits)
        #m = minutes (6 bits)
        #s = seconds (6 bits)
        #y......yMMMddddhhhhmmmmmsssss
        self.second = integer & 0b111111
        integer >>= 6
        self.minute = integer & 0b111111
        integer >>= 6
        self.hour = integer & 0b11111
        integer >>= 5
        self.day = integer & 0b11111
        integer >>= 5
        self.month = integer & 0b1111
        integer >>= 4
        self.year = integer
    
    def sql_format(self):
        y = self.year
        mo = self.month
        d = self.day
        h = self.hour
        m = self.minute
        s = self.second
        return f"{y:04}-{mo:02}-{d:02} {h:02}:{m:02}:{s:02}"
    
    @staticmethod
    def int_to_sql(integer):
        s = integer & 0b111111
        integer >>= 6
        m = integer & 0b111111
        integer >>= 6
        h = integer & 0b11111
        integer >>= 5
        d = integer & 0b11111
        integer >>= 5
        mo = integer & 0b1111
        integer >>= 4
        y = integer
        return f"{y:04}-{mo:02}-{d:02} {h:02}:{m:02}:{s:02}"
    
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
        self.min_year = 2021
        self.max_year = 2023
        self.min_hour = 9
        self.max_hour = 22
        self.min_minute = 0
        self.max_minute = 59
        self.min_second = 0
        self.max_second = 59
        self.max_datetime = DateTime(2023,12,28,23,59,59)
        
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
        
    def generate_datetime_int(self):
        second = randint(self.min_second, self.max_second)
        minute = randint(self.min_minute, self.max_minute)
        hour = randint(self.min_hour, self.max_hour)
        day = randint(self.min_day, self.max_day)
        month = randint(self.min_month, self.max_month)
        year = randint(self.min_year, self.max_year)
        
        dt = 0
        dt |= second
        dt |= minute << 6
        dt |= hour << 12
        dt |= day << 17
        dt |= month << 22
        dt |= year << 26
        
        int_max = int(self.max_datetime)
        if dt > int_max:
            return int_max
        else:
            return dt
        
if __name__ == "__main__":
    dt_gen = DateTimeGenerator()
    dt_gen.min_year = 0
    
    for i in range(10000):
        print(DateTime.int_to_sql(dt_gen.generate_datetime_int()))
        print(DateTime.int_to_sql(int(dt_gen.generate_datetime())))