from apiclient.discovery import build

from apiclient.errors import HttpError

from oauth2client.tools import argparser
import sys
import pafy




# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps

# tab of

#   https://cloud.google.com/console

# Please ensure that you have enabled the YouTube Data API for your project.

DEVELOPER_KEY = "AIzaSyBAl6nVRAys1ZNhICd0sJmVZfeEbE1pt8Y "

YOUTUBE_API_SERVICE_NAME = "youtube"

YOUTUBE_API_VERSION = "v3"


videos = []

channels = []

playlists = []

videoid = []


def youtube_search(options):

  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,

    developerKey=DEVELOPER_KEY)



  # Call the search.list method to retrieve results matching the specified

  # query term.

  search_response = youtube.search().list(

    q=options.q,

    part="id,snippet",

    maxResults=options.max_results

  ).execute()





  # Add each result to the appropriate list, and then display the lists of

  # matching videos, channels, and playlists.
  i1=1
  i2=1
  i3=1
  for search_result in search_response.get("items", []):


    if search_result["id"]["kind"] == "youtube#video":


      videos.append(str(i1)+". %s " % (search_result["snippet"]["title"]))


      videoid.append(search_result["id"]["videoId"])
      i1+=1

    elif search_result["id"]["kind"] == "youtube#channel":


      channels.append(str(i2)+". %s (%s)" % (search_result["snippet"]["title"],

                                   search_result["id"]["channelId"]))
      i2+=1

    elif search_result["id"]["kind"] == "youtube#playlist":


      playlists.append(str(i3)+". %s (%s)" % (search_result["snippet"]["title"],

                                    search_result["id"]["playlistId"]))
      i3+=1



  #print ",".join(videos).encode(sys.stdout.encoding, errors='replace')

'''
  print "Videos:\n", "\n".join(videos).encode(sys.stdout.encoding, errors='replace'), "\n"

  print "Channels:\n", "\n".join(channels).encode(sys.stdout.encoding, errors='replace'), "\n"

  print "Playlists:\n", "\n".join(playlists).encode(sys.stdout.encoding, errors='replace'), "\n"
'''






def youtubeplay(vname):


      argparser.add_argument("--q", help="Halsey", default=vname)

      argparser.add_argument("--max-results", help="Max results", default=10)

      args = argparser.parse_args()



      try:

        youtube_search(args)

      except HttpError as e:

        print ("HTTP error")


      numofsong=1
      yurl = "https://www.youtube.com/watch?v="+videoid[0]

      '''
      yvideo = pafy.new(yurl)
      bestaudio = yvideo.getbestaudio(preftype="m4a")
      yurl=bestaudio.url
      '''
      return yurl
