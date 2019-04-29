
angkaInput = input('Masukan angka : ')

mylist = []

def angkaBilangan():
    if len(angkaInput.split('.')) > 1:
        print('Input bilangan bulat!')
    else:
        if angkaInput.replace('-','').isdigit() == False:
            print('Masukkan bilangan yang benar!')
        else:
            angka = int(angkaInput)
            mylist.append('Bulat')
            
            if angka < 0:
                mylist.append('Negatif')
            else:
                mylist.append('Cacah')

                if angka == 0:
                    mylist.append('Nol')
                else:
                    mylist.append('Asli')

                    if angka % 2 == 0:
                        mylist.append('Genap')
                    elif angka % 2 != 0:
                        mylist.append('Ganjil')

                    if angka > 1:

                        for i in range(2, angka):
                            if (angka % i) == 0:
                                mylist.append('Composite')
                                break
                        else:
                            mylist.append('Prima')

                    else:
                        mylist.append('Composite')

    
    print(mylist)

angkaBilangan()