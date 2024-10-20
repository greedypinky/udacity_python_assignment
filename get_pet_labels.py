#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:                                  
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # look into directory pet_images
    try:
        image_files = listdir(image_dir)
    except FileNotFoundError:
        print(f"The directory '{image_dir}' does not exist.")

    label_dict = dict()

    for i in range(len(image_files)):
        pet_label = ""
        # check if file is NOT started with ".xxx format"
        if image_files[i][0] != '.':
            filename = image_files[i]
            pet_label = ""
            if filename not in label_dict:
                pet_label = create_label(filename)
                label_dict[filename] = [pet_label]
            else:
                label_list = label_dict[filename]
                label_dict[filename] = label_list.append(pet_label)
  
    return label_dict

def create_label(filename):
    label = ""
    space = " "
    words_lower_split = filename.lower().split("_")
    for word in words_lower_split:
        if word.isalpha():
            # for eg. boston terrier
            label += word + space
    # remove extra space
    label = label.strip()
    return label