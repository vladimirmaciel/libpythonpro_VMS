# libpythonpro
Módulo para exemplificar construção de projetos Python no curso PyTools
Isolando o Ambiente 
 O Pyenv possibilita ter multiplas versoes do python instaldas no sistema operacional, preservando a versão original do sistema e suas dependencias. 

 * instalando as ferrmantas necessárias para o python fazer o build 
   - sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm gettext libncurses5-dev tk-dev tcl-dev blt-dev libgdbm-dev git python-dev python3-dev aria2 vim libnss3-tools python3-venv liblzma-dev
 
   - para instalar o pyenv executar o comando abaixo : 
       curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
   - para ativar o pyenvv automaticamente add as linhas abaixo: 
      Editar no arquivo .bashrc:
      vim .bashrc
      add no final do arquivo 
      export PATH="~/.pyenv/bin:$PATH"
      eval "$(pyenv init -)"
      
      
      executar o comando pyenv para verficiar se foi instalado 
      para conferir a lista de todos os interpretadores 
         pyenv install -l
      É possivel instalar duas versoes do python neste caso será a mais atual da versão três e da versão 2 
        pyenv install 3.8.5 
        pyenv install 2.7.18 
        pyenv version -- conferir as versoes instaladas 
        pyenv global + versao do python para definir como golal (pode setar varias versoes de python) 
        which python mostra exatamente o python do pyenv 
    
  Instalar o virutalenv no Linux(Ubuntu) 
      virtualenv -- 
      esta forma é utilizada no python3 
      versão 3 do python + modulo a ser executado venv + nome da pasta onde vai ser colocado o virtualenv(pode ser qualquer nome) 
      python3 -m venv .ven
      para ativar o ambiente virutal
      source .venv/bin/activate (o prompt  é modificado e na frente fica o nome da pasta criada)
      utizando o comando which python  possível verificar de onde o python esta sendo executado 
      para desativar o virtualenv é só utilizar o comando deactivate, o prompt volta para a versão original,execuntando o comando which python é possivel verificar  que o diretorio do python é o do pyenv que foi instalado no passo anterior 
      
      
