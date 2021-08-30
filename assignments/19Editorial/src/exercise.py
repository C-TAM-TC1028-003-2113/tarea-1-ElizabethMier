import math
def main():
    # escribe tu código abajo de esta línea
    pal = int(input('Dame el número de palabras: '))
    if pal <= 475:
        costo1 = 60 - (60 * 0.10)
        print('El costo de la publicación es:', costo1)
    else:
        if pal > 475:
            num_pag = math.ceil(pal / 475)
        costo2 = (num_pag * 60)  - ((num_pag * 60) * 0.10)
        print('El costo de la publicación es:', costo2)

if __name__ == '__main__':
    main()
