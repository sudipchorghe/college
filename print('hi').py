colorband = {
    "black" : 0,
    "brown" : 1,
    "red" : 2,
    "orange" : 3,       
    "yellow" : 4,
    "green" : 5,
    "blue" : 6,
    "violet" : 7,
    "grey" : 8,
    "white" : 9

}
multiplier = {
    "black" : 1,
    "brown" : 10,
    "red" : 100,
    "orange" : 1000,       
    "yellow" : 10000,
    "green" : 100000,
    "blue" : 1000000,
    "violet" : 10000000,
    "grey" : 100000000,
    "white" : 1000000000,
    "gold" : 0.1,
    "silver" : 0.01

}
tolerance = {
    "brown" : "±1%",
    "red" : "±2%",
    "gold" : "±5%",
    "silver" : "±10%"
}
def res_val(band1,band2,band3,band4):
    val = (colorband[band1]*10 + colorband[band2]) * multiplier[band3]
    tol = tolerance.get(band4)
    
    print ("resistance calc")
    return val, tol

    
b1 = input("Band 1 color: ").lower()
b2 = input("Band 2 color: ").lower()
b3 = input("Multiplier band color: ").lower()
b4 = input("Tolerance band color: ").lower()

value, tol = res_val(b1, b2, b3, b4)
print(f"The resistor value is {value} Ohms with a tolerance of {tol}.")
