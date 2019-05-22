#8.1
# choose = 'miles'  #Variablar som anväds senare för att kolla inputen
# choose2 = 'km'

# ui = input('Ange distans: ')      #En Input som tar i den angivna distansen

# def km_to_miles(dist):    #funktion som tar in parametern dist
#     print(dist/1.609344)     #printar dist/1.6 för att omvandla den till miles 
#    

# def miles_to_km(dist):    #Samma sak som ovan fast denna multiplicerar värdet
#     km = dist*1.609344
#     print(km)

# word = ui.split()  #Delar upp inputen vid varje ord

# if choose in word:    #Om variablen som vi satte tidigare finns med i arrayen som håller de splittade orden 
#     miles_to_km(int(word[0]))

# if choose2 in word:
#     km_to_miles(int(word[0]))

#8.2


# def get(url):         #Funktion som tar in parametern url
#     import requests   #Importerar biblioteket request
#     r = requests.get(url)  #Hämtar värderna från den angivna url
#     return r.json          #returnerar värderna fast i json format

#8.3

# def line(streck):         #Funktion som tar in parametern streck som antingen är true eller false
#     if streck == True:    #Om streck är true så händer detta
#         print('***********************************************************************')
#     else:
#         print('------------------------------------------------------------------------')

# def header(txt):          #Funktion som tar in parantern txt och skriver sedan ut den med || såna runt 
#   print('  |                                ' + txt +'                                     | ')

# def echo(txt):            #Funktion som är liknande den ovan fast har bara en |
#     print('  | ' + txt)

# def prompt(txt):          #Funktion som skriver ut parametern txt i en input
#     input(txt + ' > ')