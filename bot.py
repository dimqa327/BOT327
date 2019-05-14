import discord
from discord.ext import commands
from discord.ext.commands import os

Bot = commands.Bot(command_prefix="!")

@Bot.command()
async def hello(ctx):
   author = ctx.message.author
   await ctx.send(f"Приветствую! {author.mention}")

@Bot.command()
@commands.has_permissions(administrator= True)
async def mute(ctx, member: discord.Member):
   mute_role = discord.utils.get(ctx.message.guild.roles, name= "mute")
   await member.add_roles(mute_role)
token - os.environ.get.('BOT_TOKEN')