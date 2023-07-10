class Visitor:

    def __init__(self, name):
        self.name = name
        # self._trips = []
        # self._national_parks = []
        
    def set_name(self, name):
        if not hasattr(self, "name") and isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise Exception
    
    def get_name(self):
        return self._name
    
    name = property(get_name, set_name)

    def trips(self):
        from classes.trip import Trip
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        from classes.trip import Trip
        return list({trip.national_park for trip in Trip.all if trip.visitor == self})
    