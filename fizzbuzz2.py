#! python3
# this has no need to be interactive except to grab attention
# I have no current reason to do these as functions except 80 col limit

def starter():
    start_val = int(input('Enter an integer for the starting value: '))
    return start_val

def ender():
    end_val = int(input('Enter an integer for the ending value: ')) + 1
    return end_val

# range is exclusive, so adding 1 to the end value is a bodge to dodge this

def fizzbuzz(start_val, end_val):
    for x in range(start_val, end_val):
        if x % 3 == 0 and x % 5 == 0:
            print('FIZZBUZZ!')
        elif x % 3 == 0:
            print('fizz')
        elif x % 5 == 0:
            print('buzz')
        else:
            print(x)


def main():
    rerun = "y"
    while rerun == "y" or rerun == "Y":
        print("FIZZBUZZ 2")

        try: 
            start_val = starter()
            end_val = ender()
            fizzbuzz(start_val, end_val)
            print("Want to keep going? Y to continue, any other key to quit:")
            rerun = input()
            
        except ValueError:
            print('Use the number keys!')
            # not fancy enough to have a save point so just reboot-
            rerun == "y"

main()
