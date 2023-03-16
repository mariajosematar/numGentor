from phonenumbers import geocoder
from colorama import Fore, init
from random import randint
import phonenumbers as pn 
import argparse
import time
import csv
import os
init(autoreset=True)

parser = argparse.ArgumentParser(description='Phone Number Generating')
parser.add_argument('-a', '--amount', help='Set a certain amount of phone numbers to generate', default=None)
parser.add_argument('-b', '--reference', help='Does 5, 10 second references of NumGen.py to see how many valid phone numbers you generate every 10 seconds.', default=False, action='store_true')
args = parser.parse_args()
numberAmount = args.amount
reference = args.reference

def setFileName():
    fileNum = 1
    fileName = f"{cwd}\\Phone Numbers {fileNum}.csv"
    while os.path.isfile(fileName):
        fileNum += 1
        fileName = f"{cwd}\\Phone Numbers {fileNum}.csv"

    return fileName


def findNumbers():
    fileName = setFileName()
    
    if numberAmount != None:
        print(f"{Fore.CYAN}Chosen Amount: {Fore.WHITE}{numberAmount}")
    print()

    header = ['Number:', 'Location:']
    with open(fileName, 'a', newline='') as startFile:
        writer = csv.writer(startFile)
        writer.writerow(header)

        startFile.close()

    print(f"{Fore.YELLOW}Generating Phone Numbers...")

    amount = 0
    while str(amount) != str(numberAmount):
        phoneNumber = randint(1000000000, 9999999999)

        countryCode = "+1"
        phoneNumber = str(countryCode) + str(phoneNumber)

        phone = pn.parse(phoneNumber)
        validNum = pn.is_valid_number(phone)
        numberLocation = geocoder.description_for_number(phone, 'en')

        if validNum == True:
            if numberLocation == "":
                pass
            else: 
                phoneNumber = phoneNumber[2:]

                num = -1
                phoneNumberFormat = "+1 ("
                for i in phoneNumber:
                    num += 1 
                    if num == 2:
                        phoneNumberFormat += phoneNumber[num]
                        phoneNumberFormat += ") "
                    elif num == 5:
                        phoneNumberFormat += phoneNumber[num]
                        phoneNumberFormat += "-"
                    else:
                        phoneNumberFormat += phoneNumber[num]

                data = [phoneNumberFormat, numberLocation]
                with open(fileName, 'a', newline='', encoding="utf-8") as file:
                    csv.field_size_limit(1000) 
                    writer = csv.writer(file)
                    writer.writerow(data)

                    amount += 1

                    file.close()
        else:
            pass

    print()
    print(f"{Fore.GREEN}Generated {numberAmount} Phone Numbers!")
    print()
    input("Press ENTER to Exit...")
    exit()


def referenceNumbers():
    global validCount

    start = time.time()

    validCount = 0
    while True:
        phoneNumber = randint(1000000000, 9999999999)

        countryCode = "+1"
        phoneNumber = str(countryCode) + str(phoneNumber)

        phone = pn.parse(phoneNumber)
        validNum = pn.is_valid_number(phone)

        numberLocation = geocoder.description_for_number(phone, 'en')
        if numberLocation == "":
            pass
        else:
            if validNum == True:
                validCount += 1

                end = time.time()

                currentTime = end - start
                currentTime = int(currentTime)

                if currentTime == 10:
                    listAdd()


def listAdd():
    global runThrough
    runThrough += 1

    vcl.append(validCount)

    print(f"{Fore.WHITE}Reference {Fore.CYAN}{runThrough}/5 {Fore.WHITE}Complete.")

    if runThrough == 5:
        time.sleep(1)
        print()
        
        average = int(sum(vcl) / len(vcl))
        average = int(average)

        print(f"{Fore.WHITE}Average Numbers Generated Every 10 Seconds: {Fore.CYAN}{average}")
        print()
        input("Press ENTER to Exit...")
        exit()
    else:
        time.sleep(1)
        referenceNumbers()


cwd = os.getcwd()
validCount = 0
runThrough = 0
vcl = []


if numberAmount == None and reference == False:
    print("Please enter amount of numbers to generate.")
    exit()

if numberAmount != None and reference == True:
    print(f"{Fore.RED}!~ ERROR ~!")
    print(f"Amount of numbers to generate: {numberAmount}")
    print()
    print("But you also want to reference.")
    print()

    choice = ""
    while choice != "b" and choice != "g":
        choice = input("Would you like to reference or generate numbers? (b/g): ")

        if choice != "b" and choice != "g":
            print("ERROR!: Please enter either g (For Generating Numbers) or b (For Referenceking)")

    if choice == "g":
        reference = False
    else:
        reference = True


if str(reference) == 'True':
    print(f"{Fore.YELLOW}Referenceking...")
    print()

    referenceNumbers()
else:
    findNumbers()