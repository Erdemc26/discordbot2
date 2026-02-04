import discord
from discord.ext import commands
import random
import os

description = """An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here."""

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', description=description, intents=intents)

@bot.event
async def on_ready():
    # Tell the type checker that User is filled up at this point
    assert bot.user is not None

    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def atik(ctx):
    await ctx.send("""---Doğadaki Atıkların Yok Olma Süresi---
             Cam Şişe: 4000 yıl
             Pet Şişe: 400 yıl
             Plastik Tabak: 500 yıl
             Sigara Atığı: 2 yıl
             Alüminyum: 100 yıl
             Atık Pil: 300 yıl""")
    
    with open('doga.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    
@bot.command()
async def atikyardim(ctx):
    await ctx.send("""---Evlerimizdeki Atıkları Nasıl Azaltabiliriz?---
                   1- Plastik atıkları azaltın
                   2- Kağıt kullanmayın
                   3- Meyve kabuklarını saklayın
                   4- Eşyalarınızı geri dönüştürün""")
    
@bot.command()
async def geridonusum(ctx):
    await ctx.send("""---Evdeki Atıkları Nasıl Geri Dönüştürebiliriz?---
                   
                   GERİ DÖNÜŞÜM NEDEN ÖNEMLİ?

                   Geri dönüşüm süreci, çeşitli şekillerde kirliliğin
                   azaltılmasına yardımcı olur.
                   • Yeni ham maddelerin çıkarılması, işlenmesi ve
                    üretilmesi ihtiyacını azaltır. Bu da yeni
                    malzemelerin çıkarılması ve üretilmesi sırasında
                    açığa çıkan sera gazı emisyonlarını ve diğer
                    kirleticileri sınırlandırır.
                    • Madencilik, tomrukçuluk ve tarım gibi yoğun enerji
                    tüketimine olan ihtiyacı azaltır. Böylece, bu süreçler
                    sırasında açığa çıkan sera gazı emisyonları ve diğer
                    kirleticiler de azalır.
                    • Geri dönüşüm pek çok atığın farklı şekilde
                    değerlendirilmesini sağladığı için atıklardan enerji
                    üretimi de söz konusudur. Bu sayede gri enerji
                    (üretiminde yüksek karbon salınımı gerçekleşen
                    enerji) başta olmak üzere mavi ya da yeşil enerji
                    (yenilenebilir enerji) üretimine katkı sağlar.
                   
                   Geri Dönüştürülebilen Atıklar: Kağıt, plastik, metal
                   ürünler, ahşap, cam
                   Geri Dönüştürülemeyen Atıklar: Ampul, seramik, plastik
                   poşetler, çocuk bezleri""")
    
    with open('images/geri-donusumun-onemi.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("")
