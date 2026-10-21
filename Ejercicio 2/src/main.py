def calcular_medida(base: float, altura: float) -> tuple[float, float]:
    """
    Calcular el área y perímetro del cuadrilátero.
    
    :param: float base = Base del cuadrilátero.
    :param: float altura = Altura del cuadrilátero.

    :return: Una tupla con el área y el perímetro del cuadrilátero.
    """
    area: float = base * altura
    perimetro: float = 2 * (base + altura)

    return (area, perimetro)

def determinar_forma(base, altura) -> str:
    """
    Devolver que tipo de cuadrilátero es la figura del usuario.

    :param: float base = Base del cuadrilátero.
    :param: float altura = Altura del cuadrilátero.

    :reutrn: Una cadena de texto que diga el tipo de cuadrilátero.
    """

    if base > altura:
        return "Horizontal"
    elif altura > base:
        return "Vertical"
    else:
        return "Cuadrado"

def main():

    base: float = float(input("Escribe la base de tu cuadrilátero: "))
    altura: float = float(input("Escribe la altura de tu cuadrilátero: "))

    # Llamamos a las funciones.
    medidas_cuadrilatero: float = calcular_medida(base, altura)
    forma_cuadrilátero: str = determinar_forma(base, altura)

    if base <= 0 or altura <=0:
        print("Error. Alguna medida es incorrecta.")
    else:
        print(f"Forma: {forma_cuadrilátero}")
        print(f"Área: {medidas_cuadrilatero[0]} cm2")
        print(f"Perímetro: {medidas_cuadrilatero[1]} cm")

if __name__ == "__main__":
    main()


