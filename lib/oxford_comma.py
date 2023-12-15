def oxford_comma(items):
    if len(items) == 1:
        return "".join(items)
    if len(items) == 2:
        return items[0] + " and " + items[1]
    if len(items) == 3:
        return items[0] + ", " + items[1] + ", and " + items[2]
    if len(items) > 3:



# if index -2 add and instead of ,