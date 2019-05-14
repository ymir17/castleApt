import random
import datetime
from random import Random, randint

INSERT_VAL = 'INSERT INTO property_properties ("added", "address", "country", "zipCode", "rooms", "size", "price", "description", realtId)\n'

def fileToList(f):
    lst = []
    for i in f:
        lst.append(i.strip())
    return lst

def generateDate():
    return datetime.date(randint(2017,2019), randint(1,12),randint(1,28))

def populateCastle(f, addresses, zipCode):
    for i in range(20):
        date = generateDate()
        f.write(INSERT_VAL+'VALUES(' \
            + "'" + str(date) + "'" + ', ' \
            + "'" + str(addresses[i]) + "'" + ', ' \
            + "'Iceland'" + ',' \
            + "'" + str(zipCode[randint(0, len(zipCode))]) + "'" + ', ' \
            + str(randint(25, 35)) + ', ' \
            + str(round(random.uniform(3000, 8000), 2)) + ', ' \
            + str(round(random.uniform(500, 1000)*1000000, 2)) + ', ' \
            + "'castle', "\
            + str(16+i) \
            + ');\n')

def populateVilla(f, addresses, zipCode):
    for i in range(20):
        date = generateDate()
        f.write(INSERT_VAL+'VALUES(' \
            + "'" + str(date) + "'" + ', ' \
            + "'" + str(addresses[i+5]) + "'" + ', ' \
            + "'Iceland'" + ',' \
            + "'" + str(zipCode[randint(0, len(zipCode))]) + "'" + ', ' \
            + str(randint(5, 15)) + ', ' \
            + str(round(random.uniform(500, 1000), 2)) + ', ' \
            + str(round(random.uniform(10, 30)*1000000, 2)) + ', ' \
            + "'villa', "\
            + str(16+i) \
            + ');\n')

def populateCabin(f, addresses, zipCode):
    for i in range(11):
        date = generateDate()
        f.write(INSERT_VAL+'VALUES(' \
            + "'" + str(date) + "'" + ', ' \
            + "'" + str(addresses[i+10]) + "'" + ', ' \
            + "'Iceland'" + ', ' \
            + "'" + str(zipCode[randint(0, len(zipCode))]) + "'" + ', ' \
            + str(randint(1, 3)) + ', ' \
            + str(round(random.uniform(40, 80), 2)) + ', ' \
            + str(round(random.uniform(100, 500)*1000, 2)) + ', ' \
            + "'cabin', " \
            + str(16+i) \
            + ');\n')

def main():
    address_f = open('addresses.txt', 'r', encoding='utf-8')
    addresses = fileToList(address_f)
    address_f.close()

    zip_f = open('zip.txt', 'r', encoding='utf-8')
    zipCode = fileToList(zip_f)
    zip_f.close()

    f = open('properties.sql', 'w', encoding='utf-8')

    populateCastle(f, addresses, zipCode)
    populateVilla(f, addresses, zipCode)
    populateCabin(f, addresses, zipCode)

    f.close()
    
main()