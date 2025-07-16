import os


def is_on_github_actions():
    if os.getenv("GITHUB_ACTIONS"):
        return True
    else:
        return False
