class Song(object):
    def __init__(self, *para):
        if len(para) == 0:
            pass
        else:
            self.lyrics = para[0]

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

    def add_lyrics(self, lyrics):
        self.lyrics = lyrics


happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right here."])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

sunshine_lyrics = ["You are my sunshine",
                   "My only sunshine",
                   "You make me happy!"
                   ]

sunshine = Song()
sunshine.add_lyrics(sunshine_lyrics)
sunshine.sing_me_a_song()
