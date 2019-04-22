# docker-workshop

## Install docker (Ubuntu for example)
	```sudo apt-get install docker.io```

If you would like to use Docker as a non-root user, you should now consider adding your user to the “docker” group with something like:

	```sudo usermod -aG docker your-user```

## Very docker installation

	```docker version```

	```docker run hello-world```

## Create a docker image by Dockerfile
Clone the repository from Github:
	```git clone https://github.com/lotusp/docker-workshop.git```

Build the docker image:
	```docker build -t docker-workshop:tag01 .```

List images:
	```docker image ls```

Create a container using docker image **docker-workshop:tag01**:
	```docker run -d --name docker-workshop-01 docker-workshop:tag01```

Check docker container status:
	```docker container ls```

Check whether the process in docker container is working fine:
	```curl http://127.0.0.1:8080```

## Create a new base docker image
Build a new image based on python image:
	```docker build -t python-with-flask .```

Modify the Dockerfile to use new image:
	```
	FROM python-with-flask
	COPY . /app
	WORKDIR /app
	EXPOSE 8080
	CMD python ./app.py
	```

Build new image:
	```docker build -t docker-workshop:tag02 .```

Create a container using docker image **docker-workshop:tag01**:
	```docker run -d --name docker-workshop-02 docker-workshop:tag02```

Check whether the process in docker container is working fine:
	```curl http://127.0.0.1:8080```


## Install Nexus as docker registry
Reference: [https://blog.sonatype.com/sonatype-nexus-installation-using-docker]

Pull docker image of nexus:
	```docker pull sonatype/nexus```

Start docker container:
	```docker run -d --name nexus-docker-registry -p 8081:8081 -p 8082:8082 -p 8083:8083 sonatype/nexus```

## Configure nexus, configure docker registry, login, push image
Reference: [https://blog.sonatype.com/using-nexus-3-as-your-repository-part-3-docker-images]

## Push image
	```docker tag docker-workshop:tag02 127.0.0.1:8082/docker-workshop:tag02```
	```docker push 127.0.0.1:8082/docker-workshop:tag02```

## Pull image
	```docker pull 127.0.0.1:8082/docker-workshop:tag02```
