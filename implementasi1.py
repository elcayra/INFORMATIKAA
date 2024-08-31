#Penulisan String
print("Hello Elyca")
print('''Ayo belajar python dari nol''')

#Penulisan blok program
if 5 > 2:
    print("five is greater than two!")

#Penulisan case
my_variable_name ="Elyca " #snake case
MyVariableName = "Rahmadhani" #pascal case

print (my_variable_name + MyVariableName)


#variable 1
x = 9
y = "Gasiwa"

print(x)
print(y)

#variable 2
N = "Elyca"
T = "GAMADA"
U = 2025
print(N, T, U)

#variable umur
umur = input("masukan umur: ")
if int(umur) < 18:
    keterangan = 'masih muda'
else:
    keterangan = 'sudah tua'

print('Elyca memasukan umur {}, artinya Elyca {}'.format(umur, keterangan))


#komentar
#Bisa menggunakan pagar
'''Bisa menggunakan petik'''
"""
This is a comment
written in
more than just one line
"""