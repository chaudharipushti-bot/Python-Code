fruit_items = ("Apple","Banana","Mango","Orange","Grapes")

entered_name = input("Enter fruit: ")

if entered_name in fruit_items:
    print("Fruit Found")
else:
    print("Fruit Not Found")