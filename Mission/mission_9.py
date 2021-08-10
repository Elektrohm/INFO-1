#Eline Nenin, Théo Denis, 17/11/18

class Duree:
    def __init__(self,h,m,s):
        while s >= 60:
            m += 1
            s -= 60
        while m >= 60:
            h +=1
            m -= 60
        self.hour = h
        self.min = m
        self.sec = s
        
    def to_seconds(self):
        secondes = self.sec
        if self.hour > 0:
            secondes += 3600*self.hour
        if self.min > 0:
            secondes += 60*self.min
        return secondes
    
    def delta(self,d):
        secondes = self.to_seconds()
        if secondes-d >= 0:
            return secondes-d
        else:
            secondes = -1
            return secondes
    
    def apres(self,d):
        delta = self.delta(d)
        if delta >= 0:
            return True
        if delta == -1:
            return False
    
    def ajouter(self,d):
        self.sec += d
        while self.sec > 60:
            self.min += 1
            self.sec -= 60
        while self.min > 60:
            self.hour +=1
            self.min -= 60
    
    def __str__(self):
        return "{0:02}:{1:02}:{2:02}".format(self.hour,self.min,self.sec)
        

class chanson:
    def __init__(self,t,a,Duree):
        self.song = t
        self.artist = a
        self.Duree = Duree
        
    def duree(self):
        return self.Duree
            
    def __str__(self):
        return "{0} - {1} - {2}".format(self.song,self.artist,self.Duree.__str__())
    
class album:
    def __init__(self):
        self.name = {}
        
    def structure(d):
        h,m = 0,0
        while d > 3600:
            h += 1
            d -= 3600
        while d > 60:
            m += 1
            d -= 60
        s = d
        return "{0:02}:{1:02}:{2:02}".format(h,m,s)
    
    def sec_in_album(self):
        duree_album = 0
        for numbers in self.name:
            connard = self.name.get(numbers,0).split()[2].split(':')
            fuck = Duree(int(connard[0]),int(connard[1]),int(connard[2]))
            lst = fuck.to_seconds()
            duree_album += lst
        return duree_album
    
    def en_tête(self,numéro):
        number_songs = str(len(self.name))
        temps = self.sec_in_album()
        time = album.structure(temps)
        return('Album'+' '+str(numéro) + ' (' + number_songs + ' chansons, '+ time +')')
    
    def corps(number,i):
        song = chanson(i[0],i[1],Duree(int(i[2].split(':')[0]),int(i[2].split(':')[1]),int(i[2].split(':')[2])))
        line = song.__str__()
        return("{0:02} : {1}".format(number,line))
        
    def __str__(self):
        print(self.en_tête(numéro))
        for number in self.name:
            i = self.name.get(number).split()
            print(album.corps(number,i))
            
    def add(self,chanson):
        time = chanson.Duree.to_seconds()
        duree_album = 0
        for songs in self.name:
            connard = self.name.get(songs,0).split()[2].split(':')
            fuck = Duree(int(connard[0]),int(connard[1]),int(connard[2]))
            lst = fuck.to_seconds()
            duree_album += lst
        if len(self.name)+1 >= 100 or duree_album + time >= 4500:
            return False
        if len(self.name) + 1 < 99:
            if duree_album + time < 4500:
                self.name[len(self.name)+1] = str(chanson.song)+' '+str(chanson.artist)+' '+str(chanson.Duree)
                return True


t = True
i = 0
file = open('music_db.txt','r')
long = len(file.readlines())
numéro = 0
while t:
    numéro += 1
    albu = album()
    while True:
        if i < long:
            file = open('music_db.txt','r')
            lst = file.readlines()[i].split()
            song = chanson(lst[0],lst[1],Duree(0,int(lst[2]),int(lst[3])))
            i += 1
            if albu.add(song) == False:
                albu.__str__()
                print('\n')
                i -= 1
                break
            
        if i >= long:
            albu.__str__()
            t = False
            file.close()
            break

"""

class Command:
    
    nbre_command=0
    sum_price=0
    
    def __init__(self,id_buyer, id_item, q, p):
        self.id_buyer=id_buyer
        self.id_item=id_item
        self.quantity=q
        self.price=p
        
    def get_price(self):
        w=int(self.quantity) * float(self.price)
        return w
    def get_number_total_command(self):
        Command.nbre_command += 1
        return Command.nbre_command
    
    def get_total_price(self):
        Command.sum_price+=float(get_price())
        return Command.sum_price 
    
    def __str__(self):
        return " {}, {} : {} * {} = {}".format(self.id_buyer,self.id_item,self.quantity,self.price, get_price())




                     
"""