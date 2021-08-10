from PIL import Image
import os 

smiley = Image.open(path)
print(smiley.size)
smiley.thumbnail((100,100))
smiley.save(name,format)
new.("RGB",size de l image)
new_im = Image.new("RGB",(400,200))
new_im.paste(smiley,(0,0))
new_im.paste(smiley,(200,0))
new_im.save

class Counters:
    def __init__(self,number):
        l = {}
        for i in range(number):
            l[i] = 0
        self.__number = l

    def next(self,number):
        if self.__number.get(number,'error')=='error':
            raise IndexError
        else: 
            self.__number[number] += 1
            return self.__number.get(number,'error')-1 
    

