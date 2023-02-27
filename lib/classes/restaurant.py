import statistics

class Restaurant:
    all = []

    def __init__(self, name):
        if type(name) == str:
            self._name = name

            Restaurant.all.append(self)
        else:
            print("The restaurant name must be a string!")

            raise Exception("The restaurant name must be a string!")
        
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