class Customer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.reviews = []
        self.restaurants = []
        

    # first_name property goes here!
    def get_first_name(self):
        return self._first_name

    def set_first_name(self, firstName):
        if not hasattr(self, "_first_name") and type(firstName) == str:
            self._first_name = firstName
        else:
            raise Exception
    
    first_name = property(get_first_name, set_first_name)

   
   # last_name property goes here!
    def get_last_name(self):
        return self._last_name

    def set_last_name(self, lastName):
        if type(lastName) == str and 1 <= len(lastName) <= 25:
            self._last_name = lastName
        else:
            return None


    last_name = property(get_last_name, set_last_name)


    def get_full_name(self):
        return self._first_name + " " + self._last_name

    def get_num_reviews(self):
        return len(self.reviews)

    def add_review(self, restaurant, rating):
        # This prevents a circular import!
        # Don't worry about it right now, but check it out when you have the time!
        from classes.review import Review
        Review(self, restaurant, rating)