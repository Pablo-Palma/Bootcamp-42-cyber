kata = (2019, 9, 25, 3, 30)
if all(x >= 0 for x in kata):
    año = str(kata[0]).zfill(4)
    mes = str(kata[1]).zfill(2)
    dia = str(kata[2]).zfill(2)
    hora = str(kata[3]).zfill(2)
    minuto = str(kata[4]).zfill(2)

    fecha = f"{mes}/{dia}/{año}"
    hora = f"{hora}:{minuto}"

    print(fecha, hora)
else:
    print("ERROR: todos los componentes deben ser positivos")
