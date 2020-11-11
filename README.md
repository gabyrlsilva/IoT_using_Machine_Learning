# IoT using Machine Learning - Lapisco Trainne - Módulo 6

## Questão 01
Quando o modelo é carregado fora do endpoint, é carregada como variável global, sendo assim possível de utilizar em mais de uma rota, no entanto, se for carregada dentro de uma rota terá um maior custo do tempo para requisitar o modelo.

## Questão 02 e 04
 - Django 2.0
    
    1. A pasta [Django_2_0](https://github.com/gabyrlsilva/IoT_using_Machine_Learning/tree/main/Django_2_0) é onde se encontra todos os códigos necessários para resolver essa questão, o código principal [views.py](https://github.com/gabyrlsilva/IoT_using_Machine_Learning/blob/main/Django_2_0/main/views.py) está dentro da pasta main 
    
    2. Se necessário, fazer download do requirements.txt
    
    3. Para construir um docker-compose da aplicação é necessário (Folder: Django_2_0):
    
           sudo docker-compose build
        
    4. Para executar o docker-compose da aplicação é necessário (Folder: Django_2_0):
    
           sudo docker-compose up
    
    5. Copie o arquivo env-example e remoneie .env, porque o docker-compose irá analisar as variáveis de ambiente.
 ------------------------------------------------------------------------------------------------------------------------------------------------------------
    
 - Django Rest Framework


## Questão 03 e 05

1. O caminho para encontrar o código principal é [FastAPI -> src](https://github.com/gabyrlsilva/IoT_using_Machine_Learning/tree/main/FastAPI/src) -> main.py;
    
2. Se necessário, fazer download do requirements.txt
    
3. Para construir um docker-compose da aplicação é necessário (Folder: Django_2_0):
    
        cd src
        sudo docker-compose build
        
4. Para executar o docker-compose da aplicação é necessário (Folder: Django_2_0):

        cd src
        sudo docker-compose up
    
5. Copie o arquivo env-example e remoneie .env, porque o docker-compose irá analisar as variáveis de ambiente.

## Questão 06

1. O caminho para encontrar o código principl (main) é [Churn_detector](https://github.com/gabyrlsilva/IoT_using_Machine_Learning/tree/main/Churn_detector);

2. Se necessário, fazer download do requirements.txt;

3. Para construir um docker-compose da aplicação é necessário:
    
        cd src
        sudo docker-compose build
        
4. Para executar o docker-compose da aplicação é necessário:

        cd src
        sudo docker-compose up
    
5. Copie o arquivo env-example e remoneie .env, porque o docker-compose irá analisar as variáveis de ambiente.

----------------------------------------------------------------------------------------------------------------------------------------------------------------
Importante: No Linux, eu digito "sudo docker-compose...", porque eu não configurei para usar o docker sem o sudo, mas caso seu computador não necessite, é apenas remover isso. 

**Observação:** Caso a porta 8000 esteja sendo utilizada, inserir *sudo lsof -i:8000* para encontrar o container que está utilizando a porta, em seguida *kill <ID processo>*.
