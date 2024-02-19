'''
Constante = "Variáveis" que vão mudar muitras condições no mesmo if (não queremos isso)
<---- Contagem de complexidade, ou seja, quanto mais linha mais distantes da margem
(quanto mais blocos de código dentro de blocos de código), mais complexo o código
'''
velocidade = 61 #Velocidade atual do carro
local_carro = 90 #Local em que o carro está na estrada

RADAR_1 = 60 #Veocidade máxima do radar 1
LOCAL_1 = 100 #Local aonde o radar 1 está
RADAR_RANGE = 1 #Distância onde o radar pega

velocidade_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE)and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_passou_radar_1

if velocidade > RADAR_1:
    print('Velocidade do carro pasou do radar 1')

if carro_passou_radar_1:
    print ('Carro passou radar 1')

if  carro_passou_radar_1 and velocidade_carro_passou_radar_1:
    print('Carro multado em radar 1')