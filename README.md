# Manga Downloader

Este é um script em Python que baixa mangás de um site fornecido.

## Pré-requisitos

- Python 3.x instalado
- Bibliotecas Python necessárias, que podem ser instaladas através do comando: `pip install -r requirements.txt`

## Configuração

Antes de executar o script, é necessário configurar o driver do Chrome e criar as pastas necessárias. Siga os passos abaixo:

1. Faça o download do driver do Chrome compatível com a sua versão do Chrome e sistema operacional.

2. Coloque o arquivo do driver na mesma pasta do script.

## Uso

1. Execute o arquivo `main.py`.

2. Insira o nome do mangá que deseja baixar.

3. Insira a URL do site que contém o mangá. 

4. O script irá baixar os capítulos do mangá e salvá-los na pasta tendo o nome do Manga e todos os seus capitulos em ordem decrescente.

## Observações

- Certifique-se de ter uma conexão com a internet para que o script funcione corretamente.

- Se ocorrerem erros durante o download das páginas do mangá, verifique a conexão com o site ou tente novamente mais tarde.

- O script irá criar um arquivo zip para cada capítulo baixado na pasta. O arquivo zip conterá todas as páginas do capítulo.

- Os arquivos de imagem das páginas serão excluídos após a criação do arquivo zip para economizar espaço em disco.

- Certifique-se de ter permissões de escrita na pasta onde o script está sendo executado.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request com melhorias, correções de bugs, ou novos recursos.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
