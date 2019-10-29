from youtubeex import *
import vlc
songurl=youtubeplay('chris brown')
#print songtitle+'\n'
player=vlc.MediaPlayer(songurl)
player.play()
