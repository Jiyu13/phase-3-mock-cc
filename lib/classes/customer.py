class Customer:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.reviews = []
        self.restaurants = []

    @property
    def first_name(self):
        # first_name property goes here!
        return self._first_name
    
    @first_name.setter
    def first_name(self, first_name):
        if type(first_name) == str and 1 <= len(first_name) <= 25:
            self._first_name = first_name
        else:
            raise Exception("Your first name must be a string and contain between 1 and letters inclusive!")

    @property
    def last_name(self):
        # last_name property goes here!
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name):
        if type(last_name) == str and 1 <= len(last_name) <= 25:
            self._last_name = last_name
        else:
            raise Exception("Your last name must be a string and contain between 1 and letters inclusive!")

    
    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_num_reviews(self):
        return len(self.reviews)

    def add_review(self, restaurant, rating):
        # This prevents a circular import!
        # Don't worry about it right now, but check it out when you have the time!
        from classes.review import Review
        Review(self, restaurant, rating)