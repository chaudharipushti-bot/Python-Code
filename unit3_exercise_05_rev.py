# 3.5 Phone Book
phone_book_value = {}

# (a) Add 5 contacts
phone_book_value["Alice"] = "9876543210"
phone_book_value["Bob"] = "8765432109"
phone_book_value["Charlie"] = "7654321098"
phone_book_value["David"] = "6543210987"
phone_book_value["Eva"] = "5432109876"

# (b) Search by name
search_name_value = "Charlie"
print(f"Search '{search_name_value}': {phone_book_value.get(search_name_value, 'Not Found')}")

# (c) Update a number
phone_book_value["Alice"] = "9998887770"
print(f"Updated Alice's number: {phone_book_value['Alice']}")

# (d) Delete a contact
deleted_value = phone_book_value.pop("David", None)
print(f"Deleted contact 'David': {deleted_value}")

# (e) Display all contacts sorted by name
print("\nContacts sorted by name:")
for entered_name in sorted(phone_book_value.keys()):
    print(f"  {entered_name:<10} : {phone_book_value[entered_name]}")