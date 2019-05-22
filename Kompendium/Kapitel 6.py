import requests

#6.1

# ui = input('Skriv in ett heltal: ')

# url = 'http://77.238.56.27/examples/numinfo/?integer='+ui
# r = requests.get(url)
# response_dictionary = r.json()


# if response_dictionary['even'] == False:
#     isEven = 'Udda'
# else:
#     isEven = 'Jämnt'

# if response_dictionary['prime'] == False:
#     isPrime = 'inte ett Primtal'
# else:
#     isPrime = 'ett Primtal'

# print(ui+ ' är ett ' + isEven + ' nummer. Nummret är ' + isPrime + ' . Nummrets faktorer är: ')

# for factors in response_dictionary['factors']:
#     print(factors)

#6.2

# ui = input('Skriv in ett en stad (Stockholm/Göteborg/Malmö/Uppsala/Västerås): ')

# final = ui.lower()


# url = 'https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/'+final
# r = requests.get(url)
# response_dictionary = r.json()
# print("-------------------------------------------------")
# print('                      FORCAST')
# print("*************************************************")



# slut = range(5)

# for i in slut:
#     print(response_dictionary['forecasts'][i]['date'], "                                  ", response_dictionary['forecasts'][i]['forecast'])

#6.3

# print('Artister som finns')
# print("")

# url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"
# r =  requests.get(url)
# artists = r.json()

# hej = range(8)
# lol = []
# for i in hej:
#     print(artists['artists'][i]['name'])
#     lol.append(artists['artists'][i]['name'])

# ui = input('Vilken artist vill du veta mer om?: ')


# if ui in lol:
#     hej = artists['artists'][lol.index(ui)]['id']

# url2 = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/" + hej
# h = requests.get(url2)
# info = h.json()


# gen = info['artist']['genres']

# print('Generas: ') 

# for generas in gen:
#     print(generas)

# print('Years active: ', str(info['artist']['years_active']))

# print('Members: ', info['artist']['members'])



