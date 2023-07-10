
class Trip:
    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)
        
    def set_visitor(self, visitor):
        from classes.visitor import Visitor
        if isinstance(visitor, Visitor):
            self._visitor = visitor
    def get_visitor(self):
        return self._visitor
    
    visitor = property(get_visitor, set_visitor)
    
    def set_national_park(self, national_park):
        from classes.national_park import NationalPark
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
    def get_national_park(self):
        return self._national_park
    
    national_park = property(get_national_park, set_national_park)