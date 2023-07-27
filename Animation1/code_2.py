from PIL import Image
import os

output_folder=input('Enter Output Folder Name :') #new Folder 
Logo_name=input('Enter Logo Name :')

os.chdir('images') #changes the current working directory to a specific path(images)

if not os.path.isdir(output_folder):#checking-folder-and-if-it-doesnt-exist-create-it
  os.mkdir(output_folder)


Logo=Image.open(Logo_name)
Logo_width,Logo_height =Logo.size


for filename in os.listdir('.'):#loop to find the files(images) in folder or in my path(.)
    if filename.endswith((".jpeg",".png",".jpg")):#check the file extension(if it is image or not)
       image=Image.open(filename)#open the image
       width , height = image.size

       image.paste(Logo,(width - Logo_width,height - Logo_height))
       image.save(os.path.join(output_folder,filename))