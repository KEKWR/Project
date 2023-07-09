from fastapi import APIRouter
from datetime import datetime
import os

from utils.script import Hash_md5



now = datetime.now()
router = APIRouter()

@router.get('/Ansible')
def makeAnsible(server_name:str):
    try:
        os.mkdir(f'sbom/')
    except:
        pass
    
    os.system(f'cd ansible && ansible-playbook playbook.yml -i hosts.txt --vault-password-file=vault.txt -e "HOST={server_name},SECRET={server_name}"')
    
    try:
        os.mkdir(f'sbom/{server_name}/{now.day}-{now.month}-{now.year}/')
    except:
        pass
    
    os.replace(f'sbom/{server_name}/sbom.json', f'sbom/{server_name}/{now.day}-{now.month}-{now.year}/sbom.json')
    return 'Sbom successfully generated'



@router.get('/indetic')
def check_indentical_sbom(server_name:str,
                          day1:str,month1:str,year1:str,
                          day2:str,month2:str,year2:str):
    if Hash_md5.get_hash_md5(f'sbom/{server_name}/{day1}-{month1}-{year1}/sbom.json') == Hash_md5.get_hash_md5(f'sbom/{server_name}/{day2}-{month2}-{year2}/sbom.json'):
        return 'Sboms are identical'
    else:
        return 'Sboms differ'