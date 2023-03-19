from fastapi import FastAPI
from script import CheckV_and_Install
import os
import datetime

app =FastAPI()

@app.get('/syftD')
def syftUpdateDeb():
    chSyft = CheckV_and_Install('https://github.com/anchore/syft','syft', 0)
    chSyft.run()
    return chSyft.m

@app.get('/grypeD')
def grypeUpdateDeb():
    chGrype = CheckV_and_Install('https://github.com/anchore/grype','grype', 1)
    chGrype.run()
    return chGrype.m

@app.get('/Ansible')
def makeAnsible():
    try:
        os.mkdir(f'sbom/')
    except:
        pass
    
    os.system('ansible-playbook /home/kali/Project/ansible/playbook.yml -i /home/kali/Project/ansible/hosts.txt -kK')

@app.get('/Grype')
def makeGrype():
    now = datetime.datetime.now()
    try:
        os.system('mkdir grype')
        os.system('cd /home/kali/Project/grype && mkdir server1')
    except:
        pass
    
    os.system(f'grype sbom/server1/sbom.json -o json  --add-cpes-if-none >> grype/server1/{now.day}-{now.month}-{now.year}grype.json')