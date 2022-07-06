from collections import defaultdict
import itertools

#Programado por Afranio Gazolla - Professor e Zootecnista
print("****************************************")
print("* Verificador de Endogamia em Equinos *")
print("****************************************")

# List of nodes
exemplo1 =["DON ROJO HJG", "DON DIEGO BARS", "HJG PEPITA ROJO","MR HULK","MINIE APOLO BARS","DON DIEGO BARS","PESETA ROJO JAR","MR THREE WARS","RED BEE DIAMOND","SHADY APOLO BARS", "SPARKIE BARS", "MRHULK", "MINIE APOLO BARS", "EL CORONE ROJO", "BREE RYDER JA" ]

# List of nodes
exemplo2 =["ETERNALY FRED", "ETERNAL STEEL", "FREDS KITTEN","ETERNAL SUN","SABENA BAR","FRED M","RATSYS KITTEN","ETERNAL WAR","SIERRA GLITTER","STEEL BARS", "PATSY SUE", "DEL MONTE", "COKE ROBERDS MARE", "SMOKEY MOORE", "KITTEN MOORE" ]

# List of nodes
exemplo3 =["HOLLAND TOOLS","HOLLAND EASE","SCENT OF A WOMAN","FIRST DOWN DASH","EASY HENRYETTA","DASH FOR CASH","COPASETTI","DASH FOR CASH","FIRST PRIZE ROSE","EASY JET","BABYS HENRYETTA","ROCKET WRANGLER","FIND A BUYER(TB)","THREE OHS","MONA POLLITA"]


nodes = exemplo2

#Pesos Geneticos na Arvore Genealogica
pesos =[0,0.5,0.5,0.25,0.25,0.25,0.25,0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125]

pares = []

for i in range(0, len(nodes)):
	pares.append((nodes[i], pesos[i]))

d = defaultdict(list)
for k, *v in pares:
   d[k].append(v)

duplas = []

for i in d:
	soma = 0
	flatten_list = list(itertools.chain(*d[i]))
	for v in flatten_list:
		soma += v
	duplas.append((i,soma))

#Impressao dos Resultados
print("animal/influencia genetica")
print("")
for i in duplas:
	print(i[0], i[1])
