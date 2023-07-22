# WEBFEST MOOD BOARD 

class Image:
	def __init__(self, tags, width, length):
		self.tags = tags
		self.width = width
		self.length = length
		self.area = width * length
		self.selected = False

	def set_length(self, length):
		self.length = length
	
	def set_width(self, width):
		self.width = width

	def scale_image(self, scale):
		self.area *= scale
	
	def set_selection(self, selected):
		self.selected = selected

	def get_selection(self):
		return self.selected

	def get_tags(self):
		return self.tags

	def get_area(self):
		return self.area

# 18 categories/tags - and each image has at least 3 tags 
TAGS = ['Accelerators', 'Beam systems', 'Cryogenics', 'Detectors', 
				'Electronics', 'Industrial Controls & Simulations', 'Cosmology & Astroparticle Physics'
				'Information & Communication Technology', 'Magnets', 
				'Biophysics', 'Materials', 'Mechanics', 
				'Lasers', 'Microelectronics', 'Particle Tracking & Radiation Monitoring',
				'Radio Frequency Technology', 'Superconductivity', 'Theoretical Physics']


image_example1 = Image(['Accelerators', 'Beam systems', 'Magnets'], 2, 3)
image_example2 = Image(['Cosmology & Astroparticle Physics', 'Theoretical Physics', 'Radio Frequency Technology'], 2, 3)
image_example3 = Image(['Industrial Controls & Simulations', 'Beam systems', 'Particle Tracking & Radiation Monitoring'], 2, 3)
image_example4 = Image(['Mechanics', 'Biophysics', 'Electronics', 'Radio Frequency Technology'], 2, 3)

# This list will be filled with all the pre-loaded images that the user can choose from
IMAGES = [image_example1, image_example2, image_example3, image_example4]

# User selects the images with pseudocode as follows:
	# if (the HTML/CSS interface detects mouse movement that selects an image):
		# image.selected = True
	# The web interface detects the new_length and new_width of the image after the user resizes the image as per their inclination
		# image.set_length(new_length)
		# image.set_width(new_width)


# Create a new list of Images with the selected images
selected_images = []

# For now, we can simulate user behaviour so we have 
idx = input('Which image do you want to select? (1 - 4) / Choose 0 if done: ')

while int(idx) != 0:
	image = IMAGES[int(idx) - 1]
	image.set_selection(True)
	scale = input('What factor would you like to scale it by? ')
	image.scale_image(float(scale))
	selected_images.append(image)
	idx = input('Which image do you want to select? (1 - 4) / Choose 0 if done: ')


# Create a dictionary to store the tags and their weightages based on user selection
weighting = {}

for img in selected_images:
	for tag in img.get_tags():
		current_weight = weighting.get(tag, 0)  
		weighting[tag] = current_weight + (1 * img.get_area())

# Sort the dictionary in descending order of weightage
sorted_list = sorted(weighting.items(), key = lambda x:x[1], reverse = True)

# Return the top 3 areas of interest based on user selection
print(f'Your first area of interest could be: {sorted_list[0][0]}')
print(f'Your second area of interest could be: {sorted_list[1][0]}')
print(f'Your third area of interest could be: {sorted_list[2][0]}')


		
