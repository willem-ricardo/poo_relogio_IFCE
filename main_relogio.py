import hora

h1 = hora.Hora(12,15,30)
h2 = hora.Hora(7, 16, 33)


for i in range(100):
    print(h1, h1.str_12)
    h1.mais_um_segundo()
