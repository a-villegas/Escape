
class hotels():
    """An obscure example of a hotel"""
    
    def __init__(self, hotel_name, hotel_location='Los Angeles', total_days_stay=0, **kwargs):
        self.hotel_name = hotel_name
        self.hotel_location = hotel_location
        self.total_days_stay = total_days_stay
        
    
    def describe_hotel(self):
        """Hotel Description"""
        print(self.name.title() + "is located in " + self.hotel_location.title())
        
    
    def number_of_days_ocupancy(self):
        if(self.total_days_stay > 0):
            return self.total_days_stay
        return 0 
    
        