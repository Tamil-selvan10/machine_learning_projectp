## Start Machine Learning project

## Software and Account Requirements:

1. [Github Account](https://github.com/)
2. [Heroku Account](https://signup.heroku.com/)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT CLI](https://git-scm.com/downloads)
5. [Git Documentation](https://git-scm.com/docs/gittutorial)


Creating conda environment:
```
conda create -p venv python==3.9 -y
-p , --prefix , Current Directory
-n , --name   , Anaconda by default,location
-y , --yes
-m , --message
```

To activate conda environment:

```
conda activate venv/
```

or

```
conda activate D:\Python\machine_learning_projectp\venv
```

To install requirements:
```
pip install -r requirements.txt
```

To add files to git:
```
git add .
```

OR

```
git add <filename>
```

> Note: To ignore file or folder from git we can write name of file/folder in .gitignore file.

To check git status:
```
git status
```

To check all versions maintained by git:
```
git log
```

To create version/commit all changes by commit:
```
git commit -m "message"
```

To send version/changes to github:
```
git push origin main
```

To check remote url:
```
git remote -v  (remote list)
git remote add origin
git remote rm origin
```


To setup CI/CD pipeline in Heroku we need 3 information

1.HEROKU_EMAIL=
2.HEROKU_API_KEY=
3.HEROKU_APP_NAME=


To build Docker image:
```
docker build -t <image_name>:<tag_name> .
```
> Note: Image name for docker must be lower case.   

To list docker images:
```
docker images
```

To run docker image:
```
docker run -p 5000:5000 -e PORT=5000 <image_ID>
```

To check running container in docker:
```
docker ps
```

To stop docker container:
```
docker stop <container_id>
```

```
python setup.py install
```

To install ipykernel:

```
pip install ipykernel
```