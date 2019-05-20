from discord.ext.commands import Bot

import settings

bot = Bot(command_prefix=settings.COMMAND_PREFIX)

bot.load_extension('commands')


if __name__ == "__main__":
    bot.run(settings.DISCORD_TOKEN)
