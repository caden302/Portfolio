from git import Repo
import json

class GitHubUploader:
    def __init__(self, repo_path, fileName):
        self.repo_path = repo_path
        self.repo = Repo(self.repo_path)
        self.fileName = fileName

    def update_json(self, data):
        try:
            with open(self.fileName, "w") as f:
                json.dump(data, f, indent=2)
        except IOError as e:
            print(e)

    def testUploader(self):
        print(self.repo)
        pass

    def pushToGitHub(self):
        if self.repo.is_dirty(untracked_files=True):
            self.repo.git.add(self.fileName)
            self.repo.index.commit("Auto update Steam stats")
            self.repo.remote(name='origin').push()
        else:
            print("Nothing to push")
    