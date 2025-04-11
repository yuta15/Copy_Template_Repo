import git
import github
import os
from mods.setting import setting

repository = git.Repo.init('../test')
# remote = repository.create_remote(name="origin", url='https://github.com/yuta15/test6.git')
index = repository.index
# remote.pull('main')
os.chdir('../test')
with open('.git/config', 'r') as f:
    config = f.readlines()
if '[remote "origin"]\n' in config:
    remote = repository.remote('origin')
    print('exists')
else:
    remote = repository.create_remote('origin', url=f'https://github.com/yuta15:{setting.GITHUB_TOKEN}/test6.git')
    print('not exists')
remote.pull('main')
print(repository.active_branch.name)


with open('test.py', 'w') as f:
    f.write('test')



index = repository.index
index.add(["test.py"])
index.commit("Add files")
remote.push(repository.active_branch.name)

g = github.Github(setting.GITHUB_TOKEN)
user = g.get_user()
repos = user.get_repos()
fetched_repo_names = [repo.name for repo in repos]
print(fetched_repo_names)