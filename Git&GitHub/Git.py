import pandas as pd
import cv2
import matplotlib.pyplot as plt
# Git :- It is a software. Git is a distributed version control system .
# what is vcs(version control system)/scm(source contol manager)
"""
A Version Control System (VCS), also called Source Control Management (SCM), 
is a software tool that tracks changes made to files (especially source code) over time.
It allows you to:
Save different versions of your code.
See who made changes and when.
Restore previous versions if something breaks.
Work with multiple developers without overwriting each other's code.
"""
# Why is VCS/Git Needed?
"""
Problems:-
Which file is the latest?
Who changed what?
How do you undo a mistake?
What if your laptop crashes?
Very difficult to manage.
Advantage:-
1. Tracks History
2. Backup
3. Collaboration
4. Undo Mistakes
5. Branching
6. Team Collaboration
"""
# Difference Between Git and GitHub
"""
Git	                                            GitHub
Version control software	            Cloud hosting platform
Installed on your computer	            Runs online
Tracks code history	                    Stores Git repositories online
Works offline	                        Requires internet for remote operations
"""
# working directory :- jha pa code likhta hai.
# staging index :- jha pa aap code rkhta hoa commit krna k liya
# commit:- A commit is a saved snapshot of your project at a specific point in time.
# Repository :- A repository (repo) is a storage location where your project and its complete version history are kept.
# Step to copy repo :
"""
1. Go on repository
2. Copy repo link
3. Open Git Bash
4. type "git clone" and then paste the link.
"""
# git status 
# step to commit 
# Go in the repo directory 
# git status :- to check what you have to do
# git add . (ready to commit)
# gitignore :- if you do not want to make chnages in that file.
# git status
# git commit -m "message"
# git push :- to push on git hub

"""
Scenario 1: Local development only

If you're working only on your own computer:

git add .
git commit -m "Updated Git.py"

That's enough.

Your commit is safely stored in your local Git repository.

Scenario 2: You want the changes on GitHub

Then you must do:

git add .
git commit -m "Updated Git.py"
git push

Without git push, GitHub will not receive your new commit.
"""

# seeing commits :- 
# if you want to see how many commits you done then use :- git log
# if you only want summary commit :- git log --oneline

# git -stat
# git -p :- show all changes made in whole file
# git show (put first 6 sah value) :- show code of specific file

# diff :- commit sa phla kuch changes hua hai to ya apko bta deta hai, commit kiya bina
# git diff


# Creating a versions of a software
"""
-tag --> X,Y,Z
X -> The major version,used for making major and backward-incompatible changes.
Y -> The minor version,used for adding functionality while maintaining backwards compatibility.
Z -> The patch version, used for making small bug fixes while maintaining backwards compatibility.

"""

# adding tag
# git tag -a v1.0.0 (tag name) then vin editor will open
# to insert the tag press :- fn+insert
# exit insert by pressing esc and then save by typing wq
# to delete the tag := git tag -d (tag name)
# to create tag in previous commit :- git tag -a v1.0.0 (sash)

# Non-Linear development(Branching)

# If we want to develop 2 features in parallel then we use branching

branching = cv2.imread("C:\Users\prana\OneDrive\Pictures\Screenshots\Screenshot 2026-07-21 151326.png")
plt.imshow(branching)
