# 3.11 Default Parameter Function

def display_info_value(entered_name, city_value="Ahmedabad", programme_value="M.Sc. IT"):
    print(f"Name: {entered_name:<10} | City: {city_value:<10} | Programme: {programme_value}")

print("(a) Calling with all 3 arguments:")
display_info_value("John Doe", "Mumbai", "M.Tech")

print("\n(b) Calling with only 'name':")
display_info_value("Alex")

print("\n(c) Calling with 'name' and 'city':")
display_info_value("Priya", "Surat")
