import praw
import playlist
import time
import re
import json

class RedditService:
    def __init__(self):
        self.REDDIT_CLIENT_FILE = "reddit_client.json"
        data = self.set_reddit_service()
        self.reddit = praw.Reddit(client_id=data['client_id'],
                        client_secret=data['client_secret'],
                        user_agent=(data['user_agent']))
        self.youtube = playlist.PlaylistService()

    def set_reddit_service(self):
        with open("reddit_client.json") as f:
            raw_data = f.read()
        data = json.loads(raw_data)
        return data

    def get_id_url(self, url):
        match = re.search(r"youtube\.com/.*v=([^&]*)", url)
        if match:
            id = str(match.group(1))
            print("ID: " + id)
            return id
        if url.find("youtu.be") >= 0:
            id = url[17:]
            print("ID: " + id)
            return id

    def get_songs_by_top_of(self, date):
        title_playlist = str(time.strftime("%d/%m/%y")) + "prueba"
        playlist_id = self.youtube.create_playlist(title_playlist)
        i=0
        for submission in self.reddit.subreddit('listentothis').top(date):
            i = i+1
            if i < 40:
                print("\n ----------------------------------------------- \n")
                title = submission.title
                song = title.split('[')[0]
                print("Song: " + song)
                genre = title.split('[')[1].split(']')[0]
                print("Genre: " + genre)
                url = submission.url
                print("URL: " + url)
                video_id = self.get_id_url(url)
                if video_id != None:
                    self.youtube.add_video_to_playlist(video_id, playlist_id)
            else: 
                break

if __name__ == "__main__":
    reddit = RedditService()
    date = ["day", "week", "month", "year"]
    reddit.get_songs_by_top_of(date[1])
