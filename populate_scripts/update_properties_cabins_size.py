from random import Random, uniform

def main():
    f = open('update_properties_cabins.sql', 'w')
    for i in range(5):
        f.write('UPDATE "property_properties"\n' \
            + "SET price = " \
            + str(round((uniform(1, 3)), 2) * 100000) + '\n' \
            + "WHERE description = 'cabin' AND "+'"propertyId" = ' + str(i+11) + ";\n\n")
    f.close()

main()