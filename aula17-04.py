"""
L=[8,9,15]
x=0
while x < len(L):
    e=L[x]
    print(e)
    x+=1
#
L = [7,9,10,12]
P = int(input("Digite um número a pesquisar"))
for e in L:
    if e == P:
        print("Elemento encontrado!")
        break
    else:
        print("Elemento não encontrado")
#
for v in range(11):
    print(v)
#
for v in range (5, 8):
    print(v)
#
L=[5,9,13]
x=0
for e in L:
        print("[%d] %d" % (x,e))
        x+=1
#
L=[5,9,13]
for x, e in enumerate(L):
    print("[%d] %d" % (x,e))
#
L=[1,7,2,4]
máximo=L[0]
for e in L:
    if e > máximo:
        máximo = e
print(máximo)
#
V=[9,8,7,12,0,13,21]
P=[]
I=[]
for e in V:
    if e % 2 == 0:
        P.append(e)
    else:
        I.append(e)
print("Pares: ", P)
print("Impares: ", I)
#
#Controle da utilização de salas de um cinema
lugares_vagos = [10,2,1,3,0]
while True:
    sala=int(input("Sala (0 sai): "))
    if sala == 0:
        print("Fim")
        break
    if sala > len(lugares_vagos) or sala<1:
        print("Sala inválida")
    elif lugares_vagos[sala-1]==0:
        print("Desculpe, sala lotada!")
    else:
        lugares = int(input("Quantos lugares você deseja (%d vagos):" % lugares_vagos[sala-1]))
    if lugares > lugares_vagos[sala-1]:
        print("Esse número de lugares não está disponível.")
    elif lugares < 0:
        print("Número inválido")
    else:
        lugares_vagos[sala-1]-=lugares
        print("%d lugares vendidos" % lugares)
print("Utilização das salas")
for x,l in enumerate(lugares_vagos):
    print("Sala %d - %d lugar(es) vazio(s)" % (x+1, l))
#
L=["maçãs", "peras", "kiwis"]
for s in L:
    for letra in s:
        print(letra)
#
L=[7,4,3,12,8]
fim=5
while fim > 1:
    trocou=False
    x=0
    while x < (fim-1):
        if L[x] > L[x+1]:
            trocou=True
            temp=L[x]
            L[x]=L[x+1]
            L[x+1]=temp
            x+=1
    if not trocou:
        break
    fim-=1
for e in L:
    print(e)
#
opcao = int(input('Escolha a opção desejada: de 1 a 5: '))

match opcao:
    case 1:
        print("Vc optou pela alternativa 1")
   
    case 2:
        print("Vc optou pela alternativa 2")
   
    case 3:
        print("Vc optou pela alternativa 3")
   
    case 4:
        print("Vc optou pela alternativa 4")
       
    case 5:
        print("Vc optou pela alternativa 5")
       
    case _:
        print("Opção inválida")
#case _:(é obrigatorio no match case, igual o else)
#

print("Bem vindo a estação")
print("Qual estação deseja embarcar?")
print("1-São Paulo")
print("2-Rio de Janeiro")
print("3-Curitiba")
print("4-Brasilia")
print("5-Florianopolis")

plataforma = int(input('Para onde você quer ir, Digite o número da cidade: '))

match plataforma:
   
    case 1:
        print("Você precisa ir para a plataforma 1")
   
    case 2:
        print("Você precisa ir para a plataforma 2")
   
    case 3:
        print("Você precisa ir para a plataforma 3")
   
    case 4:
        print("Você precisa ir para a plataforma 4")
   
    case 5:
        print("Você precisa ir para a plataforma 5")
   
    case _:
        print("Não foi possivel localizar a plataforma, ou houve erro de digitação.")

#
print("")
print("-------------------------")
print("Bem vindo ao Restaurante!")
print("-------------------------")
print("Opções de Vinhos:")
print("1 - Casa Valduga Gran                     | R$160,00")
print("2 - Casa Silva Gran Terrois los Carménère | R$130,00")
print("3 - Chocolan Origen Viognier              | R$180,00")
print("4 - Miolo Demi-sec Reserva especial 2005  | R$ 90,00")
print("5 - Casa Silva Terrois Cabernet Savignon  | R$100,00")
print("----------------------------------------------------")
vinho = int(input('Qual vinho você deseja? (Digite o número do vinho): '))

print("-------------------------------------------------------")

match vinho:
   
    case 1:
        print("Você escolheu: Casa Valduga Gran - R$160,00 ")
       
    case 2:
        print("Você escolheu: Casa Silva Gran Terrois los Carménère - R$130,00")
       
    case 3:
        print("Você escolheu: Chocolan Origen Viognier - R$180,00")
       
    case 4:
        print("Você escolheu: Miolo Demi-sec Reserva especial 2005 - R$90,00")
       
    case 5:
        print("Você escolheu: Casa Silva Terrois Cabernet Savignon - R$100,00")
       
    case _:
        print("Você escolheu: Vinho não encontrado")
"""
