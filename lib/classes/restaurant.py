import statistics

class Restaurant:
    all = []

    def __init__(self, name):
        # be initialized with a name, as a string
        # Returns the restaurant's name
        # Should not be able to change after the restaurant is created
        # !!!! NO SETTER !!!
        if type(name) == str:
            self._name = name
            # every time make a new restaurant obj, add it to all=[]
            Restaurant.all.append(self)
        else:
            raise Exception
        
        self.reviews = []
        self.customers = []

    '''
    @property
    def name(self):
        return self._name
    '''
    
    def get_name(self):
        return self._name
    
    name = property(get_name)

    def get_average_rating(self):
        total = 0

        for review in self.reviews:
            total += review.rating

        average = total / len(self.reviews)

        return average
    
        # return sum([review.rating for review in self.reviews]) / len(self.reviews)
    

    @classmethod
    def get_all_restaurants(cls):
        return cls.all