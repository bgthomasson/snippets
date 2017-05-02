# iterate integers from 1 to 100:
# multiples of 3 print "fizz", of 5 print "buzz", of 15 "fizzbuzz"

def start():
    print('Enter an integer for the starting value:')
    start_val = int(input())
    return start_val

def end():
    print('Enter an integer for the ending value: ')
    end_val = int(input()) + 1
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


# Your first instinct is probably to follow instructions directly-
# 3, 5, both. However this can cause a bug where it outputs the results
# for 3 or 5 and not the "both" condition. At least in certain languages
# tested...

# Note that range() is 'exclusive' and does NOT include the max value:
# if z = 12, then 11 is the last number printed out!

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
            
