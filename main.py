import os

import discord
from discord import app_commands
import webserver

from discord.ext import commands

token = os.environ["DISCORD_TOKEN"]


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
  print("Bot is ready")
  try:
    synced = await bot.tree.sync()
    print(f"Synced {len(synced)} command(s)")
  except Exception as e:
    print(e)


@bot.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
  await interaction.response.send_message(f"HELLO {interaction.user} this is a prova")





@bot.tree.command(name="say")
@app_commands.describe(thing_to_say="What should i say?")
async def say(interaction: discord.Interaction, thing_to_say: str):
  await interaction.response.send_message(f"Hello {interaction.user} you said {thing_to_say}")

@bot.tree.command(name="ign")
@app_commands.describe(ign="What is your IGN?")
async def ign(interaction: discord.Interaction, ign:str):
  id = interaction.user.id
  
  try:
    member = await interaction.guild.fetch_member(id)
    await member.edit(nick=ign)
    await interaction.response.send_message(f"I've changed your nickname to {ign}")
  except Exception as e:
    print(e)
    await interaction.response.send_message(f"I could not change your nickname.  Please make sure I have the correct permissions.")


webserver.keep_alive()
bot.run(token)
  
#print(os.getenv("DISCORD_TOKEN"))
