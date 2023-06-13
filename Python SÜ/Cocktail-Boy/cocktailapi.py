'''
Cocktailboy. Ein netter Kerl, der gerne Cocktails mixt.
Maximilian
01.05.2023
'''

import requests
import discord
import csv

#Hier werden Rechte für den Bot festgelegt
client = discord.Client(intents = discord.Intents.all())

#Geheimen Token auslesen damit der Bot funktioniert
file = open("abc.txt" , "r")
TOKEN = file.read()
file.close()

##############################################################################################

#Wenn der Bot bereit ist, wird folgendes in der Konsole ausgegeben
@client.event
async def on_ready ():
#mit await wartet der Bot bis er den Status geändert hat und macht dann weiter
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='"Hilfe" für Hilfe'))

    print("Moiners! Ich bin startklar!")

##############################################################################################

#Wenn eine Nachricht geschrieben wird, wird Folgendes ausgeführt
#client.event ist eine Funktion die aufgerufen wird, wenn ein Event eintritt
@client.event
async def on_message(message):
    if message.author == client.user:
        return None
#Wenn der Bot eine Nachricht mit dem Inhalt "Hilfe" bekommt, wird Folgendes ausgeführt
    if message.content == "Hilfe":
        hilfe = discord.Embed(title="Hier ist der Befehl den du brauchst:", color=0xff00ff)
        hilfe.add_field(name="Start", value="Startet die Suche", inline=False)
        hilfe.set_footer(text="Ziemlich einfach wenn du mich fragst...")
        await message.channel.send(embed=hilfe)

