'''
Created on 16 Oct 2017

@author: Bruno Ono

Before use:

    - All images should be in the same folder and write the folder path at variable 'path'
    - Images from different fields of the sample should be named sequentially (image1.jpg, image2.jpg)
    - For the same image, the channels in each image should be named with "." + "number":
   
        image1.1.jpg - For channel 1
        image1.2.jpg - For channel 2
        image1.3.jpg - For channel 3
        
    - For this programme it is possible to merge 3 channels in the same image
'''

import cv2


def mrg_images():
    
    # write the folder path of images
    path = str( 'write here!' ) + '/'
 
    # write the number of images
    N = int(input("Enter the number samples: "))
   
    # write the common name of the images file e.g (image1.1.jpg,image1.2.jpg,image2.1.jpg,...) the common name is "image"
    common_name = input('What is the common name of the files?' + '\n' + 'Answer:' )
    
    # Write the extension file of the image
    answer1 = input("Type the extension of the image files (jpg, tif,...)" +'\n' + "Answer:")
    
    
    Ch = int(input('How many channels there is to merge?' +'\n' +  'Number of Channels ='))
    
    if Ch is 2:
        
        answer2 = input("""Choose the letter correspondent to the channels do you want to merge.
A) 1,2
B) 1,3
C) 2,3
        
Answer:""")
        
        for x in range(1,N):
            
            d = {"A":(1,2), "B":(1,3), "C":(2,3)}
            
            no_img = 2    
            
            img_1 = cv2.imread(path + common_name + str(x) +'.' + d[answer2.upper()][0] + '.' + answer1)
            img_2 = cv2.imread(path + common_name + str(x) +'.' + d[answer2.upper()][1] + '.' + answer1)
            
            img = img_1/no_img + img_2/no_img
            
            cv2.imwrite(path + common_name + str(x) +'.merged.' + answer1,img)
        
    if Ch is 3:
        
        for x in range(1,N):
            
            no_img = 3
            
            img_1 = cv2.imread(path + common_name + str(x) +'.1.' + answer1)
            img_2 = cv2.imread(path + common_name + str(x) +'.2.' + answer1)
            img_3 = cv2.imread(path + common_name + str(x) +'.3.' + answer1)
            
            
            img = img_1/no_img + img_2/no_img + img_3/no_img
            
            cv2.imwrite(path + common_name + str(x) + '.merged.' + answer1,img)
        
mrg_images()