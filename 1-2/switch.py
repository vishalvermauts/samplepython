
Country=input('Country(INDIA / CHINA / PAKISTAN / RUSSIA / QATAR): ').upper()

match Country:
    case 'INDIA': print("IN")
    case 'CHINA' : print("CN")
    case 'PAKISTAN' : print('PK')
    case 'RUSSIA': print('RU')
    case 'QATAR': print('QR')
    case _: print("Invalid")

