# import os

# files = os.listdir("vid")
# print(files)
# #
# # while True:
# #     for vid in files:
# #         print()

# import vlc

# video_paths = ['path/to/video1.mp4', 'path/to/video2.mp4', 'path/to/video3.mp4']

# # Create a VLC instance
# vlc_instance = vlc.Instance()

# # Create a media player
# player = vlc_instance.media_player_new()

# while True:
# # Iterate over video paths
#     for vid in files:
#         # Load the video file
#         video_path = "vid/" + vid
#         media = vlc_instance.media_new(video_path)
#         # full screen

#         #     player.set_fullscreen(True)

#         # Set the media to the player
#         player.set_media(media)

#         # Play the video
#         player.play()

#         # Wait for the video to finish
#         while player.get_state() != vlc.State.Ended:
#             pass

# # Release the media player and instance
# player.release()
# vlc_instance.release()

from flask import *


import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
from werkzeug.utils import secure_filename

# Initialize the Firebase Admin SDK
cred = credentials.Certificate('firebase/services.json')
firebase_admin.initialize_app(cred, {'storageBucket': 'ad-vid.appspot.com'})

def upload_video(file_path, destination_path):
    bucket = storage.bucket()

    blob = bucket.blob(destination_path)
    blob.upload_from_filename(file_path)

    print('Video uploaded successfully!')

# Provide the local file path and the desired destination path in Firebase Storage


def upload_file_to_storage(file, destination_path):
    # Create a unique filename
    filename = secure_filename(file.filename)
    # Get the default bucket from Firebase
    bucket = storage.bucket()
    # Specify the destination path in the bucket
    blob = bucket.blob(destination_path + filename)
    # Upload the file to Firebase Cloud Storage
    blob.upload_from_string(file.read(), content_type=file.content_type)
    # Get the public URL of the uploaded file
    url = blob.public_url
    return url

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['video']
        m = upload_file_to_storage(file, "")

        return m
    return render_template('index.html')


app.run()
