import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="selecione uma pasta") #aqui a variável vai receber o caminho da pasta que vc irá selecionar. Ou seja, a pasta que vc irá organizar

lista_arquivos = os.listdir(caminho) #aqui a variável vai listar todos os arquivos que tem dentro da pasta a qual vc disse o caminho. O argumento é a variável caminho

locais = {"Planilhas": [".xlsx"], "PDF": [".pdf"], "Documentos":[".docx"]} #aqui está sendo criada as pastas(chaves) e dentro delas será guardada o tipo de arquivo(valores)

for arquivo in lista_arquivos: #a variável arquivo do for é o arquivo que existe dentro da pasta 
   nome, extensao = os.path.splitext(f"{caminho}/{arquivo}") #a variável nome é o caminho inteiro + nome do arquivo e a variável extensão é .extensao
   for pasta in locais:
      if extensao in locais[pasta]:
         if not os.path.exists(f"{caminho}/{pasta}"):
            os.mkdir(f"{caminho}/{pasta}") #criar uma pasta
         os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}") #aqui os arquivos estão sendo colocados na nova pasta  