# This is the beginning of the program.

import time
import os
import ping,socket

def logic():
    print('Loading txt file now.')
    time.sleep(1)
    contents = []
    with open ('ip.txt', 'r') as txtfile:
        for myline in txtfile:
            contents.append(myline)
        for element in contents:
            print(element)
    time.sleep(2)
    print('Data loaded.')
    number = contents.count() + 1
    print('number of IP adresses detected:', number)
    time.sleep(1)
    testvalue = 0
    while testvalue != number:
        listelement = 0
        traceip = str(contents[listelement])
        print(traceip)
        try:



        # While loop logic:
        listelement += 1
        testvalue += 1



def main():
    print('MAKE SURE THIS PROGRAM HAS BEEN RUN UNDER ADMINISTRATOR PRIVILEGES!')
    time.sleep(3)
    print('Welcome to Tracer, have a .txt file ready in the destination of this program.')
    time.sleep(2)
    print('This program will collect IPV4 addresses, trace to their destination, and save that data')
    print('to a file.')
    time.sleep(2)
    print('Instructions:')
    time.sleep(2)
    print('1. Have your txt file ready in the destination the program is running in.')
    print('(Have only this file in the destination path. HAVE THIS FILE NAMED "ip.txt")')
    time.sleep(1)
    print('(This file should contain IPV4 addresses separated by a new line.)')
    time.sleep(2)
    print('2. When complete, copy or remove both your original file and the destination file.')
    time.sleep(2)
    def readycode():
        ready = input('Ready? (Yes or No)')
        if ready == 'Yes' or ready == 'yes':
            logic()
        elif ready == 'No' or ready == 'no':
            print('You have chosen to quit the program, goodbye.')
            quit()
        else:
            print('Incorrect input, please try again')
            readycode()

    readycode()
main()
