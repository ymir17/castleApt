from random import Random, uniform, randint

def main():
    f = open('update_properties_castles_rooms.sql', 'w')
    for i in range(5):
        f.write('UPDATE "property_properties"\n' \
            + "SET rooms = " \
            + str(randint(60, 150)) + '\n' \
            + "WHERE description = 'castle' AND "+'"propertyId" = ' + str(i+1) + ";\n\n")

main()