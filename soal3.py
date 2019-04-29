import requests

url = 'https://newsapi.org/v2/top-headlines?country=id&category='
key = 'a78fdb2c6da54f4b8b65a7b2a07f1c52'

print('Selamat datang, mau tahu berita apa hari ini?\n'
  '[1] Berita seputar teknologi\n'
  '[2] Berita seputar bisnis\n'
  '[3] Berita seputar olahraga\n'
  '[4] Berita seputar kesehatan\n'
  '[5] Berita seputar science')

userInput = int(input('Ketik pilihan anda : '))

if userInput == 1:
    judulTeknologi = requests.get(url+'technology&apiKey='+key)

    for i in range(5):
        print(i+1, '-', judulTeknologi.json()['articles'][i]['title'])

elif userInput == 2:
    judulBusiness = requests.get(url+'business&apiKey='+key)

    for i in range(5):
        print(i+1, '-', judulBusiness.json()['articles'][i]['title'])

elif userInput == 3:
    judulSports = requests.get(url+'sports&apiKey='+key)

    for i in range(5):
        print(i+1, '-', judulSports.json()['articles'][i]['title'])

elif userInput == 4:
    judulKesehatan = requests.get(url+'health&apiKey='+key)

    for i in range(5):
        print(i+1, '-', judulKesehatan.json()['articles'][i]['title'])

elif userInput == 5:
    judulSains = requests.get(url+'science&apiKey='+key)

    for i in range(5):
        print(i+1, '-', judulSains.json()['articles'][i]['title'])

else:
    print('Invalid input!')