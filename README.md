# Apprentice-Website
This is a website project created by the apprentices who joined Land Registry in October 2016, ready for next years apprentices.
This document will give the people working on this project.

# Git Commands

    $ git status
Viewing the changed files in your working directory.

    $ git diff

Viewing tracked file changes

    $ git add. 
    
Add all current changes to the next commit.

    $ git add -p <file:

 Add some changes that was created in the files to the next commit. 
 
    $ git commit -a:
 
  Commit all local changes in tracked files.

# Branches
    $ git branch -av
    
   This command list all the existing branches in the repository
  
    $ git checkout <branch-name>
  
  This command points the branch that you want to work on, in your working directory (HEAD Branch)
  
    $ git branch <new-branch>  
    
  This command creates a new branch in the repository.
  
    $ git checkout --track <remote/branch>
   
   This command creates a new tracking branch based on a remote branch.
   
    $ git branch -d <branch>
   
   This command deletes a branch locally.
   
# Update and Publish
    $ git remote -v
 This command shows all the configured remotes linked to your local repository. Eg github. This is an example:
 
    $ git remote -v
    origin  https://github.com/LR-Apprentices/Apprentice-Website.git (fetch)
    origin  https://github.com/LR-Apprentices/Apprentice-Website.git (push)

    $ git remote origin
 
 Shows information about the remote repositorys stored online. Here is an example of the output of our repo.
   
        * remote origin
        Fetch URL: https://github.com/LR-Apprentices/Apprentice-Website.git
        Push  URL: https://github.com/LR-Apprentices/Apprentice-Website.git
         HEAD branch: master
         Remote branches:
    Alex                                 tracked
    Annas-branch                         tracked
    Jess                                 tracked
    Lukes-Branch                         tracked
    master                               tracked
    refs/remotes/origin/ALuffy87-patch-1 stale (use 'git remote prune' to remove)
    Local branches configured for 'git pull':
    Jess         merges with remote Jess
    Lukes-Branch merges with remote Lukes-Branch
    master       merges with remote master
     Local refs configured for 'git push':
    Jess         pushes to Jess         (up to date)
    Lukes-Branch pushes to Lukes-Branch (up to date)
    master       pushes to master       (up to date)
        
Hopefully that should give you more of an idea.

    $ git remote add <shortname> <url>
               


Adds new remote repository. For example, if you had the same stuff saved on gitlab, you can add it.

    $ git push

Pushes all of the commits from the staging area to the remote repo. In our case it is Github.


