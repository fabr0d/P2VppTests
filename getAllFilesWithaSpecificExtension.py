#Import required Image library
from PIL import Image, ImageFilter
import glob, os
path = "D:\\images-661-24-GB1.5"
#path2 = "C:\\Users\\Fabrizio\\Desktop\\Todo de proyectos\\imagesbad\\pieza0\\pieza0background145" #Aca iria el directorio de el dataset

num_piezas = 3
num_bg = 661

text_files = glob.glob(path + "/**/*.png", recursive = True)

for image_path in text_files:
	#Open existing image
	OriImage = Image.open(image_path)
	#OriImage.show()

	#Applying GaussianBlur filter
	gaussImage = OriImage.filter(ImageFilter.GaussianBlur(1.5))
	#gaussImage = OriImage.filter(ImageFilter.BoxBlur(2))
	#gaussImage.show()

	#Save Gaussian Blur Image
	gaussImage.save(image_path)