import names
import random
import xlsxwriter

def gen_numbers():
    allowed_numbers = '0123456789'
    indx = '(+39)331'
    for i in range(7):
        indx += allowed_numbers[random.randint(0, len(allowed_numbers) - 1)]
    return indx
##Creazione file excel
workbook = xlsxwriter.Workbook("Anagrafiche.xlsx")
worksheet = workbook.add_worksheet("Anagrafica")

#Creo testata
worksheet.write(0, 0, "Progressivo")
worksheet.write(0, 1, "Nome")
worksheet.write(0, 2, "Cognome")
worksheet.write(0, 3, "Email")
worksheet.write(0, 4, "Numero_telefonico")

i = 0
print("Stampa anagrafiche complete")
while(i<10):
    name = names.get_first_name()
    surname = names.get_last_name()
    print(name)
    print(surname)
    print (name+ "."+ surname+"@gmail.com")
    print(gen_numbers())
    worksheet.write(i+1, 0, str(i))
    worksheet.write(i+1, 1, name)
    worksheet.write(i+1, 2, surname)
    worksheet.write(i+1, 3, str(name+ "."+ surname+"@gmail.com"))
    worksheet.write(i+1, 4, str(gen_numbers()))
    i += 1

#chiudo il file
workbook.close()
