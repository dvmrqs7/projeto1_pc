import math
import random
import datetime
import statistics
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

#ENTRADAS
capital = float(input('Capital inicial:'))
aporte = float(input('Aporte mensal:'))
meses = int(input('Prazo em meses:'))
cdi_anual = float(input('CDI anual em %:')) / 100
perc_cdb = float(input('Percentual do CDI (%):'))/ 100
perc_lci = float(input('Percentual do LCI (%):')) / 100
taxa_fii = float(input('Rentabilidade mensal FII (%):')) / 100
meta = float(input('Meta financeira (R$):'))

#CONVERSÃO CDI
cdi_mensal = math.pow((1+cdi_anual),1/12) -1

#TOTAL INVESTIDO
total_investido = capital + (aporte*meses)

#CDB
taxa_cdb = cdi_mensal * perc_cdb
montante_cdb = (capital * math.pow (1+ taxa_cdb, meses)) + (aporte * meses)
lucro_cdb = montante_cdb - total_investido
montante_cdb_liquido = total_investido + (lucro_cdb*0.85)

#LCI
taxa_lci = cdi_mensal * perc_lci
montante_lci = (capital * math.pow((1+taxa_lci), meses) + (aporte * meses))

#POUPANÇA
taxa_poupanca = 0.005
montante_poupanca = (capital * math.pow((1 + taxa_poupanca), meses) + (aporte * meses))

#FII - SIMULAÇÕES
variacao1 = random.uniform(-0.03, 0.03)
variacao2 = random.uniform(-0.03, 0.03) 
variacao3 = random.uniform(-0.03, 0.03) 
variacao4 = random.uniform(-0.03, 0.03) 
variacao5 = random.uniform(-0.03, 0.03) 

taxa_fii1 = taxa_fii + variacao1
taxa_fii2 = taxa_fii + variacao2
taxa_fii3 = taxa_fii + variacao3
taxa_fii4 = taxa_fii + variacao4
taxa_fii5 = taxa_fii + variacao5

fii1 = (capital * math.pow((1 + taxa_fii1), meses) + (aporte * meses))
fii2 = (capital * math.pow((1 + taxa_fii2), meses) + (aporte * meses))
fii3 = (capital * math.pow((1 + taxa_fii3), meses) + (aporte * meses))
fii4 = (capital * math.pow((1 + taxa_fii4), meses) + (aporte * meses))
fii5 = (capital * math.pow((1 + taxa_fii5), meses) + (aporte * meses))

lista_fii = [fii1, fii2, fii3, fii4, fii5]
media_fii = statistics.mean(lista_fii)
mediana_fii = statistics.median(lista_fii)
desvio_fii = statistics.stdev(lista_fii)

#DATAS
data_simulacao = datetime.date.today()
dias = meses * 30   
data_resgate = data_simulacao + datetime.timedelta(days=dias)

#META
meta_atingida = media_fii >= meta

#FORMATAÇÃO DE MOEDA
capital_formatado = locale.currency(total_investido, grouping=True)
cdb_formatado = locale.currency(montante_cdb_liquido, grouping=True)
lci_formatado = locale.currency(montante_lci, grouping=True)
poupanca_formatado = locale.currency(montante_poupanca, grouping=True)
fii_formatado = locale.currency(media_fii, grouping=True)

#GRAFICO
grafico_cdb = '█' * int(montante_cdb_liquido / 1000)
grafico_lci = '█' * int(montante_lci / 1000)
grafico_poupanca = '█' * int(montante_poupanca / 1000)
grafico_fii = '█' * int(media_fii / 1000)

#SAIDA
print("\n=========== RELATÓRIO DE INVESTIMENTO ===========")

print("Data da simulação:", data_simulacao)
print("Data estimada de resgate:", data_resgate)

print("\nTotal investido:", locale.currency(total_investido, grouping=True))

print("\n----------- RESULTADOS -----------")

print("CDB:", locale.currency(montante_cdb_liquido, grouping=True))
print("LCI/LCA:", locale.currency(montante_lci, grouping=True))
print("Poupança:", locale.currency(montante_poupanca, grouping=True))
print("FII:", locale.currency(media_fii, grouping=True))

print("\n-------- ESTATÍSTICAS DO FII --------")

print("Média:", locale.currency(media_fii, grouping=True))
print("Mediana:", locale.currency(mediana_fii, grouping=True))
print("Desvio padrão:", locale.currency(desvio_fii, grouping=True))

print("\nMeta atingida:", meta_atingida)

print("\n----------- GRÁFICO -----------")

print("\nCDB")
print(grafico_cdb)

print("\nLCI/LCA")
print(grafico_lci)

print("\nPOUPANÇA")
print(grafico_poupanca)

print("\nFII")
print(grafico_fii)