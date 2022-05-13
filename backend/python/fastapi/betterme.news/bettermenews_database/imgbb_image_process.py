import imgbbpy
import wget
import cv2

from dotenv import load_dotenv
import os
import time
load_dotenv()
API_KEY = os.environ["API_KEY"]

def save_image(url):
	image = wget.download(url)
	#print(image)

	return image

def delete_image(image):
	time.sleep(2)
	os.remove(image)
	print("delete done")	

def upload_imgbb_image(image):
	client = imgbbpy.SyncClient(API_KEY)
	img = client.upload(file=image)
	return img.url

def imgbb_image(url:str):
	image = save_image(url)
	link = upload_imgbb_image(image)
	delete_image(image)

	return link

def crop_image(url):
	image = save_image(url)
	print(image)
	img = cv2.imread(image)
	print(img.shape) # Print image shape

	# resize image
	resized_img = cv2.resize(img,(382, 200), interpolation = cv2.INTER_AREA)
	# Cropping an image
	cropped_image = resized_img[0:200,91:291]

	# Save the cropped image
	cv2.imwrite("cropped-"+str(image), cropped_image)

	cv2.waitKey(0)
	cv2.destroyAllWindows()

	return "cropped-"+str(image)
