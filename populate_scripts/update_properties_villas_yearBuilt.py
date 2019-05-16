import datetime
from random import Random, randint

def generateDate():
    return datetime.date(randint(1980,2005), randint(1,12),randint(1,28))

def main():
    f = open('update_properties_villas_yearBuilt.sql', 'w')
    for i in range(5):
        date = generateDate()
        f.write('UPDATE "property_properties"\n' \
            + "SET yearbuilt = " \
            + "'" + str(date) + "'\n" \
            + "WHERE description = 'villa' AND "+'"propertyId" = ' + str(i+6) + ";\n\n")
    f.close()

main()