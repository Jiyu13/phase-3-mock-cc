
class Restaurant:

    all = []

    def __init__(self, name):
        self.name = name
        self.customers = []
        self.reviews = []
        # self.ratings = []
        Restaurant.all.append(self)
        
    
    def get_name(self):
        return self._name

    def set_name(self, name):
        # name property goes here!
        if not hasattr(self, "_name") and type(name) == str:
            self._name = name
        else:
            raise Exception(f"No restaurant called {name}")

    name = property(get_name, set_name)



    def get_average_rating(self):
        rating_count = len(self.reviews)
        amount = 0
        for each in self.reviews:
            amount += each.rating
        if rating_count > 0:
            average = amount / rating_count
            return average

    

    @classmethod
    def get_all_restaurants(cls):
        return cls.all