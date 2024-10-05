#inisiasi matriks ordo 3*3
a = [[1, 7, 2],
    [3, 4, 1],
    [5, 2, 1]]

#inisiasi matriks ordo 3*3
b = [[1, 2, 4],
    [3, 5, 2],
    [4, 3, 3]]

baris_a = len(a)
kolom_a = len(a[0])

baris_b = len(b)
kolom_b = len(b[0])

print(a)
print(f"Baris matriks a adalah: {baris_a} ")
print(f"Kolom matriks a adalah: {kolom_a} ")
print()
print(b)
print(f"Baris matriks b adalah:{baris_b}" )
print(f"Kolom matriks b adalah:{kolom_b}" ) 


if (kolom_a != baris_b):
    print("matriks a dengan b tidak dapat di kalikan")
else:
    print('''
Matriks a dengan b dapat di kalikan''')


