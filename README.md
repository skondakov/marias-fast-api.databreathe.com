# Maria's Web Service (Databreathe Backend Coding Challange)
 Databreathe's Backend Code Challange. A FastAPI Web service to retrieve some specific data from a dataset of 
 Maria's shopping outlet business. 

## Local Environment

### Requirements

* [Docker for Windows](https://www.docker.com/docker-windows), [Docker for Mac](https://www.docker.com/docker-windows)
  or [Docker for Linux](https://hub.docker.com/search?offering=community&q=&operating_system=linux). Just
  make sure you also have [Docker Compose](https://docs.docker.com/compose/) included in the package you install;
* [GitHub for Desktop](https://desktop.github.com/) or any other [Git](https://git-scm.com/) client for your OS of
  choice.

### Setup

1. Clone this repo in your local host's directory of choice;
1. Go to project's dir, open `example.env` replace all values enclosed in < and > with your values and remove the <
   and >. Then save as `.env`. (Please make sure that the file is saved EXACTLY as `.env` and not `.env.env`
   , `something.env`, etc.);
1. Run `docker-compose up -d api-server` to start the API server. This will download, build and run all the needed
   docker images, download & setup all app dependеnсies, import & setup a copy of the database. The API app should
   then be started. (NOTE: if you get `ERROR: The Compose file './docker-compose.yml' is invalid`, make sure you
   have set `.env` file properly and it is in the same dir as `docker-compose.yml`);
1. The API should respond here [http://localhost:5057/](http://localhost:5057/). 
   You can check if the API is working by accessing this: [http://localhost:5057/ping](http://localhost:5057/ping)

### Usage

* **Start the API Server:** Run `docker-compose up -d api-server` from the root of your project's working dir.
* **Stop All Services:** Run `docker-compose down` from the root of your project's working dir.
* **Update code:** When the web app is started you can freely update code and see the results right away in your
  browser. Same goes for the API.
* **Access the DB with a MySQL client:** You can access the application's database with the MySQL credentials you provided 
  in the `.env` file on **localhost**
* **Recreate local DB:** Call `docker-compose down -v` and after it's finished, call `docker-compose up -d api-server`
  from the root of your project's working dir. 
* **How to get into a docker container?:** Sometimes you need to connect to the container to do some job directly. In
  order to do this you must first execute `docker ps` to see all currently running containers, and then
  execute `docker exec -it <container name> bash`. To exit you must simply type `exit`, followed by enter.
* **How to rebuild a docker container?:** It is a good practice to rebuild the docker containers you use to make sure
  you always work with the same environment as everywhere else. You can do this
  with `docker-compose build --no-cache <container name i.e. api-server>`
* **How to run the unit tests?:** In order to run the unit tests you would need to run the api server first.
  You can do this by running `docker-compose up -d api-server`. Then you have to run `pytest test_api.py` from the project's 
  root dir in order to run the unit tests.