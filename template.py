import discord
from discord import app_commands
from discord.ext import commands

# init the bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# sync command 
@bot.event
async def on_ready():
    try:
        await bot.tree.sync() 
        print(f"connect with {bot.user}             [sharko template]")
    except Exception as e:
        print(f"error: {e}")

# you can add more command and delete this commande
@bot.tree.command(name="ping", description="sharko template")
async def ping(interaction: discord.Interaction):
    latency = round(bot.latency * 1000)
    await interaction.response.send_message(f"Pong! Latency : {latency}ms")

@bot.tree.command(name="echo", description="sharko template")
@app_commands.describe(message="sharko template")
async def echo(interaction: discord.Interaction, message: str):
    await interaction.response.send_message(f"{message}")


@bot.tree.command(name="help", description="sharko template")
async def help_command(interaction: discord.Interaction):
    help_text = (
        "help message"
        
    )
    await interaction.response.send_message(help_text)

# input your token here
bot.run('your token')