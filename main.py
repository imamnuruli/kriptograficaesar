import caesarCP

input = "Av To"
hasil = caesarCP.enkripsi(input)
print("Ini input data     : ", input)
print("Ini hasil Enkripsi : ", hasil)
res = caesarCP.dekripsi(hasil)
print("Ini hasil Dekripsi : ", res)
