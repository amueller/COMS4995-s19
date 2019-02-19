from github import Github
import tqdm
import shutil
from os import listdir
import os
from glob import glob
import shlex
import mosspy


# TODO: use absolute paths everywhere...
# FIXME clone_repos changes path = global state WTF?!
# usage:
# clone_repos(pattern="homework-3", store_at="/home/andy/Dropbox/columbia_safe/applied_machine_learning_spring_2018/submissions_hw3/")
# convert_notebooks()
# m, url = submit_moss()
# mosspy.download_report(url, "hw1_report/", connections=8, log_level=20)

def clone_repos(pattern="homework-1", store_at="/tmp/homework"):
    if not os.path.exists(store_at):
        os.mkdir(store_at)
    os.chdir(store_at)

    with open("/home/andy/Dropbox/documents/accounts/github_moss_token.txt") as f:
        token = f.read().strip()

    g = Github(token)
    org = g.get_organization("applied-ml-spring-18")
    repos_list = org.get_repos()
    these = [repo for repo in repos_list if pattern in repo.full_name]
    for repo in tqdm.tqdm(these):
        #print(repo.ssh_url)
        if not os.path.exists(repo.name):
            os.system("git clone --depth 1 {}".format(repo.ssh_url))
    for repo in repos_list:
        try:
            l = listdir(repo.name)
        except FileNotFoundError:
            #print(repo.name)
            continue
        if len(l) < 2:
            # has .git folder
            shutil.rmtree(repo.name)
    return repos_list

def convert_notebooks():
    notebooks = glob("*/*.ipynb")
    for notebook in tqdm.tqdm(notebooks):
        #print(notebook)
        if not os.path.exists(notebook.replace("ipynb", "py")):
            os.system("jupyter-nbconvert {} --to script".format(shlex.quote(notebook)))
            
def submit_moss(location="/tmp/homework/"):
    import mosspy

    userid = 273660752

    m = mosspy.Moss(userid, "python")
    m.setDirectoryMode(1)

    m.addFilesByWildcard(os.path.join(location, "*/*.py"))
    m.addFilesByWildcard(os.path.join(location, "*/*/*.py"))


    url = m.send() # Submission Report URL

    print ("Report Url: " + url)
    return m, url