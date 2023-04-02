from datetime import timedelta,datetime
import json

from fastapi import FastAPI
from script import CheckV_and_Install
import os

from os import environ

from models.database import database
from routers import users

from subprocess import Popen, PIPE

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(users.router)

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
    
    os.system('ansible-playbook /home/kali/Project/ansible/playbook.yml -i /home/kali/Project/ansible/hosts.txt --vault-password-file=/home/kali/Project/ansible/vault.txt')
    return 'Sbom successfully generated'

@app.get('/Grype/{server_name}')
def makeGrype(server_name:str):
    now = datetime.now()
    sbom_servers = os.listdir('/home/kali/Project//sbom')
    if server_name in sbom_servers:
        try:
            os.system('cd  sbom/{server_name}')
            os.system('mkdir grype')
            os.system(f'cd /home/kali/Project/grype && mkdir {server_name}')
            os.system(f'cd /home/kali/Project/grype/{server_name} && mkdir {now.day}-{now.month}-{now.year}')
        except:
            pass
        os.system(f'grype sbom/{server_name}/sbom.json -o json  --add-cpes-if-none >> grype/{server_name}/{now.day}-{now.month}-{now.year}/grype.json')
        return 'Grype successfully generated'
    else:
        return 'There is no such server'




