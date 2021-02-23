# Importing all necessary libraries
import cv2
import os

'''
# Read the video from specified path
cam = cv2.VideoCapture(0)

# frame
currentframe = 0
while(True):

	# reading from frame
	ret, frame = cam.read()

	if ret :
		# if video is still left continue creating images
		name = 'name' + str(currentframe) + '.jpg'
		print('Creating...' + name)

		# writing the extracted images
		cv2.imwrite(name, frame)

		# increasing counter so that it will
		# show how many frames are created
		currentframe += 1
	if currentframe == 5 :
		break

    
		

# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()
'''

def camera():
	cam = cv2.VideoCapture(0)
	currentframe = 0
	while(True):
		ret, frame = cam.read()
		if ret:
			name = 'name' + str(currentframe) +'.jpg'
			cv2.imwrite(name, frame)
			currentframe += 1
		if currentframe == 5 :
			break

	

camera()


