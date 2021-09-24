from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play

class TextSpeech:
    """Text to Speech fuction.
         This method takes a text, and turns it into audio
        """
    def play_news(self, news):
        mp3_fp = BytesIO()
        tts = gTTS(news, lang='pt', tld='com.br')
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)
        song = AudioSegment.from_file(mp3_fp, format="mp3")
        play(song)

    """News fuction.
             This method get a list of news, and turns it into audio
             through the play_news function.
            """
    def get_news(self, list_news):
        for index, news in enumerate(list_news):
            date = news[0]
            title = news[1]
            abstract = news[2]
            all_news = ' '.join(filter(None, (date, '\n', title, '\n', abstract)))
            self.play_news(all_news)
