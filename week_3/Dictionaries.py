my_laptop = {"make":"hp","color":"gray","wight":"9.5","year":"2023"}

print(my_laptop["make"])
print(my_laptop["color"])
print(my_laptop["year"])

for key,value in my_laptop .items():
    
    print(key)
    print("\n")
    print(value)

    print(my_laptop)

    my_laptop["size"] = "1200mm x 600mm"

    del my_laptop["color"]

    print(my_laptop)

    siz_laptop = my_laptop.copy


    car = {"make":"Audi","type":"Convertible","colour":"black",}

print(car)
for key , value in car.items:
    print(key)
print("/n")
print(value)

siz_car =car.copy()  
print(siz_car)
