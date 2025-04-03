nota1=int(input("Nota 1:"))
nota2=int(input("Nota 2:"))

media = (nota1+nota2)/2
print(media)
if media>6:
    print("Aprovado")
elif media==6:
    print("Recuperação")
else:
    print("Reprovado")
