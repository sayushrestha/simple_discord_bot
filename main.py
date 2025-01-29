import discord
from discord.ext import commands

class MyBot(commands.Bot):
    async def setup_hook(self):
        try:
            synced = await self.tree.sync()
        except discord.HTTPException as e:
            print(f"Failed to sync commands: {e}")
        else:
            print(f"Synced {len(synced)} commands")

bot = MyBot(command_prefix="!", intents=discord.Intents.all())

@bot.command()
async def greet(ctx: commands.Context, member: discord.Member):
    await ctx.send(f'Hello there {member.mention}')

@bot.tree.command(name="ping")
async def ping(ctx: discord.Interaction):
    await ctx.response.send_message("Pong!")

@bot.hybrid_command()
async def echo(ctx: commands.Context, message: str):
    await ctx.send(message)

@bot.event
async def on_ready():
    print(f"{discord.utils.oauth_url(bot.user.id, permissions=discord.Permissions.all())}")

bot.run("YOUR_DISCORD_API")
