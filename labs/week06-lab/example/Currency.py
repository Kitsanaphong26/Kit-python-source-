def convert_currency(value, currency)
    result = 0
    if currency =="USA"
       result = value / 33.0
       print (f"{value} THB = {result} USA")
    else:
        result = value / 33.0
        print (f"{value} USA = {result} THB")
convert_currency(100, "USA")
convert_currency(100, "THB")