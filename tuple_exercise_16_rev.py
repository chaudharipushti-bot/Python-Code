st_value = ("Pen","Marker","Pencil","Eraser","Scale")

for word_value in st_value:

    rev_value = ""

    for ch_value in word_value:
        rev_value = ch_value + rev_value

    print(rev_value)