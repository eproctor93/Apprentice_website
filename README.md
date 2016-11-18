# Apprentice-Website


#Git-Help

How to link a folder to github (make sure git/git bash is installed)

To start we will make a seperate folder (name of your choice) once done open git bash by right-clicking in the folder you just made and click the Git Bash here and write the following codes

```
$ git init
```

this creates a local repo

or type

```
$ git clone https://github.com/LR-Apprentices/Apprentice-Website.git
```

this will clone a repository from github's master branch to your local folder

now we want to make a branch
to do this we will type

```
$ git checkout -b 'insert name'
```

so now the folder will represent that branch

we will now want to learn how to commit the branch and push it to the website so it knows about the branch
to do this type

```
$ git status
```

this shows you all the changes made
to add them to the commit type

```
$ git add .
```
alternatively you can add a single file by typing
```
$ git add filename.txt
```

now we will check the status again

```
$ git status
```
this is so that we know if it has it added
now to commit it
type

```
$ git commit -m "Enter a message that represents the changes"
```

now we want to push the file to the website to do this type
```
$ git push
```

if this doesnt work this may be because you will need to type
```
$ git push --set-upstream origin flask-app
```
now it should have pushed to the website including your new branch
