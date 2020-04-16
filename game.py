def error():
    return """Re blakama thes na paikses Kill Fuck Marry (kfm). koita pws grafete:
`$kfm thn mana sou|thn gkomena sou|ton paidiko sou erwta`
H akoma pio apla:
`$kfm mickey|minnie|pluto`"""


class Game:
    def __init__(self, name1, name2, name3, creator, channel):
        self.channel = channel
        self.creator = creator
        self.name1 = name1.strip()
        self.name2 = name2.strip()
        self.name3 = name3.strip()

        self.kill_msg = None
        self.fuck_msg = None
        self.marry_msg = None

        self.name1_emoji = ":pig:"
        self.name2_emoji = ":stuck_out_tongue_closed_eyes:"
        self.name3_emoji = ":dolphin:"

        self.name1_emoji_uni = u"\U0001F437"
        self.name2_emoji_uni = u"\U0001F61D"
        self.name3_emoji_uni = u"\U0001F42C"

    def game_intro(self):
        return """Wp oi kauliaries theloun na paiksoun kill fuck marry!
Les kai eixes kai sto xwrio sou {0}""".format(self.creator.mention)

    def game_start_message(self):
        return """Loipon kauliarides!
Tha paikosume kill fuck marry!
Ta uposifia thumata pros thanato gamisiatiko gamilio einai ta ekshs:
{0} : {1}
{2} : {3}
{4} : {5}""".format(
            self.name1_emoji, self.name1,
            self.name2_emoji, self.name2,
            self.name3_emoji, self.name3
        )

    def marry(self):
        return "Marry who?"

    def fuck(self):
        return "Fuck who?"

    def kill(self):
        return "Kill who?"
