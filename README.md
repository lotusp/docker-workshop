# docker-workshop

## Install docker (Ubuntu for example)
Command line:

	sudo apt-get install docker.io

If you would like to use Docker as a non-root user, you should now consider adding your user to the “docker” group with something like:

	sudo usermod -aG docker your-user

## Very docker installation

	docker version

	docker run hello-world

## Create a docker image by Dockerfile
Clone the repository from Github:

	git clone https://github.com/lotusp/docker-workshop.git

Build the docker image:

	docker build -t docker-workshop:tag01 .

List images:

	docker image ls

Create a container using docker image **docker-workshop:tag01**:

	docker run -d --name docker-workshop-01 -p 8080:5000 docker-workshop:tag01

Check docker container status:

	docker container ls

Check whether the process in docker container is working fine:

	curl http://127.0.0.1:8080

## Add a volume to save data or logs
Update app.py to print some logs:

	if __name__ == "__main__":
	    logging.basicConfig(filename='./log/app.log',level=logging.DEBUG)
	    logging.info('Hello World!')
	    app.run(host="0.0.0.0", port=int("5000"))

Build image and run:

	docker build -t docker-workshop:tag02 .

	docker run -d --name docker-workshop-02 -p 8080:5000 -v /home/maguangguang/training/docker-workshop/log:/app/log docker-workshop:tag02

## Connect to database in host machine
Update Dockerfile to run the script: db_connector.py
Build image:

	docker build -t docker-workshop-db:tag01 .

Run using host network (only work for linux):

	docker run -d --name docker-workshop-db-01 --network host docker-workshop-db:tag01

Or we can use host IP directly to access database in host machine.


## Create a new base docker image
Build a new image based on python image:

	docker build -t python-with-flask .

Modify the Dockerfile to use new image:
	
	FROM python-with-flask
	COPY . /app
	WORKDIR /app
	EXPOSE 5000
	CMD python ./app.py
	

Build new image:

	docker build -t docker-workshop:tag02 .

Create a container using docker image **docker-workshop:tag01**:

	docker run -d --name docker-workshop-02 -p 8080:5000 docker-workshop:tag02

Check whether the process in docker container is working fine:

	curl http://127.0.0.1:8080


## Install Nexus as docker registry

### Install by distribution archive file:
Reference: [https://help.sonatype.com/repomanager2/installing-and-running/installing]

Download Nexus Repository Manager OSS distribution:

	wget https://sonatype-download.global.ssl.fastly.net/repository/repositoryManager/3/nexus-3.16.1-02-unix.tar.gz

	tar xvzf nexus-3.16.1-02-unix.tar.gz

	sudo cp -rf ~/nexus-3.16.1-02 ./

	sudo ln -s nexus-3.16.1-02 nexus

	sudo ./bin/nexus start

### Install by docker image
Reference: [https://blog.sonatype.com/sonatype-nexus-installation-using-docker]

Pull docker image of nexus:

	docker pull sonatype/nexus

Start docker container:

	docker run -d --name nexus-docker-registry -p 8081:8081 -p 8082:8082 -p 8083:8083 sonatype/nexus

Note:
- 8081: the port which nexus listen on
- 8082: the port we will configure for the private docker repository
- 8083: the port we will configure for the docker repository group

## Configure nexus, configure docker registry, login, push image

Reference: [https://blog.sonatype.com/using-nexus-3-as-your-repository-part-3-docker-images]

## Push image to the private docker repository

	docker tag docker-workshop:tag02 127.0.0.1:8082/docker-workshop:tag02

	docker login -u admin -p admin123 127.0.0.1:8082

	docker push 127.0.0.1:8082/docker-workshop:tag02

## Pull image

	docker pull 127.0.0.1:8082/docker-workshop:tag02

