import discord
from discord.ext import commands
from src.utils.queryGemini import query_gemini

class GeminiCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="gemini", aliases=["ia", "ai", "ask", "chatgpt"], help="Faz uma consulta ao gemini ai")
    async def gemini(self, ctx, *, pergunta: str):
        await ctx.send("Buscando...", delete_after=2)
        result = query_gemini(pergunta)
        await ctx.send(f"** Resposta **\n{result}")

async def setup(bot):
    await bot.add_cog(GeminiCog(bot))