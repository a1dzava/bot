import discord
from discord.ext import commands



client = commands.Bot( command_prefix = '!' )

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name="to keep it a secret", url="https://www.twitch.tv/saor1a"))
    print( 'BOT подключен.' )

# clear
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )
async def clear( ctx, amount = 100 ):
    await ctx.channel.purge( limit = 1 )

# test
@client.command( pass_context = True )
async def test( ctx, amount = 1 ):
    await ctx.channel.purge( limit = 1 )
    author = ctx.message.author
    await ctx.send( f'{ author.mention } zxc' )

# kick
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )
async def kick( ctx, member: discord.Member, *, reason = None ):
    await ctx.channel.purge( limit = 1 )
    await member.kick( reason = reason )
    await ctx.send( f'kick: { member.mention }' )

# ban
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )
async def ban( ctx, member: discord.Member, *, reason = None ):
    await ctx.channel.purge( limit = 1 )
    await member.ban( reason = reason )
    await ctx.send( f'ban: { member.mention }' )

# unban
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )
async def unban(ctx, *, member):
    await ctx.channel.purge( limit = 1 )
	banned_users = await ctx.guild.bans()
	member_name, member_discriminator = member.split('#')
	for ban_entry in banned_users:
		user = ban_entry.user
		if (user.name, user.discriminator) == (member_name, member_discriminator):
 			await ctx.guild.unban(user)
 			await ctx.channel.send(f"unbanned: {user.mention}")



# token
token = open( 'token.txt', 'r' ).readline()
client.run( token )




