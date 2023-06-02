import os

def pasta_capitulo(titulo, nome_manga):
    

    pasta = nome_manga
    if not os.path.exists(pasta):
      os.makedirs(pasta)
    
    pasta_capitulo = os.path.join(pasta, titulo)
      
    if not os.path.exists(pasta_capitulo):
      os.makedirs(pasta_capitulo)
      
    return pasta_capitulo