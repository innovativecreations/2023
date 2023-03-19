# Python3 program to illustrate
# accessing of audio metadata
# using tinytag library

# Import Tinytag method from
# tinytag library
from tinytag import TinyTag

# Pass the filename into the
# Tinytag.get() method and store
# the result in audio variable
audio = TinyTag.get("WIN_20230318_11_53_13_Pro.mp4")

# Use the attributes
# and Display
print(audio)
