import git
import github
import os
import sys
from mods.setting import setting

os.chdir('/home/anzai/Actions/test')
if not '.git' in os.listdir():
    repository = git.Repo.init()
else:
    repository = git.Repo()
index = repository.index
with open('.git/config', 'r') as f:
    config = f.readlines()
if '[remote "origin"]\n' in config:
    remote = repository.remote('origin')
    print('exists')
else:
    remote = repository.create_remote('origin', url=f'https://{setting.PERSONAL_TOKEN}@github.com/yuta15/test_repo4.git')
    print('not exists')
print(repository.head.is_valid())
print(os.getcwd())
print(os.listdir())
print(repository.active_branch.name)
remote.pull('main')
print(repository.head.is_valid())

with open('test12.py', 'w') as f:
    f.write('test12')
    
    
index.checkout()

print(os.getcwd())
print(os.listdir())
index.add('*')
print(os.getcwd())
print(os.listdir())
index.commit("Add files")
print(os.getcwd())
print(os.listdir())
