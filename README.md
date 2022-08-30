# BDD com Selenium



### Para rodar o app, basta seguir os passos abaixo

Utilizando o terminal, acesse a raiz do projeto
Rode o comando:
```
$ python3.10 -m venv env
```

(Altere a versão do Python para a que esteja instalada em seu sistema)
 
Em caso de dúvida rode:
``` 
$ python --version
```
Em seguida execute o comando
```
$ source env/bin/activate
```
Isso iniciará uma ambiente virtual em sua máquina, evitando que os pacotes que serão instalados entrem em conflito com os demais pacotes do seu sistema.

Em seguida execute
```
$ pip install -r requirements.txt
```

#### Verifique a versão do Chrome instalado em sua máquina.

- O WebDriver dispobilizado neste projeto é compatível com a versão `104`.

Caso a versão em seu sistema seja diferente, entre no site do [Chromium](https://chromedriver.chromium.org/downloads) e baixe a versão compatível.

Após baixar, coloque o arquivo `chromedriver` na pasta `features/resources/`.

#### Em seguida rode as migrations e crie um usuário
```
$ python manage.py migrate
$ python manage.py createsuperuser
```
Acesse o arquivo `features/steps/app_tests.py`

Insira o usuário e senha criados nas constantes:

> USUARIO
> 
> SENHA

No terminal, vá para a raiz do projeto e execute o comando:
```
$ python manage.py runserver
```
Abra outra aba do terminal, ainda na raiz do projeto, e execute:
```
$ behave
```
