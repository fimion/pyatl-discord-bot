import pkgutil


def setup(bot):
    for p in pkgutil.walk_packages([__name__]):
        bot.load_extension(f'{__name__}.{p.name}')
