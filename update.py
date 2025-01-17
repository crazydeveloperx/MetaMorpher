from subprocess import run as srun
from os import path as ospath, getcwd, execl as osexecl
from sys import executable

UPSTREAM_REPO = 'https://github.com/harsha7668/metabor'
UPSTREAM_BRANCH = 'SH24BOTS-GD-REVERSION-GRP'

# Debugging Information
print("Current working directory:", getcwd())

if UPSTREAM_REPO is not None:
    if ospath.exists('.git'):
        srun(["rm", "-rf", ".git"])
        print("Removed existing .git directory.")

    # Run git commands
    update = srun([
        f"""
        git init -q &&
        git config --global user.email "sunriseseditsoffical249@gmail.com" &&
        git config --global user.name "metamorpher" &&
        git add . &&
        git commit -sm "update" -q &&
        git remote add origin {UPSTREAM_REPO} &&
        git fetch origin -q &&
        git reset --hard origin/{UPSTREAM_BRANCH} -q
        """
    ], shell=True)

    # Check for update success
    if update.returncode == 0:
        print("Git update successful. Restarting bot.py...")
        bot_path = ospath.join(getcwd(), "bot.py")  # Ensure bot.py is in the current directory
        if ospath.exists(bot_path):
            osexecl(executable, executable, bot_path)
        else:
            print(f"bot.py not found in directory: {getcwd()}")
    else:
        print('Something went wrong while updating. Check UPSTREAM_REPO or branch name.')

# Fallback execution
bot_path = ospath.join(getcwd(), "bot.py")
if ospath.exists(bot_path):
    osexecl(executable, executable, bot_path)
else:
    print(f"bot.py not found in directory: {getcwd()}")
