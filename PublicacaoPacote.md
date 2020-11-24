#Publicação de Pacote 

Arquivo Setup.py
Instalação Local de Pacote
Criação de Release
Publicação no PyPi
Upgrade de Lib no PyPi
Conclusão - Construção de Projetos

criar um abimente virutal e instala o pacote com o seguinte comando 

pip install -e <diretório>

vai ler o arquivo setup.py e instalar o projeto com todas as suas dependencias
para testar rodar o comandos abaixo: 
>>> from libpythonpro.github_api import buscar_avatar
>>> buscar_avatar('vladimirmaciel')
'https://avatars1.githubusercontent.com/u/606140?v=4'

comando para criação de release 

git tag <nome-da-tag>
git push --tags
pip install <link> 