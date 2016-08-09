# TEMPERATURE CONVERTER
# 2014.01.08, 2016.08.04
# To do: 
# Continue/quit option.
# Defaults to F as input, should it be a choice between F, C, K?
# Bonus: commentary, e.g. "Hot enough to melt lead!" "What a lovely day!"

# Why round()? well obviously, otherwise you get like 100.11111111, and 
# I thought 2 decimal places is precise enough for laymen and nerds

def f_to_k(degrees_f):
    degrees_k = 273.15 + (degrees_f - 32) * 5 / 9
    degrees_k = round (degrees_k, 2) 
    return degrees_k

def f_to_c(degrees_f):
    degrees_c = (degrees_f - 32) * 5 / 9
    degrees_c = round (degrees_c, 2) 
    return degrees_c

def c_to_f(degrees_c):
    degrees_f = (degrees_c * 9 / 5) + 32
    degrees_f = round (degrees_f, 2)
    return degrees_f

def c_to_k(degrees_c):
    degrees_k = degrees_c + 273.15
    # I'll leave off the rounding here because it seems superfluous
    return degrees_k

def k_to_c(degrees_k):
    degrees_c = degrees_k - 273.15
    # Again no rounding for this since it's simple subtraction
    return degrees_c

def k_to_f(degrees_k):
    degrees_f = 32 + (degrees_k - 273.15) * 9 / 5
    degrees_f = round (degrees_f, 2)
    return degrees_f

def main():
    rerun = "y"
    while rerun == "y" or rerun == "Y":
        print("Enter degrees Fahrenheit to convert to Kelvin and Celsius:")
        degrees_f = float(input())
        degrees_k = str(f_to_k(degrees_f))
        degrees_c = str(f_to_c(degrees_f))
        print("That is " + degrees_k + " Kelvin and "
              + degrees_c + " Celsius.")
        print("Enter Y to convert another temperature, or N to quit.")
        # I'm a dirty liar, any other letter OR number will work!
        # Maybe even something crazy like ~
        rerun = input()

main()

