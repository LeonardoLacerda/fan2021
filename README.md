fan2021.1
Este é um projeto da disciplina de Programação para Web 2, realizado no decorrer do semestre de 2021.1 na Faculdade de Negócios - FAN.

Para inicializar o projeto, deve-se executar os seguintes comandos:
pip install -r requirements-dev.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

OBS: Caso opte por fazer a instalação no servidor de produção, deve-se utilizar o arquivo de requirements. ao invés do requirements-dev.txt