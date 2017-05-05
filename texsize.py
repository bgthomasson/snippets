'''
How many Texas-es?
Texas = 268,581 sq mi (696,241 km^2)
Have to test which is greater.
problems:
1. choice between km and miles is better with GUI

2. handling input integer with comma like 132,645
    input.split(",") then "".join() ??? too awkward.
    ah OK: input.strip(",")
3. normal division results in a float, even if use integer inputs, so format
    '{0:.1f}'.format(number)
    also, make the input a float for consistency, and avoid typecasting errors

'''

def handle_input(user_input):

    clean_input = user_input.strip(",")

    float_input = float(clean_input)

    return float_input


def comparator(float_input, texas):

    locus = float_input

    if locus > texas:
        result = locus / texas
        print('Your country can hold Texas {0:.1f} times!'.format(result))

    elif texas > locus:
        result = texas / locus
        print('Texas can hold {0:.1f} of your country!'.format(result))

    elif locus == texas:
        result = 1
        print('That is exactly the same size!')

    else:
        result = 0 # error code
        print('Gremlins!')

'''
it was at this point I don't need two FUNCTIONS, just two VARIABLES duh.
the hazards of referencing basic tutorials.
I need to clarify my logic.
FIRST,measure = input() determines value of var texas
SECOND, size = input() gets sanitized and fed into comparator()

'''

def main():

    rerun = "y"
    while rerun == "y":
        print('Is it bigger than Texas!?')
        print('Enter 1 to use square kilometers.')
        print('Enter 2 to use square miles.')

        try:
            choice = int(input())
            if choice == 2:
                texas = 268581
            else:
                texas = 696241

            # now get a number

            print('Now enter the size in numbers [like 14325]: ')
            user_input = input()

            float_input = handle_input(user_input)
            
            comparator(float_input, texas)

            print("Enter y to test another, or any other key to quit:")
            rerun = input()
        
        # error handle non-numbers
        
        except ValueError:
            print('Use the number keys!')
            # not fancy enough to have a save point so just reboot-
            rerun == "y"


# run it

main()


# oh this only took an hour or two, and like 6 minor proofreading errors. 
    

