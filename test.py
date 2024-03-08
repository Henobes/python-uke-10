def myfunction(navn):
    tekst = "Hello " + navn
    print(tekst)
    return tekst
mittnavn = input("Hva heter du?")
tekst = myfunction(mittnavn)
print(tekst)

