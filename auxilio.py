import pandas as pd 

tabela1 = pd.read_csv("funcionarios_brasil_150.csv")
print(tabela1)

#   EXPLANAÇÃO DA TABELA DE FUNCIONÁRIOS 


#         Nome  Sobrenome  ... ID da Empresa                     Cargo
#0       Lucas      Silva  ...          1001              Social Media
#1     Mariana     Araújo  ...          1002              Social Media
#2       Pedro    Azevedo  ...          1003  Coordenador de Logística
#3      Renata      Alves  ...          1004     Assistente de Compras
#4      Camila  Rodrigues  ...          1005      Analista de Sistemas
#..        ...        ...  ...           ...                       ...
#145   Matheus      Gomes  ...          1146          Assistente de RH
#3146  Carolina   Teixeira  ...          1147     Analista de Operações
#3147  Henrique   Nogueira  ...          1148      Analista de Sistemas
#148    Marcos     Araújo  ...          1149         Gerente Comercial
#149    Marcos    Martins  ...          1150             Desenvolvedor