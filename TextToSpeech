# Import the required module for text 
# to speech conversion
from gtts import gTTS
  
# This module is imported so that we can 
# play the converted audio
import os
import os
# The text that you want to convert to audio
mytext = 'This is test text and will be Sarveshs string.'
  
# Language in which you want to convert
language = 'en'
  
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)



#Creates a separate file to increment filename so this program makes a audiofile everytime it's name is changed
counter_file = 'counter.txt'

# Check if the counter file exists
if os.path.exists(counter_file):
    # Read the current counter value from the file
    with open(counter_file, 'r') as file:
        counter = int(file.read())
else:
    # Counter file doesn't exist, initialize the counter
    counter = 0

# Increment the counter
counter += 1

# Save the updated counter value to the file
with open(counter_file, 'w') as file:
    file.write(str(counter))

# Print the updated counter value
print(f"Counter: {counter}")


# Saving the converted audio in a mp3 file named
# welcome 

myobj.save(f"Audio File{counter}.mp3")
  


# Playing the converted file
os.system("mpg321 welcome.mp3")
