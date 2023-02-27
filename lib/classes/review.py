from classes.customer import Customer
from classes.restaurant import Restaurant

class Review:
    
    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        self.add_customer_to_restaurant()
        self.add_review_to_restaurant()
        self.add_restaurant_to_customer()
        self.add_review_to_customer()


    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise Exception("Customer is not an instance of class Customer")
    
 
    @property
    def restaurant(self):
        # restaurant property goes here!
        return self._restaurant

    @restaurant.setter
    def restaurant(self, restaurant):
        if isinstance(restaurant, Restaurant):
            self._restaurant = restaurant
        else:
            raise Exception("Restaurant is not an instance of class Restaurant")

    @property
    def rating(self):
        # rating property goes here!
        return self._rating

    
    @rating.setter
    def rating(self, rating):
        if rating in [1, 2, 3, 4 ,5]:
            self._rating = rating
        else: 
            raise Exception("Your rating must be a number between 1 and 5, inclusive!")


    # connect to other class
    def add_customer_to_restaurant(self):
        if self._customer not in self._restaurant.customers:
            self._restaurant.customers.append(self._customer)

    def add_review_to_restaurant(self):
        self._restaurant.reviews.append(self)

    def add_restaurant_to_customer(self):
        if self._restaurant not in self._customer.restaurants:
            self._customer.restaurants.append(self._restaurant)

    def add_review_to_customer(self):
        # if self not in self._customer.reviews:
        self._customer.reviews.append(self)
