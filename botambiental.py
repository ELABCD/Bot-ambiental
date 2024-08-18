import discord

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send("¡Hola!")
    elif message.content.startswith('$bye'):
        await message.channel.send("¡Adiós! 😊")
    
    elif message.content.startswith('$decompose'):
        # Obtener el objeto mencionado por el usuario
        objeto = message.content[len('$decompose '):].strip().lower()
        
        # Diccionario con objetos y sus tiempos de descomposición
        tiempos_descomposicion = {
            'botella de plástico': 450,
            'lata de aluminio': 200,
            'bolsa de plástico': 10,
            'papel': 2,
            'chicle': 5,
            'vidrio': 4000
        }

        # Responder con el tiempo de descomposición si el objeto está en el diccionario
        if objeto in tiempos_descomposicion:
            tiempo = tiempos_descomposicion[objeto]
            await message.channel.send(f'Una {objeto} tarda aproximadamente {tiempo} años en descomponerse.')
        else:
            await message.channel.send(f'Lo siento, no tengo información sobre el tiempo de descomposición de "{objeto}".')

    else:
        await message.channel.send("Comando no reconocido. Prueba con $hello, $bye, o $decompose <objeto>")

client.run("MTI2NjUwNzQ1OTYwMjgwODg3Mg.GZQXP7.zcqBRUcv0Om-Ha9fnBo4n4j2SLUgTdfuuslpZ0")