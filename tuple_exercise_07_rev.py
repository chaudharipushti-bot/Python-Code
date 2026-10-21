cities_value = ()

temp_value = []

for i_value in range(5):
    city_value = input("Enter city: ")
    temp_value.append(city_value)

cities_value = tuple(temp_value)

print(cities_value)