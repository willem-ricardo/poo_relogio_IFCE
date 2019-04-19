import hora

h1 = hora.Hora(12,15,30)
h2 = hora.Hora(7, 16, 33)

print(h1)
print(h2)
print(50*'-')
h1.mais_um_segundo()
h2.mais_um_segundo()
print(h1)
print(h2)