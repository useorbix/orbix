import os
from git import Repo, InvalidGitRepositoryError

def load_repo(path='.'):
    try:
        return Repo(path)
    except InvalidGitRepositoryError:
        print("Not a git repo. Please run inside a git repository folder.")
        exit(1)

def show_current_branch(repo):
    print(f'Current branch: {repo.active_branch.name}')

def show_latest_commit(repo):
    commit = repo.head.commit
    print(f'Latest commit: {commit.hexsha[:7]} - {commit.message.strip()} by {commit.author.name}')

def show_status(repo):
    changed_files = [item.a_path for item in repo.index.diff(None)]
    staged_files = [item.a_path for item in repo.index.diff('HEAD')]
    untracked = repo.untracked_files

    print("\nChanges not staged for commit:")
    for f in changed_files:
        print(f"  modified: {f}")
    print("\nChanges to be committed:")
    for f in staged_files:
        print(f"  staged: {f}")
    print("\nUntracked files:")
    for f in untracked:
        print(f"  {f}")

def show_commit_history(repo, n=5):
    print(f"\nLast {n} commits:")
    for commit in list(repo.iter_commits(max_count=n)):
        print(f"{commit.hexsha[:7]} | {commit.author.name} | {commit.committed_datetime.strftime('%Y-%m-%d %H:%M')} | {commit.message.strip()}")

def main():
    repo = load_repo()
    show_current_branch(repo)
    show_latest_commit(repo)
    show_status(repo)
    show_commit_history(repo)

if __name__ == "__main__":
    main()
