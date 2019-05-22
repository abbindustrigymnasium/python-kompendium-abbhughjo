
#Kapitel 2

#Makera koden du vill använda och klicka på ctrl och * för att av kommentera och klicka sedan på samma sak för att kommentera bort igen för att använda en ny kod 





                    #2.1

# citat =" datatyper har inbyggda metoder "
# print (citat.upper())


                    #2.2

# tal = float(input('Skriv ditt decimal tal: '))
# print(round(tal))

                    #2.3

# print('Hallå')
# namn = input('Vad är ditt förnamn?: ')
# efter = input('vad är ditt efternamn?: ')
# print('hej på dig ' + namn + " " + efter)


                    #2.4

# age = int(input('Hur gammal är du?: '))

# if age < 18 < 0:
#     i = 18-age
#     print(str(i) +' år kvar tills du är myndig!')

# elif age >= 18:
#     print('Du är myndig!')

# elif age<0:
#     print('skriv in din riktiga ålder')

# else:
#     print('error')

                    #2.5

# import math

# antalElever = int(input('Antal elever?: '))

# tvåKorvar = int(input('Hur många ska ha 2 vanliga korvar?: '))
# print(str(antalElever- tvåKorvar) + ' elever kvar')
# treKorvar = int(input('Hur många ska ha 3 vanliga korvar?: '))
# print(str(antalElever- (tvåKorvar+treKorvar)) + ' elever kvar')

# tvåVeg = int(input('Hur många ska ha 2 veganska korvar?: '))
# print(str(antalElever- (tvåKorvar + treKorvar + tvåVeg)) + ' elever kvar')
# treVeg = int(input('Hur många ska ha 3 veganska korvar?: '))

# sak = tvåKorvar + treKorvar + tvåVeg + treVeg

# if sak == antalElever:

#     prisdricka = antalElever * 13.95

#     print(str(antalElever) +' så många läsk')

#     antalkorvar = tvåKorvar * 2 + treKorvar * 3

#     packKorv = antalkorvar/8

#     prisKorv = math.ceil(packKorv) * 20.95

#     print(str(math.ceil(packKorv))+ ' packet korv')


#     antalVeg = tvåVeg * 2 + treVeg * 3

#     packVeg = antalVeg/4

#     prisVeg = math.ceil(packVeg) * 34.95

#     print(str(math.ceil(packVeg))+' packet vegetarisk korv')

#     prisTot = prisVeg + prisdricka + prisKorv

#     print(str(prisTot)+ ' total pris')

# else:
#     print('mer/mindre som ska ha korv än elever! Räkna igen')