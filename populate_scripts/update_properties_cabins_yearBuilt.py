import datetime
from random import Random, randint

def generateDate():
    return datetime.date(randint(1975,1995), randint(1,12),randint(1,28))

def main():
    f = open('update_properties_cabins_yearBuilt.sql', 'w')
    for i in range(5):
        date = generateDate()
        f.write('UPDATE "property_properties"\n' \
            + "SET yearbuilt = " \
            + "'" + str(date) + "'\n" \
            + "WHERE description = 'cabin' AND "+'"propertyId" = ' + str(i+11) + ";\n\n")
    f.close()

main()