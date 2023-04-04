from fastapi import APIRouter
import os
from subprocess import Popen, PIPE
from datetime import datetime

now = datetime.now()

router = APIRouter()

@router.get('/Grype/{server_name}')
def makeGrype(server_name:str):
    sbom_servers = os.listdir('/home/kali/Project//sbom')
    if server_name in sbom_servers:
        try:
            os.system('cd  sbom/{server_name}')
            os.system('mkdir grype')
            os.system(f'cd grype && mkdir {server_name}')
            os.system(f'cd grype/{server_name} && mkdir {now.day}-{now.month}-{now.year}')
        except:
            pass
        os.system(f'grype sbom/{server_name}/{now.day}-{now.month}-{now.year}/sbom.json -o json  --add-cpes-if-none >> grype/{server_name}/{now.day}-{now.month}-{now.year}/grype.json')
        return 'Grype successfully generated'
    else:
        return 'There is no such server'

@router.get('/grypehr')
def make_grype_human_readeble(server_name:str):
    a = ['grype',f'sbom/{server_name}/{now.day}-{now.month}-{now.year}/sbom.json']
    b = Popen(a,stdout=PIPE)
    data, error = b.communicate()
    return data.decode(encoding='cp866')