#Wenn der Bot eine Nachricht mit dem Inhalt "Start" bekommt, wird Folgendes ausgeführt
    if message.content == "Start":
        startfeld = discord.Embed(title="1 um nach Anfangsbuchstabe zu suchen, 2 um nach Cocktailnamen zu suchen, 3 um nach Zutat zu suchen"
                                        " oder 4 um dir einen Zufälligen anzeigen zu lassen:" , color=0xff00ff)
        startfeld.set_footer(text="Du kannst auch 'Exit' schreiben um die Suche zu beenden.")
        await message.channel.send(embed=startfeld)
    #Der Bot wartet auf eine Nachricht vom User
        message = await client.wait_for("message")

        if message.content == "1":
            cocktails = []
            try:
                eins = discord.Embed(title="Bitte gebe den Anfangsbuchstaben ein:" , color=0xff00ff)
                await message.channel.send(embed=eins)

                msg = await client.wait_for("message")
            #Er sucht nach Cocktails mit dem Buchstaben
                response = requests.get("https://www.thecocktaildb.com/api/json/v1/1/search.php?f=" + msg.content)
                for r in response.json()["drinks"]:
                    cocktails.append(r["strDrink"])
            #Er schreibt sie in eine Discord Nachricht
                antwort1 = discord.Embed(title="Hier sind die Cocktails mit dem Anfangsbuchstaben " + msg.content + ":" , color=0xff00ff)
                antwort1.add_field(name="Cocktails:", value='\n'.join(cocktails), inline=False)
                antwort1.set_footer(text="Mehr konnte ich nicht finden.")
                await message.channel.send(embed=antwort1)
            #Er fragt, ob man den Link haben will
                frage1 = discord.Embed(title="Möchtest du einen Cocktail auswählen?" , color=0xff00ff)
                frage1.add_field(name="Antworte mit:", value="Ja oder Nein", inline=False)
                frage1.set_footer(text="Du kannst auch 'Exit' schreiben um die Suche zu beenden.")
                await message.channel.send(embed=frage1)

                message = await client.wait_for("message")

                if message.content == "Ja":
                    frage1 = discord.Embed(title="Bitte gebe den Cocktailnamen ein:" , color=0xff00ff)
                    await message.channel.send(embed=frage1)
            #Er sucht die ID zu dem Drink und fügt ihn in den Link ein
                    msg = await client.wait_for("message")
                    response = requests.get("https://www.thecocktaildb.com/api/json/v1/1/search.php?s=" + msg.content)
                    for r in response.json()["drinks"]:
                        cocktails.append(r["idDrink"])
                #Er gibt den Link mithilfe einer Discord Nachricht aus
                    frage1 = discord.Embed(title="Hier ist der Cocktail mit dem Namen " + msg.content + ":" , color=0xff00ff)
                    frage1.add_field(name="Link:", value="https://www.thecocktaildb.com/drink/" + str(r["idDrink"]), inline=False)
                    frage1.set_footer(text="Prost!")
                    await message.channel.send(embed=frage1)

                elif message.content == "Nein":
                    frage1 = discord.Embed(title="Okay, dann nicht.", color=0xff00ff)
                    frage1.set_footer(text="Schade")
                    await message.channel.send(embed=frage1)

        #Wenn es einen Fehler gibt, wird Folgendes ausgeführt
            except:
                error1 = discord.Embed(title="Oh-Oh!" , color=0xff00ff)
                error1.add_field(name="Fehler:", value="Zu diesem Buchstaben gibt es keine Cocktails O.O", inline=False)
                error1.set_footer(text="Versuche es nochmal.")
                await message.channel.send(embed=error1)


        if message.content == "2":
            cocktails = []
            try:
                antwort2 = discord.Embed(title="Bitte gebe den Cocktailnamen ein:" , color=0xff00ff)
                await message.channel.send(embed=antwort2)

                msg = await client.wait_for("message")
                response = requests.get("https://www.thecocktaildb.com/api/json/v1/1/search.php?s=" + msg.content)
                for r in response.json()["drinks"]:
                    cocktails.append(r["strDrink"])
                antwort2 = discord.Embed(title="Hier sind die Cocktails mit dem Namen " + msg.content + ":" , color=0xff00ff)
                antwort2.add_field(name="Cocktails:", value='\n'.join(cocktails), inline=False)
                antwort2.set_footer(text="Mehr konnte ich nicht finden.")
                await message.channel.send(embed=antwort2)

                frage2 = discord.Embed(title="Möchtest du einen Cocktail auswählen?" , color=0xff00ff)
                frage2.add_field(name="Antworte mit:", value="Ja oder Nein", inline=False)
                frage2.set_footer(text="Du kannst auch 'Exit' schreiben um die Suche zu beenden.")
                await message.channel.send(embed=frage2)

                message = await client.wait_for("message")

                if message.content == "Ja":
                    frage2 = discord.Embed(title="Bitte gebe den Cocktailnamen ein:" , color=0xff00ff)
                    await message.channel.send(embed=frage2)

                    msg = await client.wait_for("message")
                    response = requests.get("https://www.thecocktaildb.com/api/json/v1/1/search.php?s=" + msg.content)
                    for r in response.json()["drinks"]:
                        cocktails.append(r["idDrink"])

                    frage2 = discord.Embed(title="Hier ist der Cocktail mit dem Namen " + msg.content + ":" , color=0xff00ff)
                    frage2.add_field(name="Link:", value="https://www.thecocktaildb.com/drink/" + str(r["idDrink"]), inline=False)
                    frage2.set_footer(text="Prost!")
                    await message.channel.send(embed=frage2)

                elif message.content == "Nein":
                    frage2 = discord.Embed(title="Okay, dann nicht.", color=0xff00ff)
                    frage2.set_footer(text="Schade")
                    await message.channel.send(embed=frage2)


            except:
                error2 = discord.Embed(title="Oh-Oh!" , color=0xff00ff)
                error2.add_field(name="Fehler:", value="Zu diesem Namen gibt es keine Cocktails O.O", inline=False)
                error2.set_footer(text="Versuche es nochmal.")
                await message.channel.send(embed=error2)


        if message.content == "3":
            cocktails = []
            try:
                antwort3 = discord.Embed(title="Bitte gib eine Zutat ein:", color=0xff00ff)
                await message.channel.send(embed=antwort3)

                msg = await client.wait_for("message")
                response = requests.get("https://www.thecocktaildb.com/api/json/v1/1/filter.php?i=" + msg.content)
                for r in response.json()["drinks"]:
                    cocktails.append(r["strDrink"])

                antwort3 = discord.Embed(title="Hier sind die Cocktails, welche die Zutat " + msg.content + " enthalten:",
                                         color=0xff00ff)
                antwort3.add_field(name="Cocktails:", value='\n'.join(cocktails), inline=False)
                antwort3.set_footer(text="Mehr konnte ich nicht finden.")
                await message.channel.send(embed=antwort3)

                frage3 = discord.Embed(title="Möchtest du einen Cocktail auswählen?" , color=0xff00ff)
                frage3.add_field(name="Antworte mit:", value="Ja oder Nein", inline=False)
                frage3.set_footer(text="Du kannst auch 'Exit' schreiben um die Suche zu beenden.")
                await message.channel.send(embed=frage3)

                message = await client.wait_for("message")

                if message.content == "Ja":
                    frage3 = discord.Embed(title="Bitte gebe den Cocktailnamen ein:" , color=0xff00ff)
                    await message.channel.send(embed=frage3)

                    msg = await client.wait_for("message")
                    response = requests.get("https://www.thecocktaildb.com/api/json/v1/1/search.php?s=" + msg.content)
                    for r in response.json()["drinks"]:
                        cocktails.append(r["idDrink"])

                    frage3 = discord.Embed(title="Hier ist der Cocktail mit dem Namen " + msg.content + ":" , color=0xff00ff)
                    frage3.add_field(name="Link:", value="https://www.thecocktaildb.com/drink/" + str(r["idDrink"]), inline=False)
                    frage3.set_footer(text="Prost!")
                    await message.channel.send(embed=frage3)

                elif message.content == "Nein":
                    frage3 = discord.Embed(title="Okay, dann nicht." , color=0xff00ff)
                    frage3.set_footer(text="Schade")
                    await message.channel.send(embed=frage3)

            except:
                error3 = discord.Embed(title="Oh-Oh!", color=0xff00ff)
                error3.add_field(name="Fehler:", value="Kein einziger Cocktail besitzt diese Zutat O.O", inline=False)
                error3.set_footer(text="Versuche es nochmal.")
                await message.channel.send(embed=error3)

        if message.content == "4":
            cocktails = []
            response = requests.get("https://www.thecocktaildb.com/api/json/v1/1/random.php")
            for r in response.json()["drinks"]:
                cocktails.append(r["strDrink"])
            cocktails = cocktails[0]
            antwort4 = discord.Embed(title="Hier ist dein zufälliger Cocktail:", color=0xff00ff)
            antwort4.add_field(name="Cocktail:", value=cocktails, inline=False)
            antwort4.add_field(name="Link:", value="https://www.thecocktaildb.com/drink/" + str(r["idDrink"]), inline=False)
            antwort4.set_footer(text="Prost!")
            await message.channel.send(embed=antwort4)

        if message.content == "Exit":
            exit = discord.Embed(title="Schade" , color=0xff00ff)
            exit.add_field(name="Exit:", value="Du hast die Suche beendet.", inline=False)
            exit.set_footer(text="Bis zum nächsten Mal!")
            await message.channel.send(embed=exit)

##############################################################################################

#Damit geht der Bot online und man kann mit ihm schreiben
client.run(TOKEN)
