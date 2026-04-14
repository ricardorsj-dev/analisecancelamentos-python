import pandas as pd

#criando a tabela para ser lida pelo python 
tabela = pd.read_csv("ClientesBanco.csv", encoding = "latin1")

#mostra o conteudo da tabela
#o head deixa o código mais limpo, mostrando só cinco primeiras linhas
tabela.head()

#tratamento de dados vazios
#exclusão destes dados
#na = not a number 
tabela = tabela.dropna()
tabela.info()

#descrição dos dados do arquivo
tabela.describe().round(1)

#analise das causas de cancelamento
#escolha de uma coluna para saber se ela impacta no meu negocio 
#comparaçao entre a coluna a ser analisada com a coluna que diz se a pessoa é cliente ou cancelado
import plotly.express as px 

#o histograma vai analisar a tabela criada
#todo grafico tem dois eixos para comparar
#eixo x será uma coluna e o eixo y outra coluna 
#o color irá separar as cores para ver a proporção de cancelamentos de acordo com os contatos feitos
grafico = px.histogram(tabela, x= "Contatos 12m", color="Categoria")
grafico.show()


#analise de cancelamento comparando as colunas idade e categoria
grafico = px.histogram(tabela, x= "Idade", color="Categoria")
grafico.show()


#analise do cancelamento comparando as colunas limite e categoria
grafico = px.histogram(tabela, x= "Limite", color="Categoria")
grafico.show()


#analise do cancelamento comparando colunas categoria cartao e categoria
grafico= px.histogram(tabela, x="Categoria Cartão", color="Categoria")
grafico.show()

#analise do cancelamento comparando colunas faixa salarial anual e categoria
grafico=px.histogram(tabela, x="Faixa Salarial Anual", color="Categoria")
grafico.show()

#analise do cancelamento comparando colunas produtos contratados e categoria
grafico=px.histogram(tabela, x="Produtos Contratados", color="Categoria")
grafico.show()













