# *************************
# ECUACI�N DE SEGUNDO GRADO
# *************************


def run(a: int, b: int, c: int) -> tuple:
    # TU C�DIGO AQU�
    discriminante = b ** 2 - 4 * a * c

    if discriminante > 0:
        # Dos soluciones reales diferentes
        x1 = (-b + discriminante ** 0.5) / (2 * a)
        x2 = (-b - discriminante ** 0.5) / (2 * a)
    elif discriminante == 0:
        # Una solución real (raíz doble)
        x1 = x2 = -b / (2 * a)
    else:
        # Soluciones complejas
        real_part = -b / (2 * a)
        imaginary_part = (-discriminante) ** 0.5 / (2 * a)
        x1 = complex(real_part, imaginary_part)
        x2 = complex(real_part, -imaginary_part)

    return x1, x2

    return x1, x2


if __name__ == '__main__':
    run(4, -6, 2)