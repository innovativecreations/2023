
import os

files = os.listdir("vid")
print(files)
#
# while True:
#     for vid in files:
#         print()

import vlc



# Create a VLC instance
vlc_instance = vlc.Instance()

# Create a media player
player = vlc_instance.media_player_new()

while True:
# Iterate over video paths
    for vid in files:
        # Load the video file
        video_path = "vid/" + vid
        media = vlc_instance.media_new(video_path)
        # full screen

        player.set_fullscreen(True)

        # Set the media to the player
        player.set_media(media)

        # Play the video
        player.play()

        # Wait for the video to finish
        while player.get_state() != vlc.State.Ended:
            pass
        
# Release the media player and instance
player.release()
vlc_instance.release()

       

