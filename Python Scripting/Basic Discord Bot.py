import os
import discord
from discord.ext import commands, tasks
from discord import app_commands

# Initialize the bot with intents
intents = discord.Intents.default()
intents.messages = True  # Enable the message intent
intents.message_content = True  # Enable message content intent
bot = commands.Bot(command_prefix="!", intents=intents)

# Define the channel and guild ID
CHANNEL_ID = 1185649103913353356
GUILD_ID = 1128304985499766924

# Traditional command (!yes)
@bot.command(name='yes')
async def yes(ctx):
    await ctx.send("Hello World")

# Traditional command (!no)
@bot.command(name='no')
async def no(ctx):
    await ctx.send("Goodbye World")

# Command to sync slash commands globally
@bot.command(name='sync', description='Owner only')
async def sync(ctx):
    if ctx.author.id == 511971193298092044:  # Replace with your Discord user ID
        await bot.tree.sync()
        print('Command tree synced globally.')
        await ctx.send('Command tree synced globally.')
    else:
        await ctx.send('You must be the owner of the bot to use this command!')

# Slash command to choose between "Hello World" and "Goodbye World"
@bot.tree.command(name="hello_goodbye", description="Choose to say Hello World or Goodbye World")
@app_commands.choices(option=[
    app_commands.Choice(name='Hello', value='hello'),
    app_commands.Choice(name='Goodbye', value='goodbye')
])
async def hello_goodbye(interaction: discord.Interaction, option: app_commands.Choice[str]):
    if option.value == 'hello':
        await interaction.response.send_message("Hello World but in a slash command")
    elif option.value == 'goodbye':
        await interaction.response.send_message("Goodbye World but in a slash command")

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')
    # Sync the slash command with the guild
    await bot.tree.sync(guild=discord.Object(id=GUILD_ID))
    print("Slash commands synced!")  # Log that commands were synced

# Main function to run the bot
def run():
    bot_token = os.getenv('SCHOOL_BOT')
    if bot_token:
        bot.run(bot_token)
    else:
        print("Bot token not found. Please set the SCHOOL_BOT environment variable.")

if __name__ == "__main__":
    run()