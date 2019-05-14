# id,propImgUrl, porpertyId_id

LINE = 'INSERT INTO property_propimages ("propImgUrl", propertyId_id)\nVALUES ('
PATH = 'static/'

def populateCastle(f):
    for i in range(5):
        for j in range(4):
            f.write(LINE \
                + "'" + PATH + 'castles/0' + str(i) + '_0' + str(j) + '.jpeg' + "', " \
                + str(i+1) + ');\n')

def populateVilla(f):
    for i in range(5):
        for j in range(4):
            f.write(LINE \
                + "'" + PATH + 'villas/0' + str(i) + '_0' + str(j) + '.jpeg' + "', " \
                + str(i+6) + ');\n')

def populateCabin(f):
    for i in range(5):
        for j in range(2):
            f.write(LINE \
                + "'" + PATH + 'cabins/0' + str(i) + '_0' + str(j) + '.jpeg' + "', " \
                + str(i+11) + ');\n')

def main():
    f = open('propertiesImg.sql', 'w')
    
    populateCastle(f)
    populateVilla(f)
    populateCabin(f)
    
    f.close()

main()