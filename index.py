import discord

from game import Game, error
from secret import connect_key

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


game = None


@client.event
async def on_message(message):
    global game

    if message.author == client.user:
        return

    if (game != None):
        await send_results(game)

    if message.content.startswith('$hello'):
        await message.channel.send(
            ' :pig: Ela kauliarh {0}. To afentiko mou emathe ena paixnidi steile $kfm gia na sou pw.'.format(
                message.author.mention))
    if message.content.startswith('$kfm'):
        words = message.content[4:].split("|")
        if (len(words) != 3):
            await message.channel.send(error())
            return

        game = Game(words[0], words[1], words[2], message.author, message.channel)
        await message.channel.send(game.game_intro())
        msg = await message.channel.send(game.game_start_message())

        msg = await message.channel.send(game.kill())
        await add_all_reactions(game, msg)
        game.kill_msg = msg

        msg = await message.channel.send(game.fuck())
        await add_all_reactions(game, msg)
        game.fuck_msg = msg

        msg = await message.channel.send(game.marry())
        await add_all_reactions(game, msg)
        game.marry_msg = msg

        # try:
        #     reaction, user = await client.wait_for('reaction_add', timeout=10.0, check=check)
        # except asyncio.TimeoutError:
        #     await channel.send('👎timeout')
        # else:
        #     await channel.send('👍done')
        #
        # send_results(game)


async def send_results(game: Game):
    kill_msg = await game.channel.fetch_message(game.kill_msg.id)
    fuck_msg = await game.channel.fetch_message(game.fuck_msg.id)
    marry_msg = await game.channel.fetch_message(game.marry_msg.id)

    kill_map = await create_map(game, kill_msg.reactions)
    fuck_map = await create_map(game, fuck_msg.reactions)
    marry_map = await create_map(game, marry_msg.reactions)

    print(kill_map)
    print(fuck_map)
    print(marry_map)
    for user in kill_map.keys():
        if (kill_map[user] != None and fuck_map[user] != None and marry_map[user] != None):
            await game.channel.send("O {0} tha skotonai {1}, tha fortonai {2} kai tha pantreuotan {3}".format(
                user, kill_map[user], fuck_map[user], marry_map[user]))


async def create_map(game, kill_reactions):
    map = dict()
    for reaction in kill_reactions:
        async for user in reaction.users():
            print(user)
            print(reaction)
            if user == client.user:
                continue
            map[user] = get_name_from_reaction(reaction, game)
    return map


def get_name_from_reaction(reaction, game):
    if (str(reaction.emoji) == game.name1_emoji_uni):
        return game.name1
    if (str(reaction.emoji) == game.name2_emoji_uni):
        return game.name2
    if (str(reaction.emoji) == game.name3_emoji_uni):
        return game.name3


async def add_all_reactions(game, msg):
    await msg.add_reaction(game.name1_emoji_uni)
    await msg.add_reaction(game.name2_emoji_uni)
    await msg.add_reaction(game.name3_emoji_uni)


client.run(connect_key)
