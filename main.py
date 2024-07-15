import discord 
from discord.ext import commands 
import random
import requests




bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Yo soy {bot.user}")
    
    ####Comandos basicos 
@bot.command()
async def hola(ctx):
    await ctx.send("Hola!")
    
@bot.command()
async def clima(ctx):
    await ctx.send("https://smn.conagua.gob.mx/tools/DATA/MainSlider/MapaTiempo.jpg")
    
@bot.command()
async def ping(ctx):
    # Comando !ping para verificar latencia
    latency = bot.latency * 1000  # Convertir a ms
    await ctx.send(f'Pong! Latency: {latency:.2f}ms')
    

    ###MEMES
@bot.command()
async def meme(ctx):
    images = [
        "https://static.retail.autofact.cl/blog/c_url_original.1exi97kgkt7vze.jpg",
        "https://i.imgur.com/49z4BQC.gif",
        "https://i.imgur.com/lvNRWhe.jpeg",
        "https://i.imgur.com/gDQk9GQ.gif",
        "https://i.imgur.com/mLROiso.jpeg",
        "https://i.imgur.com/iXxawLm.jpeg",
        "https://i.imgur.com/NUNqvDI.jpeg",
    ]
    embed = discord.Embed(color=0x00ff00)
    embed.set_image(url=random.choice(images))
    await ctx.send(embed=embed)
    
    
    
            
@bot.command()
async def llama(ctx, *, message):
    print(message)
    response = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama3",
        "prompt": message,
        "stream": False
    })
    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Convertir la respuesta JSON a un diccionario de Python
        data = response.json()  # Esto convierte el JSON a un diccionario
        print(data)
        await ctx.send(data["response"])
    else:
        print(f'Error al hacer la solicitud. Código de estado: {response.status_code}')
    
@bot.event
async def on_message(message):
    await bot.process_commands(message)
    

    
       
bot.run("")