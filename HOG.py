import sys
import dlib
from skimage import io
import numpy as np

from PIL import Image
#from PIL.Image import crop

# Take the image file name from the command line
file_name = sys.argv[1]
print (file_name)
#file_name = '/home/pawel/Documents/CezWorkspac1/FaceBot/zjeby.jpg'

im = Image.open(file_name)
rgb_im = im.convert('RGB')
file_name = file_name.split('.')[0] + '.jpg'
rgb_im.save(file_name)

# Create a HOG face detector using the built-in dlib class
face_detector = dlib.get_frontal_face_detector()

win = dlib.image_window()

# Load the image into an array
img = io.imread(file_name)
to_crop = Image.open(file_name)

# Run the HOG face detector on the image data.
# The result will be the bounding boxes of the faces in our image.
detected_faces = face_detector(img, 1)

print("I found {} faces in the file {}".format(len(detected_faces), file_name))

# Open a window on the desktop showing the image
win.set_image(img)

# Loop through each face we found in the image
for i, face_rect in enumerate(detected_faces):

	# Detected faces are returned as an object with the coordinates 
	# of the top, left, right and bottom edges
	print("- Face #{} found at Left: {} Top: {} Right: {} Bottom: {}".format(i, face_rect.left(), face_rect.top(), face_rect.right(), face_rect.bottom()))
	little = to_crop.crop((face_rect.left(), face_rect.top(), face_rect.right(), face_rect.bottom()))
	little.save('mala.jpg')

	# Draw a box around each face we found
	win.add_overlay(face_rect)
	        
# Wait until the user hits <enter> to close the window	        
dlib.hit_enter_to_continue()
