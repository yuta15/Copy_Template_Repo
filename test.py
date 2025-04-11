import git

repository = git.Repo.init('../test')
# remote = repository.create_remote(name="origin", url='https://github.com/yuta15/test6.git')
index = repository.index
# remote.pull('main')
print(repository.branches)