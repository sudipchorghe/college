# f = float(input("enter the frequency in hz "))
# if f <= 20000:
#     print ("audio frequency is (am)")
                           
# else:
#     print(" audio frequency is (rf)")


#code 2 
# f = float(input("enter frequency in hz :"))
# if 30000 <= f <= 300000:
#     print(" VLF band ")
# elif 300000 <= f <= 3000000:
#     print("LF band")
# elif 3000000 <= f <= 30000000:
#     print("HF band")
# elif 30000000 <= f <= 300000000:
#     print("VHF band")
# else:
#     print("frequency not in standard freauency range")
    
#code 3
# resistor value by color
# color = input("enter the color of band : ")

# if color == "black":
#     print("the value of band is = zero (0)")
# elif color == "brown":
#     print("the value of band is = one (1)")
# elif color == "red":
#     print("the value of band is = two (2)")
# elif color == "orange":
#     print("the value of band is = three (3)")
# elif color == "yellow":
#     print("the value of band is = four (4)")
# elif color == "green":
#     print("the value of band is = five (5)")
# elif color == "blue":
#     print("the value of band is = six (6)")
# elif color == "voilet":
#     print("the value of band is = seven (7)")
# elif color == "grey":
#     print("the value of band is = eight (8)")
# elif color == "white":
#     print("the value of band is = nine (9)")
# else:
#     print("enter a valid color")
#code 4 
# voltage = float(input("enter the voltage of battery")) 
# if 1 <= voltage <= 3.7:
# print("battery is charging") 
# elif 3.7 <= voltage <= 4.2: print("battery is charged") 
# else: print("over/under voltage, battery is damaged!!!")
    
#code 5

# #tolerence checker
# nominal_resistance = 100
# tolerence_percent = 5
# #measured resistance
# measured_resistance = 103

# tolerance = nominal_resistance* (tolerence_percent / 100)
# lower_limit = nominal_resistance - tolerance
# upper_limit = nominal_resistance + tolerance

# #check

# if lower_limit <= measured_resistance <= upper_limit:
#     print("the resister is within tolrence")
# else:
#     print("the resistor is outside tolernece range")