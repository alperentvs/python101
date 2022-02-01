username = 'alperentavas'
password = '1234'

if (username == "alperentavas"): # Blok yapisi oldugu icin girintilere dikkat etmek gerekli. Aksi halde "IndentationError" hatasi alinir.
    if(password == "12345"):
        print('Uygulamaya hos geldiniz.')
    else:
        print('parola yanlis')
else:
    print("username ya da parola yanlis") 