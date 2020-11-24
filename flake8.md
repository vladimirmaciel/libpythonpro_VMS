# Flake8
Biblioteca que vai conferir se o código esta de acordo com as boas práticas da 
pep8
para instalar pip install flake8

 pip freeze  > requirements-dev.txt (para os desenvolvedores)
 adiconar dentro de requirements-dev.txt 
-r requirements.txt

ao montar o ambiente de desenvolvimento rodar o comando 
pip isntall -r requiremenst-dev.txt
feito isso rodar o comando 
flake8 para verificar se esta de acordo com as boas práticas 
criar um arquivo na raiz do prjeto chamado .flake8(evita que o comando analise todo o projeto)