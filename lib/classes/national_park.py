class NationalPark:

    def __init__(self, name):
        self.name = name
        # self._trips = []
        # self._visitors = []

    def set_name(self, name):
        if not hasattr(self, "name") and isinstance(name, str):
            self._name = name
        else:
            raise Exception
        
    def get_name(self):
        return self._name
    
    name = property(get_name, set_name)

    def trips(self):
        from classes.trip import Trip
        return [trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self):
        from classes.trip import Trip
        return list({trip.visitor for trip in Trip.all if trip.national_park == self})
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        visitors = self.visitors()
        num_trips = [0] * len(visitors)
        for trip in self.trips():
            num_trips[visitors.index(trip.visitor)] += 1
        return visitors[num_trips.index(max(num_trips))]