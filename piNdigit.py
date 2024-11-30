
import requests
import bs4


res = requests.get("https://www.piday.org/million/")


# Now we use BeautifulSoup to analyze the extracted page. Technically we could use our own custom script to loook for items in the string of res.text 
# but the BeautifulSoup library already has lots of built-in tools and methods to grab information from a string of this nature (basically an HTML file). 
# Using BeautifulSoup we can create a "soup" object that contains all the "ingredients" of the webpage. Don't ask me about the weird library names, I didn't choose them! :)

soup = bs4.BeautifulSoup(res.text,"lxml")
pi_scrap = soup.select('#million_pi')
pi_text = pi_scrap[0].text
pi_list = list(pi_text)

on = True
print("Bienvenido al generador de digitos del número PI!!!")
while on:
    while True:
        try:
            user = int(input("Por favor, indique cuantos digitos despues del punto quiere visualizar del número PI: "))
        except ValueError:
            print("No es un valor válido.")
            print("Inténtelo otra vez:")
            continue
        if isinstance(user, int):
            break

    PI_user = ''.join(pi_list[0:int(user)+2])
    print(PI_user)

    while True:
        ex = input("¿Desea realizar otra consulta? Escriba 'Y' para continuar. 'N' para salir.")
        if ex not in ['Y','y','N','n']:
            print("No es un valor válido.")
            print("Inténtelo otra vez:")
            continue
        elif ex in ['Y','y']:
            break
        elif ex in ['N','n']:
            on = False
            break


