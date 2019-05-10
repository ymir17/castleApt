from random import Random, uniform

def main():
    f = open('update_properties_villas.sql', 'w')
    for i in range(5):
        f.write('UPDATE "property_properties"\n' \
            + "SET price = " \
            + str(round((uniform(1, 5)), 2) * 1000000) + '\n' \
            + "WHERE description = 'villa' AND "+'"propertyId" = ' + str(i+6) + ";\n\n")

main()