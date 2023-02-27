class Restaurant:
    all = []

    def __init__(self, name):
        if type(name) == str:
            self._name = name
            Restaurant.all.append(self)
        else :
            raise Exception("Restaurant name must be a string")
        
        self.reviews = []
        self.customers = []

    @property
    def name(self):
        # name property goes here!
        return self._name
    

    # def name(self, name):
    #     if not hasattr(self, "_name") and type(name) == str:
    #         self._name = name
    #     else:
    #         raise Exception("Your last name must be a string and contain between 1 and letters inclusive!")


    def get_average_rating(self):
        ratings = 0
        for review in self.reviews:
            ratings += review.rating
        if len(self.reviews) > 0:
            average = ratings / len(self.reviews)
            return average

    @classmethod
    def get_all_restaurants(cls):
        return cls.all