# IoT using Machine Learning
Lapisco Trainne - Módulo 6

## Questão 01
Quando o modelo é carregado fora do endpoint, é carregada como variável global, sendo assim possível de utilizar em mais de uma rota, no entanto, se for carregada dentro de uma rota terá um maior custo do tempo para requisitar o modelo.

## Questão 02 e 04

## Questão 03 e 05
1. The resolution of the questions is in the FastAPI folder -> src -> main.py;

2. If necessary, download requirements.txt;

3. How to build 

    cd src

    sudo docker-compose buil

4. How to run
    
    cd src

    sudo docker-compose up
    
5. Copy .env-example file and rename it as .env because docker-compose will look for environment variables.

Important: On Linux I used "sudo docker", because I didn't configure the docker to be used without sudo, but if you don't need it on your computer, just remove it.

## Questão 06
