from PIL import Image
import os      # change from file to another

fit_size = int (input('Enter Size : ')) # width and height

output_folder=input('Enter Output Folder Name :') #new Folder for new images

os.chdir('images') #changes the current working directory to a specific path(images)

if not os.path.isdir(output_folder):#checking-folder-and-if-it-doesnt-exist-create-it
  os.mkdir(output_folder)

for filename in os.listdir('.'):#loop to find the files(images) in folder or in my path(.)
    if filename.endswith((".jpeg",".png",".jpg")):#check the file extension(if it is image or not)
       image=Image.open(filename)#open the image
       width , height = image.size
       
       
       
    if width > fit_size and height > fit_size:#when the image size(width,height)great than my input(fit_size)
        if width > height:
          height = int((fit_size/width)*height)
          width = fit_size
        else:
          height = fit_size
          width = int((fit_size/height)*width)
        image=image.resize((width,height))
        image=image.save(os.path.join(output_folder,filename))  
      
       
