from random import Random, uniform

def main():
    f = open('update_properties.sql', 'w')
    for i in range(5):
        f.write('UPDATE "property_properties"\n' \
            + "SET price = " \
            + str(round((uniform(1, 50)), 2) * 1000000) + '\n' \
            + "WHERE description = 'castle' AND "+'"propertyId" = ' + str(i+1) + ";\n")

main()