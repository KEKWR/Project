import requests
from bs4 import BeautifulSoup
import os,shutil

class CheckV_and_Install:
    def __init__(self,url:str,name:str,n:int):
        self.url   = url
        self.name  = name
        self.lastV = "0"
        self.i = 0
        self.n= n
        self.m =''
        self.t =''
        
    def checkLastVersion(self):
        response= requests.get(self.url)
        soup = BeautifulSoup(response.text,'lxml')
        quotes = soup.find_all('span', class_='css-truncate css-truncate-target text-bold mr-2')
        self.lastV = quotes[0].text
        

    def checkLastVersionOnPC(self):
        self.f = open('Version.txt', 'r')
        self.l = [line.strip() for line in self.f]
        if self.lastV == 'v'+self.l[self.n]: self.m =  'the latest version is already installed' 
        else:
            self.downloadLastVersion()
        

        

    def downloadLastVersion(self):
        try:os.mkdir(f'soft/')
        except: pass

        try:os.mkdir(f'soft/{self.name}')
        except: pass

        response = requests.get(f'https://github.com/anchore/{self.name}/releases/download/{self.lastV}/{self.name}_{self.lastV[1:]}_linux_amd64.deb')
        with open(f'soft/{self.name}/{self.name}.deb', 'wb') as file:
            file.write(response.content)
        self.l[self.n] = f'{self.lastV[1:]}'
        with open ('Version.txt', 'w') as f:
            for i in self.l:    
                f.write(i+'\n')

            self.m = f'the latest version of {self.name} {self.lastV} is installed'    


    def run(self):
        self.checkLastVersion()
        self.checkLastVersionOnPC()
        

# if __name__ == "__main__" :
#     chSyft = CheckV_and_Install('https://github.com/anchore/syft','syft', 0)
#     chSyft.run()
#     chGrype = CheckV_and_Install('https://github.com/anchore/grype','grype', 1)
#     chGrype.run()