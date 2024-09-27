from time import time

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
palavra = ["a", "a", "a", "a"]

l1 = 0; l2 = 1; l3 = 2; l4 = 3  # Cada variável representa um indice da lista palvra (l1 = letra 1)

percorre_alfabeto1 = 0    # Cada índice da lista palavra necessita de uma variável que percorra o alfabeto 
percorre_alfabeto2 = 0
percorre_alfabeto3 = 0
percorre_alfabeto4 = 0

escolha = list("arte")

tempo_inicial = time()  # Contador de tempo

cont = 0
while cont < 52**4:
    palavra[l1] = alfabeto[percorre_alfabeto1]
    print(palavra)
    percorre_alfabeto1 += 1
    cont += 1

    if percorre_alfabeto1 > 51:
        palavra[l2] = alfabeto[percorre_alfabeto2]
        percorre_alfabeto2 += 1
        percorre_alfabeto1 = 0

        if percorre_alfabeto2 > 51:
            palavra[l3] = alfabeto[percorre_alfabeto3]
            percorre_alfabeto3 += 1
            percorre_alfabeto2 = 0

            if percorre_alfabeto3 > 51:
                palavra[l4] = alfabeto[percorre_alfabeto4]
                percorre_alfabeto4 += 1
                percorre_alfabeto3 = 0
                
                if percorre_alfabeto4 > 51:
                    break

    
            
tempo_final = time()    # Fim do contador de tempo

total = tempo_final -tempo_inicial

print(f"{total:.10f}\n")
print(cont)
        
