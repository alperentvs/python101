'''
    player 1:
        id           => 1
        name         => Cristiano Ronaldo
        yearOfBirth  => 1985
        nationality  => Portugal
        current_team => Portugal
        history      => Juventus,Real Madrid,Portugal

    player 2:
        id           => 2
        name         => Lionel Messi
        yearOfBirth  => 1987
        nationality  => Argentina
        current_team => Barcelona
        history      => Barcelona,Argentina,Portugal
'''

# 1- Yukarıda verilen bilgileri liste içerisinde saklayınız.
players = {}

id = input('oyuncu id: ')
name = input('oyuncu ad: ')
yearOfBirth = input('dogum yılı: ')
nationality = input('ülke: ')
current_team = input('takım: ')
history = input('oynadığı yerler: ')

players.update({
    id: {
        "name": name,
        "yearOfBirth": yearOfBirth,
        "nationality": nationality,
        "current_team": current_team,
        "history": history.split(',')
    }
})

id = input('oyuncu id: ')
name = input('oyuncu ad: ')
yearOfBirth = input('dogum yılı: ')
nationality = input('ülke: ')
current_team = input('takım: ')
history = input('oynadığı yerler: ')

players.update({
    id: {
        "name": name,
        "yearOfBirth": yearOfBirth,
        "nationality": nationality,
        "current_team": current_team,
        "history": history.split(',')
    }
})

print(players)

# 2- id'e göre arama yapınız.
id = input('aramak istediğiniz oyuncu id: ')
player = players.get(id)
print(player)

# 3- id'e göre bilgi kayıt siliniz.
id = input('silmek istediğiniz oyuncu id: ')
players.pop(id)

print(players)