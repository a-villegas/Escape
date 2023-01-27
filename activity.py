from  Submodules.Restaurant.Restaurant import Restaurant
from hotels import hotel

hotels = hotel( hotel_name = 'Hilton', hotel_location = 'Los Angeles', total_days_stay = 7)
restaurant = Restaurant(restaurant_name = "Benihanas", cuisine_type = "Japanese")

if hotels:
    hotels.describe_hotel()
    
if restaurant:
    restaurant.describe_restaurant()

