# Basic - Print all integers from 0 to 150.
def printRange():
    for x in range(1,151):
        print(x)

printRange()
print('\n')

# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
def multiplesOfFive():
    for x in range(5,1000):
        if x % 5 == 0:
            print(x)

multiplesOfFive()
print('\n')
# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
def counting():
    for i in range(1,101):
        if i % 5 == 0 and i % 10 != 0:
            print("Coding")
        elif i % 10 == 0:
            print("Coding Dojo")
        else:
            print(i)

counting()
print('\n')

# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
def oddInt():
    sum = 0
    for x in range(0,500000):
        if x % 2 != 0:
            print(x)
        sum += x
    print(sum)

oddInt()
print('\n')
# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
def countDown():
    start = 2018
    while start > 0:
        if start % 2 == 0:
            print(start)
        start -= 4

countDown()
print('\n')
# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
def flexCount(lowNum, highNum, mult):
    for x in range(highNum, lowNum, -mult):
        print(x)

flexCount(2,9,3)