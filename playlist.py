import httplib2
import os
import sys

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow


class PlaylistService():
    def __init__(self):
        self.CLIENT_SECRETS_FILE = "client_secret.json"
        self.YOUTUBE_READ_WRITE_SCOPE = "https://www.googleapis.com/auth/youtube"
        self.YOUTUBE_API_SERVICE_NAME = "youtube"
        self.YOUTUBE_API_VERSION = "v3"
        self.MISSING_CLIENT_SECRETS_MESSAGE = """
        WARNING: Please configure OAuth 2.0

        To make this sample run you will need to populate the client_secrets.json file
        found at:

        %s

        with information from the API Console
        https://console.developers.google.com/

        For more information about the client_secrets.json file format, please visit:
        https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
        """ % os.path.abspath(os.path.join(os.path.dirname(__file__),
                                           self.CLIENT_SECRETS_FILE))
        self.youtube = self.get_authenticated_service()

    def get_authenticated_service(self):
        flow = flow_from_clientsecrets(self.CLIENT_SECRETS_FILE,
                                       message=self.MISSING_CLIENT_SECRETS_MESSAGE,
                                       scope=self.YOUTUBE_READ_WRITE_SCOPE)
        storage = Storage("%s-oauth2.json" % sys.argv[0])
        credentials = storage.get()
        if credentials is None or credentials.invalid:
            flags = argparser.parse_args()
            credentials = run_flow(flow, storage, flags)
        youtube = build(self.YOUTUBE_API_SERVICE_NAME, self.YOUTUBE_API_VERSION,
                        http=credentials.authorize(httplib2.Http()))
        return youtube

    def add_video_to_playlist(self, videoID, playlistID):
        add_video_request = self.youtube.playlistItems().insert(
            part="snippet",
            body={
                'snippet': {
                    'playlistId': playlistID,
                    'resourceId': {
                        'kind': 'youtube#video',
                        'videoId': videoID
                    }
                }
            }
        ).execute()
    
    def create_playlist(self,title_playlist):
        playlists_insert_response = self.youtube.playlists().insert(
            part="snippet,status",
            body=dict(
                snippet=dict(
                title=title_playlist,
                description="A playlist created with the Reddit r/listentothis Bot!"
                ),
                status=dict(
                privacyStatus="public"
                )
            )
        ).execute()
        return playlists_insert_response["id"]



if __name__ == '__main__':
    youtube = PlaylistService()
    youtube.add_video_to_playlist(
        "6NXnxTNIWkc", "PLMQqp1oCRmKQi7SRhY27sOEIrHx7nV3KE")
