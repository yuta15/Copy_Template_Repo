import os
import yaml
import json
from github import Github

from mods.read_params import read_params
from mods.setting import setting
from mods.set_docker_compose import set_docker_compose


g = Github(setting.GITHUB_TOKEN)
user = g.get_user()
repo = user.get_repo(
    'test6'
)

print(repo.html_url)
