from google.cloud import storage
import os
os_vid = os.listdir("../videos")
# print(os_vid[0])
# Initialize Google Cloud Storage client
client = storage.Client.from_service_account_json('key.json')  # Replace with the path to your key file
bucket_name = 'ad-vid.appspot.com'  # Replace with the name of your Firebase Storage bucket
bucket = client.bucket(bucket_name)
blobs = bucket.list_blobs()

# Print the names of all the files
for blob in blobs:
    if not blob.name in os_vid:
        print(blob.name)
        blob = bucket.blob(blob.name)
        # Specify the local path where you want to save the downloaded video
        local_path = "../videos/" + blob.name

        # Download the video file
        blob.download_to_filename(local_path)

        print(f"Video downloaded successfully to: {local_path}")




# from google.cloud import storage
# from google.oauth2 import service_account
#
# # Specify the path to your service account key JSON file
# key_path = 'services.json'
#
# # Create a service account credentials object
# credentials = service_account.Credentials.from_service_account_file(key_path)
#
# # Initialize the Google Cloud Storage client with the provided credentials
# storage_client = storage.Client(credentials=credentials)
#
#
# # Specify the bucket name and video file name
# bucket_name = "idks-9570b.appspot.com"
# video_filename = "vid1.mp4"
#
# # Get a reference to the video file in the bucket
# bucket = storage_client.bucket(bucket_name)
# blob = bucket.blob(video_filename)
#
# # Specify the local path where you want to save the downloaded video
# local_path = "yovideo.mp4"
#
# # Download the video file
# blob.download_to_filename(local_path)
#
# print(f"Video downloaded successfully to: {local_path}")
