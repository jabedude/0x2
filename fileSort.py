__author__ = 'sinis'
#Thanks Hannah
import os

picture_list = [".jpg", ".png", ".gif"]
document_list = [".doc", ".pdf"]
movie_list = [".mp4", "webm"]


print("Please enter the directory")
target_directory = raw_input(">")

os.makedirs(target_directory+r'\Pictures')
os.makedirs(target_directory+r'\Documents')
os.makedirs(target_directory+r'\Movies')
os.makedirs(target_directory+r'\Applications')

for _file in os.listdir(target_directory):
    #print(_file)
    #print(os.path.isdir(target_directory+"\\"+_file))
    if(_file[-4:] in picture_list):
        print("Picture!")
    elif(_file[-4:] in document_list):
        print("Document!")
    elif(_file[-4:] in movie_list):
        print("Movie!")
    elif(_file[-4:] == ".exe"):
        print("Application!")
    elif((os.path.isdir(target_directory+"\\"+_file))):
        pass
    else:
        print("UNK FILE :( " + _file)
