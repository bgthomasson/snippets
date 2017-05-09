#! python3

def start():
    start_val = int(input('Enter an integer for the starting value: '))
    return start_val

def end():
    end_val = int(input('Enter an integer for the ending value: ')) + 1
    return end_val

def fizzbuzz(starter, ender):
    for x in range(starter, ender):
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
            starter = start()
            ender = end()
            fizzbuzz(starter, ender)
            print("Want to keep going? Y to continue, any other key to quit:")
            rerun = input()
            
        except ValueError:
            print('Use the number keys!')
            # not fancy enough to have a save point so just reboot-
            rerun == "y"

main()
