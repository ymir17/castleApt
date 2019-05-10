from random import Random, uniform, randint, shuffle

def fileToList(f):
    lst = []
    for line in f:
        lst.append(line.strip())
    shuffle(lst)
    return lst

def main():
    z = open('zip.txt', 'r')
    zLst = fileToList(z)
    f = open('update_properties_zipCode.sql', 'w')
    for i in range(15):
        zipCode = zLst[i]
        f.write('UPDATE "property_properties"\n' \
            + 'SET "zipCode" = ' + "'"+zipCode+"'" + '\n' \
            + 'WHERE "propertyId" = ' + str(i+1) + ';\n\n')
    
    f.close()
    z.close()

main()