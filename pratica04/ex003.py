# Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de pontos no sistema cartesiano. Para cada ponto escrever o quadrante a que ele pertence. O algoritmo será encerrado quando pelo menos uma de duas coordenadas for NULA (nesta situação sem escrever mensagem alguma).

# Entrada
# A entrada contém vários casos de teste. Cada caso de teste contém 2 valores inteiros.

# Saída
# Para cada caso de teste mostre em qual quadrante do sistema cartesiano se encontra a coordenada lida, conforme o exemplo.


while True:
    cord_x = int(input("\nCoordenada X: "))
    cord_y = int(input("Coordenada Y: "))

    if cord_x == 0 or cord_y == 0:
        print("Programa encerrado!")
        break 

    if cord_x > 0 and cord_y > 0:
        print("Primeiro quadrante\n")
    elif cord_x > 0 and cord_y < 0:
        print("Quarto quadrante\n")
    elif cord_x < 0 and cord_y > 0:
        print("Segundo quadrante\n")
    elif cord_x < 0 and cord_y < 0:
        print("Terceiro quadrante\n")
    else: 
        print("Valor invalido")
        break

    