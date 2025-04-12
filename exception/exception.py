

class ExistRepositoryError(Exception):
    """
    リポジトリが存在する場合に発生するエラー
    """
    def __init__(self, repository_name):
        super().__init__(f"The repository '{repository_name}' already exists. Please choose a different name.")
        self.repository_name = repository_name