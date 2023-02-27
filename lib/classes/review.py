from classes.customer import Customer
from classes.restaurant import Restaurant

class Review:
    
    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        self.add_review_to_customer()
        self.add_review_to_restaurant()
        
        self.add_restaurant_to_customer()
        self.add_customer_to_restaurant()
        # self.add_rating_to_restaurant()


     # customer property goes here!
    def get_customer(self):
        return self._customer
    
    def set_customer(self, customerName):
        self._customer = customerName

    customer = property(get_customer, set_customer)
 
    
    # restaurant property goes here!
    def get_restaurant(self):
        return self._restaurant
    
    def set_restaurant(self, restaurantName):
        self._restaurant = restaurantName
    
    restaurant = property(get_restaurant, set_restaurant)


    # rating property goes here!
    def get_rating(self):
        return self._rating
    
    def set_rating(self, ratingScore):
        if not hasattr(self, "_rating") and type(ratingScore) == int:
            if ratingScore in [1, 2, 3, 4, 5]:
                self._rating = ratingScore
        else:
            raise Exception

    rating = property(get_rating, set_rating)



    def add_customer_to_restaurant(self):
        self.restaurant.customers.append(self.customer)
        

    def add_review_to_restaurant(self):
        self.restaurant.reviews.append(self)

    def add_restaurant_to_customer(self):
        self.customer.restaurants.append(self.restaurant)

    def add_review_to_customer(self):
        self.customer.reviews.append(self)


    # add rating 
    # def add_rating_to_restaurant(self):
    #     self.restaurant.ratings.append(self.rating)