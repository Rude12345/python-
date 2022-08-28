class Date:

    def __init__(self, day: int = 0, month: int = 0, year: int = 0) -> None:
        """ The Date class, which should: check date numbers for correctness;
        convert a date string to a Date object consisting of the corresponding numeric day, month, and year values.
        Both methods must receive a string like dd-mm-yyyy as input. """
        self.day = day
        self.month = month
        self.year = year

    def __str__(self) -> str:
        return 'Day: {}\tMonth: {}\tYear: {}'.format(
            self.day, self.month, self.year)\

    @classmethod
    def is_date_valid(cls, date: str) -> bool:
        dmy_list = date.split('-')
        day, month, year = int(dmy_list[0]), int(dmy_list[1]), int(dmy_list[2])
        return 0 < day <= 31 and 0 < month <= 12 and 0 < year <= 9999\

    @classmethod
    def from_string(cls, date: str) -> 'Date':
        dmy_list = date.split('-')
        day, month, year = int(dmy_list[0]), int(dmy_list[1]), int(dmy_list[2])
        date_obj = cls(date, month, year)
        return date_obj


my_date = Date.from_string('10-12-2077')
print(my_date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
