#dataframe - tabela no python
import pandas as pd 
vendas = {'data': ['15/02/2021', '16/02/2021'], 'valor': [500, 300], 'produto': ['feijao', 'arroz'], 'qtde': [50, 70]} #dicionário
df = pd.DataFrame(vendas) #basta colocar o nome do dicionário dentro dos parenteses
display(df)
print(df)