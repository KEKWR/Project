from fastapi import APIRouter
import os

router = APIRouter()

@router.get("/create_vaultfile")
def create_vaultfile(password:str):
    os.system(f'cd ansible/ && echo "{password}" >> vault.txt && chmod 600 vault.txt')


@router.get('/Add_new_server')
def add_new_server(server_name:str,server_ip:str,username:str,user_pass:str):
    #user must be sudo
    f = open('ansible/hosts.txt','a')
    f.write(f'{server_name} ansible_host={server_ip} ansible_user={username} ansible_ssh_privat_key_file=ssh_key \n')

    f = open('./ansible/vault.txt')
    vault_pass = f.readline()

    os.system(f'cd ansible/ && echo "ansible_sudo_pass: {user_pass}" >> {server_name}')
    os.system(f'utils/makesecret.exp ./ansible/{server_name} {vault_pass}')