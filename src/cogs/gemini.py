import discord
from discord.ext import commands
from discord import app_commands
from src.utils.queryGemini import query_gemini

class GeminiCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="gemini", aliases=["ia", "ai", "ask", "chatgpt"], help="Faz uma consulta ao Gemini AI")
    async def gemini(self, ctx, *, pergunta: str):
        await ctx.send("Buscando...", delete_after=2)
        result = query_gemini(pergunta)
        await ctx.send(f"**Resposta:**\n{result}")

    @app_commands.command()
    async def gemini_slash(self, interaction: discord.Interaction, pergunta: str):
        await interaction.response.defer(thinking=True)
        result = query_gemini(pergunta)
        await interaction.response.send(f"**Resposta:**\n{result}")

async def setup(bot):
    await bot.add_cog(GeminiCog(bot))
