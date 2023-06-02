import os
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import zipfile

from config_driver import chrome_driver
from cria_pastas import pasta_capitulo

def main():
    
    nome_manga = input("Digite o nome do Manga: ")
    url = input("Insira a URL do Site: ")
    
    driver = chrome_driver()
    
    #Configuracao Headers
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
   
    #URL o qual sera trabalhada
    response = requests.get(url, headers=headers)
    html_content = response.content
    
    #Objeto Bfsoup para HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    
    #Pesquisa a quantidade de titulos/O texto dos capitulos
    titulos_id = soup.find(id='capitulos')
    classes_titulos = titulos_id.find_all(class_='button')
    classes_titulos.reverse()
    
    print('Quantidade de Titulos:', classes_titulos.reverse())
    
    capitulos = {}
    
    for classe_titulo in classes_titulos:
        link = classe_titulo['href']
        titulo = classe_titulo.text
        capitulos[titulo] = link
        
    for titulo, link in capitulos.items():
        
        driver.get(link)
        
        diretorio = pasta_capitulo(titulo, nome_manga)
        
        elemento_paginas = driver.find_element(By.CSS_SELECTOR, '.u-pull-right select.images')
        paginas = elemento_paginas.find_elements(By.TAG_NAME, 'option')
    
        quantidade_paginas = len(paginas)
        print('Titulo Atual:', titulo)
        print('Quantidade de páginas:', quantidade_paginas)
        
        imagens = []
        
        for quantidade_pagina in range(1, quantidade_paginas + 1):
        
            url_pagina = str(link) + "#" + str(quantidade_pagina)
            driver.get(url_pagina)
            
            elemento_image = driver.find_element(By.ID, f'img_{quantidade_pagina}')
            src_imagem = elemento_image.get_attribute('src')
            nome_arquivo = f"pagina_{quantidade_pagina}.jpg"
            print('Pagina Atual:', quantidade_pagina)
            response = requests.get(src_imagem, headers=headers)
        
            if response.status_code == 200:
                caminho_arquivo = os.path.join(diretorio, nome_arquivo)
                with open(caminho_arquivo, "wb") as arquivo_imagem:
                    arquivo_imagem.write(response.content)
                imagens.append(caminho_arquivo)
                
            else:
                print(f"Erro ao baixar página {quantidade_pagina}. Status code: {response.status_code}")
        
        if imagens:
            zip_output = os.path.join(diretorio, f"Capitulo_Completo_{titulo}_.zip")
            
        with zipfile.ZipFile(zip_output, 'w') as zip_file:
            for imagem in imagens:
                zip_file.write(imagem, os.path.basename(imagem))
                    
        for imagem in imagens:
            os.remove(imagem)
        
        print("Titulo Finalizado!")
        
if __name__ == '__main__':
    main()