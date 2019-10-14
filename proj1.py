def sortFirst(val):
    return val[0]

#Leitura de valores
nMeses, mLics = input().split()
licensas = []
visitados = []
mLics = int(mLics)
nMeses = int(nMeses)
ant = -1
custo = []
custo.append(0.0)

#Matriz de licensas possui seguintes colunas
#0 Mês de início
#1 Tempo de duração em meses
#2 Custo da licensa


#Lê valores e inicializa vetor de visitados
for i in range(mLics):
    inicio, dur, preco = input().split()
    licensas.append([inicio, dur, preco])
    licensas[i][0] = int(licensas[i][0])
    licensas[i][1] = int(licensas[i][1])
    licensas[i][2] = float(licensas[i][2])
    visitados.append(False)
#Licensas ordenadas de acordo com tempo de início    
licensas.sort(key = sortFirst)

#Caso 2 licensas tenham o mesmo mês de início, abre um novo ramo na árvore de custos
for i in range(mLics):
    if ant == licensas[i][0]:
        custo.append(0.0)
    else:
        ant = licensas[i][0]
mes = 0

#Caso não há licensa que comece em janeiro, problema não tem solução
if int(licensas[0][0]) != 0:
    print("Não há solução.")
    exit()

#Caso trivial, quando há apenas 1 licensa
if mLics == 1:
    custo = 0.0
    if nMeses%licensas[0][1] == 0:
        for i in range(nMeses//licensas[0][1]):
            custo += licensas[0][2]
        print(custo)
    else:
        print("Não há solução")
    exit()

custoFinal = 0.0 #Custo final da árvore de custos
countCaminhos = 0 #Conntador de caminhos possíveis na árvore
contMeses = 0 #Mês atual
i=0
while   i < mLics:
    if not visitados[i]:
        #Caso mês atual seja janeiro ou se início da licensa seja igual ao mês atual 
        # e mês de fim seja menor ou igual ao final
        if contMeses == 0 or (licensas[i][0] == contMeses and contMeses+licensas[i][1] <= nMeses):
            visitados[i] = True
            contMeses+=licensas[i][1]
            custo[countCaminhos]+=licensas[i][2]
            if contMeses == nMeses:
                #Fim de caminho na árvore de custos, percorre agora o próximo caminho
                countCaminhos+=1
                contMeses = 0
                i=-1
    i+=1    

print(min(custo))