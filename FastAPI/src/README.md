## Iris Classifier FastAPI

On Linux I used "sudo docker", because I didn't configure the docker to be used without sudo, but if you don't need it on your computer, just remove it.

### How to build
    cd src
    sudo docker-compose build

### How to run
    cd src
    sudo docker-compose up

Important: there is a .env-example. Copy this file and rename it as .env. because docker-compose will look for environment variables.

