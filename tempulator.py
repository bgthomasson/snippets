# TEMPERATURE CONVERTER
# 2014.01.08, 2016.08.04
# need: branching input. continue/quit option. 
# bonus: commentary, e.g. "hot enough to melt lead!" "what a lovely day!"

def f2k(degrees_f):
    degrees_k = 273.15 + (degrees_f - 32) * 5 / 9
    degrees_k = round (degrees_k, 2) 
    return degrees_k

def f2c(degrees_f):
    degrees_c = (degrees_f - 32) * 5 / 9
    degrees_c = round (degrees_c, 2) 
    return degrees_c

# I wish I could combine these, so it factors C, then just add 273.15 for K.

def c2f(degrees_c):
    degrees_f = (degrees_c * 9 / 5) + 32
    degrees_f = round (degrees_f, 2)
    return degrees_f


def main(): 
    print("Enter degrees Fahrenheit to convert to Kelvin and Celsius:")
    degrees_f = float(input())
    degrees_k = str(f2k(degrees_f))
    degrees_c = str(f2c(degrees_f))
    print("That is " + degrees_k + " Kelvin and " + degrees_c + " Celsius.")

main()

