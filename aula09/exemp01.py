def verificar_media(n1, n2):
    media = (n1 + n2)/2

    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"
    
print(verificar_media(8, 6))
print(verificar_media(10, 1))