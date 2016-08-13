# FIZZBUZZ 2! electric function making hullabaloo!
# iterate integers from 1 to 100:
# multiples of 3 print "fizz", of 5 print "buzz", of 15 "fizzbuzz"
# 2014.01.08, 2016.08.04 
# If this seems riduculous I could have made it so the user picked integers
# other than 3 and 5 for the fizziest buzziest useless script.
# Although, if you could make some sort of graphical output... hmm...

# These are terribly generic function names instead of like..
# "bottle_opener" or "buzz_off" 

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

# OK so the point of this is to show the simplest of competencies so...
# Your first instinct is probably to follow instructions directly-
# 3, 5, both. However this can cause a bug where it outputs the results
# for 3 or 5 and not the "both" condition. At least in certain languages
# tested it in, so better safe than sorry.
# Otherwise it's a simple if/else loop. 


# Note that range() is 'exclusive' and does NOT include the max value:
# if z = 12, then 11 is the last number printed out!
# We can try getting around this by simply adding 1!
# If you wish to double check simply have the printout read:
# print(x + 'foo')

def main():
    rerun = "y"
    while rerun == "y" or rerun == "Y":
        print("FIZZBUZZ 2")
        starter = start()
        ender = end()
        fizzbuzz(starter, ender)
        print("Want to keep going? Y to continue, any other key to quit:")
        rerun = input()

main()
            
