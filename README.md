# Animador de automatos

#Requisitos

Para que o projeto seja executado é necessário Python 3.8 e o gerenciador de pacotes pip.
<br>
Apesar de não ser obrigatório, é recomendável a utilização de um virtual envioriment para a intalação dos pacotes.
Além disso, é necessário de na maquina esteja instalado o Graphviz

#Instalação das dependecias
Para instalar as dependencias do projeto, basta executar o comando ```pip install -r requirements.txt``` na pasta app do projeto. 
<br>
Caso não funcione, as bibliotecas utilizadas foram a pydot (```pip install pydot```) e a Pillow (```pip install Pillow```), banta instala-las manualmente.

#Execução
Para executar o projeto, basta rodar o comando ```python main.py``` ou ```python3 main.py```, dependendo de como está configurado em sua maquina. O comando deve ser executado na pasta que contém o arquivo main.py, no caso, ela se encontra no caminho app/src/
<br>
Já existem dois arquivos de exemplos na pasta app/assets/graphs. Para adicionar um novo arquivo, basta coloca-lo na pasta e mudar a importação no arquivo app/src/file_manege.py (na primeira linha)
<br>
Quando executado, o(s) gif(s) será(ão) gerado(s) na pasta app/assets/gifs
