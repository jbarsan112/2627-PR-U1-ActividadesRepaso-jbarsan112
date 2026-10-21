def preparar_texto(frase: str) -> str:
    """
    Eliminamos los espacios de los extremos y convierte el texto a minusculas.

    :param: str frase = Frase escrita por el usuario.

    :return: Devolver la frase en minuscula.
    """

    frase_sinespacios: str = frase.strip(" ")
    frase_minuscula: str = frase_sinespacios.lower()

    return frase_minuscula

def analizar_texto(frase: str) -> tuple[int, int, bool]:
    """
    Recibir el texto preparado y devolver una tupla con 3 datos.

    :param: str frase = Frase del usuario

    :return: Una tupla con la cantidad de caracteres, cantidad de palabras y si la palabra "python" está en la frase.
    """

    texto_preparado: str = preparar_texto(frase)
    num_caracteres: int = len(texto_preparado)
    num_palabras: int = len(texto_preparado.split())

    
    existe_python: bool = "python" in texto_preparado
   
    
    return (num_caracteres, num_palabras, existe_python)

def main():

    frase: str = input("Escribe una frase: ")

    texto_preparado = preparar_texto(frase)
    texto_analizado = analizar_texto(frase)

    if texto_preparado == "":
        print("Error: No has escrito nada.")
    else:
        print(f"Texto: {texto_preparado}")
        print(f"Caracteres: {texto_analizado[0]}")
        print(f"Palabras: {texto_analizado[1]}")
        print(f"¿Contiene python?: {texto_analizado[2]}")

if __name__ == "__main__":
    main()