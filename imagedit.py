from PIL import Image
import sys
import argparse
import pyfiglet
import os
import math
#from consolemenu import SelectionMenu


parser = argparse.ArgumentParser()
 
parser.add_argument("-f", "--File", help = "Select File")
parser.add_argument("-s", "--Stealth",help = "Open without Banner",action='store_true')
parser.add_argument("-r", "--Resize",help = "Resize WITHOUT preserving aspect ratio. Leave blank if you want to preserve aspect ratio", action='store_true')
parser.add_argument("-c", "--Centimeter",help = "Flag for entering values in Centimeters", action='store_true')
parser.add_argument("-i", "--Inch",help = "Flag for entering values in Inches", action='store_true')
parser.add_argument("-w", "--Width",help = "Enter the width")
parser.add_argument("-he", "--Height",help = "Enter the height")

# Read arguments from command line
args = parser.parse_args()

if (args.Stealth == False):
	result = pyfiglet.figlet_format("Imagedit", font = "isometric1" )
	print(result)
else:
	print("Imagedit")

print("Selected file: % s" % args.File)
filename, file_extension = os.path.splitext(args.File)
print(file_extension)
ext = [".jpg",".jpeg",".png",".JPG",".JPEG",".PNG"]
if file_extension not in ext:
	print("Please specify a file of .jpg, .jpeg or .png")
	exit()
image = Image.open(args.File)
flag = 0

if(args.Centimeter == True):
	flag = 1
	print("Resizing image based on cm values!! (Won't maintain aspect ratio)")
	width = float(args.Width) * 37.79
	width = math.floor(width)
	height = float(args.Height) * 37.79
	height = math.floor(height)
	new_image = image.resize((int(width), int(height)))
	new_image_name = 'image' + str(width) + 'x' + str(height)
	new_image.save(new_image_name + file_extension)	
	print("Saving file as " + new_image_name)

if(args.Inch == True):
	flag = 1
	print("Resizing image based on inches values!! (Won't maintain aspect ratio)")
	width = float(args.Width) * 96
	width = math.floor(width)
	height = float(args.Height) * 96
	height = math.floor(height)
	new_image = image.resize((int(width), int(height)))
	new_image_name = 'image' + str(width) + 'x' + str(height)
	new_image.save(new_image_name + file_extension)	
	print("Saving file as " + new_image_name)

if(args.Resize == True):
	flag = 1
	print("Resizing image!! (Won't maintain aspect ratio)")
	width = math.ceil(float(args.Width))
	height = math.ceil(float(args.Height))
	new_image = image.resize((int(width), int(height)))
	new_image_name = 'image' + args.Width + 'x' + args.Height
	new_image.save(new_image_name + file_extension)	
	print("Saving file as " + new_image_name)
if flag == 0:
	print("Nothing done. Maybe you forgot the '-r' or '-c' flag!")
	print("Use '-h' flag for help.")