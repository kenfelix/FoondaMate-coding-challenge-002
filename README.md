# FoondaMate-coding-challenge-002

## How to start the application

The Requirement:

Install docker desktop. Follow link to know how:

    https://docs.docker.com/desktop/

The commands:

First you have to git clone the files by entering in your terminal:

    $ git clone https://github.com/AtamanKit/fastapi_users_docker.git
    $ cd FoondaMate-coding-challenge-002

Then start the application:

    $ docker-compose up -d

The above command will both create the images and start the containers (2 images and 2 containers - one for the FastAPI application and one for the MongoDB database).

For visualizing the application, open up your browser and enter:

    http://127.0.0.1:8000/docs to see the api
    http://127.0.0.1:3000 to get access to the nextjs frontend

    NOTE: frontend is not completed but all functionalities can be accessed via the API docs

To see the runing containers in docker, enter in the terminal:

    $ docker ps

To see the database and collection created (database name is: foondaMateDB, collection: user) enter in your terminal:

    $ docker exec -it <container-id> bash
