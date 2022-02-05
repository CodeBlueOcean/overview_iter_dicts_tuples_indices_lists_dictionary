inches_snow = {"Monday": 2, "Tuesday": 4, "Wednesday": 5}

def print_total_snowfall(inches_snow):
    
    total_inches = 0
    for inches in inches_snow.values():
        total_inches += inches
    print("Total snowfall inches:", total_inches)

print_total_snowfall(inches_snow)

for x in list(inches_snow):
    inches_snow["Thursday"] = float(input("How many inches of snow fell on Thursday?"))
    print_total_snowfall(inches_snow)
    if x == "1":
        break
    else:
        print("A lot of Snow")
