from bs4 import *
import requests
import os

# CREATE FOLDER
def create_dir(parsed_images):
	try:
		created_dir = input("Provide the Folder Name that you want the images to download --> ")
		os.mkdir(created_dir)

	except:
		print("The entered folder name already exists!")
		create_dir(parsed_images)

	image_downloader(parsed_images, created_dir)


# DOWNLOAD ALL PARSED IMAGES
def image_downloader(parsed_images, created_dir):

	count = 0
	not_downloaded = []

	print(f"Total {len(parsed_images)} Images Found on the Website!")

	if len(parsed_images) == 0:
		print("No images found!")
	elif len(parsed_images) != 0:
		for i, img in enumerate(parsed_images):
			try:
				image_uri = img["src"]						# searching for "src"
				
			except KeyError:
				try:
					image_uri = img["data-fallback-src"]					# searching for "data-fallback-src"
				
				except KeyError:
					try:
						image_uri = img["data-src"]							# searching for "data-src"
					
					except KeyError:
						try:
							image_uri = img["data-srcset"]					# searching for "data-srcset"

						except KeyError:
							image_uri=None
			if image_uri is None:
				continue										# if no Source URL found

			try:
				response = requests.get(image_uri)
				if response.ok:
					content_type = response.headers.get('Content-Type', '')
					if 'image' in content_type:
						try:
							decoded_content = response.content.decode('utf-8')			# decoding the response content as UTF-8
						except UnicodeDecodeError:
				# If decoding fails, write the binary content to a file
							with open(f"{created_dir}/images{i+1}.jpg", "wb") as f:
								f.write(response.content)
							count += 1

			except:
				not_downloaded.append(image_uri)
				pass

		if count == len(parsed_images):
			print("All Images Downloaded!")
			for i in not_downloaded:
				print(i)
			
		else:
			print(f"Total {count} Images Downloaded Out of {len(parsed_images)}")
			print("Links of images not downloaded are:")
			for i in not_downloaded:
				print(i)

# MAIN FUNCTION START
def main(url):
	response = requests.get(url)								# Get all URL contents
	soup = BeautifulSoup(response.text, 'html.parser')			# Parse the HTML code
	parsed_images = soup.findAll('img')							# Look for all the images present in the URL	

	# Call folder create function
	create_dir(parsed_images)


# take url
# url = input("Enter URL:- ")
url = 'https://www.servetel.in/'
# CALL MAIN FUNCTION
main(url)