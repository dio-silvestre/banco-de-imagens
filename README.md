# Banco de Imagens

Suporta diferentes tipos de arquivos e permite fazer upload e download desses arquivos.

<br>

## Como instalar e rodar? 🚀

Para instalar o sistema, é necessário seguir alguns passos, como baixar o projeto e fazer instalação das dependências. Para isso, é necessário abrir uma aba do terminal e digitar o seguinte:

    #Este passo é para baixar o projeto
    git clone https://github.com/dio-silvestre/banco-de-imagens.git

Depois que terminar de baixar, é necessário entrar na pasta, criar um ambiente virtual e entrar nele:

    #Entrar na pasta
    cd banco_de_imagens

    #Criar um ambiente virtual
    python -m venv venv --upgrade-deps

    #Entrar no ambiente virtual
    source venv/bin/activate

Então, para instalar as dependências, basta:

    pip install -r requirements.txt

Para rodar, basta digitar o seguinte, no terminal:

    flask run

E o sistema estará rodando em `http://127.0.0.1:5000/`

## Utilização 🖥️

Para utilizar este sistema, é necessário utilizar um API Client, como o [Insomnia](https://insomnia.rest/download)

### Rotas

### ![POST](https://i.imgur.com/Qhk9miC.png) UPLOAD FILE

```
/upload
```

Esta rota será enviado um arquivo por um Multipart Form nomeado "file", com o valor sendo o arquivo a ser enviado;

`RESPONSE STATUS -> HTTP 201 (created)`


#### ![GET](https://i.imgur.com/zH6h6cZ.png) FILES LIST

```
/files
```

Esta rota lista todos os arquivos.

`RESPONSE STATUS -> HTTP 200 (ok)`


#### ![GET](https://i.imgur.com/zH6h6cZ.png) FILES BY EXTENSION

```
/files/<extension>
```

Esta rota lista os arquivos de um determinado tipo;

`RESPONSE STATUS -> HTTP 200 (ok)`


#### ![GET](https://i.imgur.com/zH6h6cZ.png) DOWNLOAD BY FILE NAME

```
/download/<file_name>
```

Esta rota é responsável por fazer o download do arquivo solicitado em file_name;

`RESPONSE STATUS -> HTTP 200 (ok)`


#### ![GET](https://i.imgur.com/zH6h6cZ.png) DOWNLOAD ZIP

```
/download-zip?file_type=<extension>&compression_rate=<1/9>
```

Esta rota é necessário passar com com query_params (file_extension, compression_ratio) para especificar o tipo de arquivo para baixar todos compactados e também a taxa de compressão, sendo a segunda opcional pois por padrão é 9.

###### rota recomendada a ser testada pelo navegador

`RESPONSE STATUS -> HTTP 200 (ok)`


## Tecnologia utilizada 📱

- Flask

## Licence

MIT
