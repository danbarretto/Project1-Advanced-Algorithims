def sortFirst(val):
    return val[0]

nMeses, mLics = input().split()
licensas = []
visitados = []
mLics = int(mLics)
ant = -1
custo = []
custo.append(0.0)

for i in range(mLics):
    inicio, dur, preco = input().split()
    licensas.append([inicio, dur, preco])
    visitados.append(False)
    
licensas.sort(key = sortFirst)

for i in range(mLics):
    if ant == licensas[i][0]:
        custo.append(0.0)
    else:
        ant = licensas[i][0]
mes = 0


if int(licensas[0][0]) != 0:
    print("Não há solução.")
    exit()

custoFinal = 0.0
countCaminhos = 0
contMeses = 0
i=0
while i < mLics:
    if not visitados[i]:
        if contMeses == 0 or (int(licensas[i][0]) == contMeses and contMeses+int(licensas[i][1]) <= int(nMeses)):
            visitados[i] = True
            contMeses+=int(licensas[i][1])
            custo[countCaminhos]+=float(licensas[i][2])
            if contMeses == int(nMeses):
                countCaminhos+=1
                contMeses=0
                i=-1
    i+=1    

print(custo)