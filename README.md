The file contents is about holiday cost which user will choose from, that would make a user spent less including car rental, travel cost, hotel cost and overall total cost for holiday.



# Ask user enter the city the will be flying to and flight cost

def hotel_cost(nights):
    pricePerNight = 170
    hotelCost = nights * pricePerNight
    return hotelCost

def plane_cost(city_flight):
    if city_flight == 'PTA':
        return 210
    
    elif city_flight == 'DBN':
        return 450
    
    elif city_flight == 'CPT':
        return 750

def car_rental(rental_days):
    car_cost_per_day = 90
    return rental_days * car_cost_per_day

def holidays_cost(nights, city_flight, rental_days ):
    hotel = hotel_cost(nights)
    print("The cost for staying in hotel", nights ,"nights is:",hotel) 

    plane = plane_cost(city_flight) 
    print("The plane cost for tickets", city_flight ,"is :", plane)

    car = car_rental(rental_days)
    print("The cost for your car rental for", rental_days ,"days is:",car)

    total = hotel + plane + car
    print("The total cost for your holiday is : R", total)

nights = int(input("Number of night staying in the hotel - "))

city = input("Choose a city from(PTA, DBN, CPT)-")

days = int(input("number of days for which car is hired -"))

holidays_cost(nights, city, days)
