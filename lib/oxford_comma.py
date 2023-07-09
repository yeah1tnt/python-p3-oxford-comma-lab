import ipdb

def oxford_comma(items):
    result = ""
    if len(items) == 1:
        result = items[0]
    elif len(items) == 2:
        result = items[0] + " and " + items[1]
    else:
        result = ", ".join(items[:-1]) + ", and " + items[-1]
    
    return result