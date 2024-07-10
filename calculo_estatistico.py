import glob

# codigo que le todos os angulos de todas as variaveis (tanto pra MMMSS como pra COLUNA) nos arquivos
# e salva todos esses valores em listas contendo o nome das variaveis
# posteriormente usa essas listas para fazer o calculo estatistico


# função que calcula a correlação entre dados que estão presentes em duas listas
def correlacao(lista_ouro, lista_video):
    
    soma_x = 0.0
    soma_y = 0.0
    soma_quadrado_x = 0.0
    soma_quadrado_y = 0.0
    soma_x_y = 0.0

    # i eh o numero de pares ordenados. as listas devem possuir o mesmo tamanho!!

    # usando a menor lista como referencia, para não dar erro de acesso indevido na lista menor
    if(len(lista_ouro) > len(lista_video)):
        
        for i in range(len(lista_video)):
            soma_x += lista_ouro[i]
            soma_y += lista_video[i]
            soma_quadrado_x += lista_ouro[i] ** 2
            soma_quadrado_y += lista_video[i] ** 2
            soma_x_y += lista_ouro[i] * lista_video[i]


        n = len(lista_video)    
        aux_1 = ((n * soma_quadrado_x - soma_x**2)**0.5)
        aux_2 = ((n * soma_quadrado_y - soma_y**2 )**0.5)

        # calculados os termos necessarios, agr eh so aplicar esses numeros na expressao matematica que calcula a correlaçao

        correlacao = ((n * soma_x_y) - soma_x * soma_y ) / (aux_1 * aux_2)

        return correlacao
    
    else:

        for i in range(len(lista_ouro)):
            soma_x += lista_ouro[i]
            soma_y += lista_video[i]
            soma_quadrado_x += lista_ouro[i] ** 2
            soma_quadrado_y += lista_video[i] ** 2
            soma_x_y += lista_ouro[i] * lista_video[i]


        n = len(lista_ouro)    
        aux_1 = ((n * soma_quadrado_x - soma_x**2)**0.5)
        aux_2 = ((n * soma_quadrado_y - soma_y**2 )**0.5)
        
        correlacao = ((n * soma_x_y) - soma_x * soma_y ) / (aux_1 * aux_2)

        return correlacao
   



# função que recebe duas listas e calcula o erro medio absoluto entre os dados
# essas listas devem possuir o mesmo tamanho
# uma lista contém os ângulos calculados a partir dos videos
# a outra lista contém os ângulos calculados a partir dos tsv
def erro_medio_absoluto(lista_ouro, lista_video):
    
    # lista que vai guardar cada um dos erros absoluto entre os ângulos
    #erro_medio = []

    if(len(lista_ouro) > len(lista_video)):
        soma = 0

        for i in range(len(lista_video)):
            soma += abs(lista_ouro[i] - lista_video[i])


        return soma / len(lista_video)    

    else:
        soma = 0

        for i in range(len(lista_ouro)):
            soma += abs(lista_ouro[i] - lista_video[i])

        return soma / len(lista_ouro)
 

    

# DECLARANDO AS LISTAS PARA REPRESENTAR TODAS AS VARIAVEIS
# MMSS
## OBSERVAÇÃO: FRONTAL = 30 FRAMES  // LATERAL = 60 FRAMES 
abd_ombro_direito_ouro = []
abd_ombro_direito_video_frontal = []
abd_ombro_direito_video_lateral = []

abd_ombro_esquerdo_ouro = []
abd_ombro_esquerdo_video_frontal = []
abd_ombro_esquerdo_video_lateral = []


flexao_cotov_direito_ouro = []
flexao_cotov_direito_video_frontal = []
flexao_cotov_direito_video_lateral = []

flexao_cotov_esquerdo_ouro = []
flexao_cotov_esquerdo_video_frontal = []
flexao_cotov_esquerdo_video_lateral = []


flexao_ombro_direito_ouro = []
flexao_ombro_direito_video_frontal = []
flexao_ombro_direito_video_lateral = []

flexao_ombro_esquerdo_ouro = []
flexao_ombro_esquerdo_video_frontal = []
flexao_ombro_esquerdo_video_lateral = []

# COLUNA
# OBSERVACAO: FRONTAL = 60 FRAMES   // LATERAL = 30 FRAMES
flexao_cabeca_ouro = []
flexao_cabeca_video_frontal = []
flexao_cabeca_video_lateral = []

flexao_tronco_ouro = []
flexao_tronco_video_frontal = []
flexao_tronco_video_lateral = []


rotacao_tronco_ouro = []
rotacao_tronco_video_frontal = []
rotacao_tronco_video_lateral = []


# busca por todos os arquivos TSV no diretorio especificado
pasta_ouro_MMSS = glob.glob("D:/Faculdade/PET/Fisioterapia/Estatistica/MMSS/padrao_ouro/*.tsv")
pasta_video_frontal_MMSS = glob.glob("D:/Faculdade/PET/Fisioterapia/Estatistica/MMSS/video_mmss/frontal/*.tsv")
pasta_video_lateral_MMSS = glob.glob("D:/Faculdade/PET/Fisioterapia/Estatistica/MMSS/video_mmss/lateral/*.tsv")

pasta_ouro_COLUNA = glob.glob("D:/Faculdade/PET/Fisioterapia/Estatistica/COLUNA/padrao_ouro/*.tsv")

pasta_video_frontal_COLUNA = glob.glob("D:/Faculdade/PET/Fisioterapia/Estatistica/COLUNA/video_coluna/frontal/*.tsv")
pasta_video_lateral_COLUNA = glob.glob("D:/Faculdade/PET/Fisioterapia/Estatistica/COLUNA/video_coluna/lateral/*.tsv")

#padrao_ouro_MMSS = 'C:/Users/jhona/OneDrive/Desktop/estatistica/MMSS/padrao_ouro/padrao_ouro_Bianca_MMSS.tsv'
#video_MMSS = 'C:/Users/jhona/OneDrive/Desktop/estatistica\MMSS/video_mmss/video_Bianca_MMSS.tsv'

#padrao_ouro_COLUNA = 'C:/Users/jhona/OneDrive/Desktop/estatistica/COLUNA/padrao_ouro/padra_ouro_Bianca_COLUNA.tsv'
#video_COLUNA = 'C:/Users/jhona/OneDrive/Desktop/estatistica/COLUNA/video_coluna/video_Bianca_COLUNA.tsv'



################################################################################################################
################################################################################################################
#                                   MMSS

# PERCORRENDO A PASTA QUE CONTEM OS ARQUIVOS DO MMSS_OURO
# E SALVANDO NAS LISTAS OS ANGULOS

for nome_arquivo in pasta_ouro_MMSS:

    with open(nome_arquivo, 'r') as ouro_MMSS:
        print(nome_arquivo)
        for i in ouro_MMSS.readlines():

            coluna = i.strip().split('\t')

            ## --------------- ABD OMBRO DIREITO -------------------- ##
            #abd_ombro_direito_ouro.append(float(coluna[2]))
            

            ## --------------- ABD OMBRO ESQUERDO -------------------- ##
            abd_ombro_esquerdo_ouro.append(float(coluna[2]))


            ## --------------- FLEXÃO COTOVELO DIREITO -------------------- ##
            #flexao_cotov_direito_ouro.append(float(coluna[4]))

            
            ## --------------- FLEXÃO COTOVELO ESQUERDO -------------------- ##
            #flexao_cotov_esquerdo_ouro.append(float(coluna[6]))


            ## --------------- FLEXAO OMBRO DIREITO ------------------------ ##
            #flexao_ombro_direito_ouro.append(float(coluna[10]))


            ## --------------- FLEXAO OMBRO ESQUERDO ---------------- ##
            #flexao_ombro_esquerdo_ouro.append(float(coluna[12]))
        
##print(abd_ombro_direito_ouro[2042]) #ultimo abd_ombro_direito_ouro da amanda facom
#print(abd_ombro_direito_ouro[2043])  #primeiro abd_ombro_direito da amanda pos   


##############################################################################################

# PERCORRENDO A PASTA QUE CONTEM OS ARQUIVOS DO MMSS_VIDEO_FRONTAL (30 FRAMES)
# E SALVANDO NAS LISTAS OS ANGULOS
for nome_arquivo in pasta_video_frontal_MMSS:

    with open(nome_arquivo, 'r') as video_MMSS:

        
        for i in video_MMSS.readlines():
            coluna = i.strip().split('\t')

            ## --------------- ABD OMBRO DIREITO -------------------- ##
            #abd_ombro_direito_video_frontal.append(float(coluna[1]))
            

            ## --------------- ABD OMBRO ESQUERDO -------------------- ##
            #abd_ombro_esquerdo_video_frontal.append(float(coluna[2]))

            
            ## --------------- FLEXÃO COTOVELO DIREITO -------------------- ##
            #flexao_cotov_direito_video_frontal.append(float(coluna[5]))


            ## --------------- FLEXÃO COTOVELO ESQUERDO -------------------- ##
            #flexao_cotov_esquerdo_video_frontal.append(float(coluna[7]))
            

            ## --------------- FLEXAO OMBRO DIREITO ----------------------- ##
            #flexao_ombro_direito_video_frontal.append(float(coluna[9]))
       
            ## --------------- FLEXAO OMBRO ESQUERDO ---------------------- ##
            #flexao_ombro_esquerdo_video_frontal.append(float(coluna[11]))
        


# PERCORRENDO A PASTA QUE CONTEM OS ARQUIVOS DO MMSS_VIDEO_LATERAL (60 FRAMES)
# E SALVANDO NAS LISTAS OS ANGULOS
for nome_arquivo in pasta_video_lateral_MMSS:
    
    with open(nome_arquivo, 'r') as video_MMSS:

        for i in video_MMSS.readlines():
            coluna = i.strip().split('\t')

            ## --------------- ABD OMBRO DIREITO -------------------- ##
            #abd_ombro_direito_video_lateral.append(float(coluna[1]))
            
 
            ## --------------- ABD OMBRO ESQUERDO -------------------- ##
            abd_ombro_esquerdo_video_lateral.append(float(coluna[1]))

        
            ## --------------- FLEXÃO COTOVELO DIREITO -------------------- ##
           # flexao_cotov_direito_video_lateral.append(float(coluna[5]))


            ## --------------- FLEXÃO COTOVELO ESQUERDO -------------------- ##
            #flexao_cotov_esquerdo_video_lateral.append(float(coluna[7]))


            ## --------------- FLEXAO OMBRO DIREITO ---------------- ##
            #flexao_ombro_direito_video_lateral.append(float(coluna[9]))


            ##---------------- FLEXAO OMBRO ESQUERDO ---------------- ##
            #flexao_ombro_esquerdo_video_lateral.append(float(coluna[11]))


################################################################################################################
################################################################################################################
#                                   COLUNA

# PERCORRENDO A PASTA QUE CONTEM OS ARQUIVOS DO COLUNA_OURO
# E SALVANDO NAS LISTAS OS ANGULOS

for nome_arquivo in pasta_ouro_COLUNA:

    with open(nome_arquivo, 'r') as coluna_ouro:

        for i in coluna_ouro.readlines():

            coluna = i.strip().split('\t')

            ## ----------- FLEXAO CABECA -------------- ##
            #flexao_cabeca_ouro.append(float(coluna[1]))
            #print("Lista flexao_cabeca_ouro:", flexao_cabeca_ouro[1])

            ## ----------- FLEXAO TRONCO -------------- ##
            #flexao_tronco_ouro.append(float(coluna[3]))

            ## ----------- ROTACAO TRONCO -------------- ##
            #rotacao_tronco_ouro.append(float(coluna[5]))



# PERCORRENDO A PASTA QUE CONTEM OS ARQUIVOS DO COLUNA_VIDEO FRONTAL (60 FRAMES)
# E SALVANDO NAS LISTAS OS ANGULOS
for nome_arquivo in pasta_video_frontal_COLUNA:

    with open(nome_arquivo, 'r') as coluna_video:

        for i in coluna_video.readlines():

            coluna = i.strip().split('\t')

            ## ----------- FLEXAO CABECA -------------- ##
            #flexao_cabeca_video_frontal.append(float(coluna[1]))


            ## ----------- FLEXAO TRONCO -------------- ##
            #flexao_tronco_video_frontal.append(float(coluna[3]))


            ## ----------- ROTACAO TRONCO -------------- ##
            #rotacao_tronco_video_frontal.append(float(coluna[5]))




# PERCORRENDO A PASTA QUE CONTEM OS ARQUIVOS DO COLUNA_VIDEO lateral (30 FRAMES)
# E SALVANDO NAS LISTAS OS ANGULOS
for nome_arquivo in pasta_video_lateral_COLUNA:

    with open(nome_arquivo, 'r') as coluna_video:

        for i in coluna_video.readlines():

            coluna = i.strip().split('\t')

            ## ----------- FLEXAO CABECA -------------- ##
            #flexao_cabeca_video_lateral.append(float(coluna[1]))


            ## ----------- FLEXAO TRONCO -------------- ##
            #flexao_tronco_video_lateral.append(float(coluna[3]))


            ## ----------- ROTACAO TRONCO -------------- ##
            #rotacao_tronco_video_lateral.append(float(coluna[5]))


##############################################################################################################
#### AQUI TERMINA A LEITURA DOS ANGULOS


################ ------- ERRO MEDIO ABSOLUTO ------- ######################

#-------------------------- MMSS ------------------------------------ #
# ABDUÇÃO OMBRO DIREITO

#erro_abd_ombro_direito_ouro_frontal = erro_medio_absoluto(abd_ombro_direito_ouro, abd_ombro_direito_video_frontal)
#erro_abd_ombro_direito_ouro_lateral = erro_medio_absoluto(abd_ombro_direito_ouro, abd_ombro_direito_video_lateral)
#erro_abd_ombro_direito_frontal_lateral = erro_medio_absoluto(abd_ombro_direito_video_frontal, abd_ombro_direito_video_lateral)

#print(f"Erro Médio Absoluto para abd_ombro_direito entre o video FRONTAL e o Padrão Ouro: {erro_abd_ombro_direito_ouro_frontal}")
#print(f"Erro Médio Absoluto para abd_ombro_direito entre o video LATERAL e o Padrão Ouro: {erro_abd_ombro_direito_ouro_lateral}")
#print(f"Erro Médio Absoluto para abd_ombro_direito entre o video FRONTAL e o video LATERAL: {erro_abd_ombro_direito_frontal_lateral}")



# ABDUÇÃO OMBRO ESQUERDO

#erro_abd_ombro_esquerdo_ouro_frontal = erro_medio_absoluto(abd_ombro_esquerdo_ouro, abd_ombro_esquerdo_video_frontal)
erro_abd_ombro_esquerdo_ouro_lateral = erro_medio_absoluto(abd_ombro_esquerdo_ouro, abd_ombro_esquerdo_video_lateral)
#erro_abd_ombro_esquerdo_frontal_lateral = erro_medio_absoluto(abd_ombro_esquerdo_video_frontal, abd_ombro_esquerdo_video_lateral)


#print(f"Erro Médio Absoluto para abd_ombro_esquerdo entre o video FRONTAL e o Padrão Ouro: {erro_abd_ombro_esquerdo_ouro_frontal}")
print(f"Erro Médio Absoluto para abd_ombro_esquerdo entre o video LATERAL e o Padrão Ouro: {erro_abd_ombro_esquerdo_ouro_lateral}")
#print(f"Erro Médio Absoluto para abd_ombro_esquerdo entre o video FRONTAL e o video LATERAL: {erro_abd_ombro_esquerdo_frontal_lateral}")
 

# FLEXÃO OMBRO DIREITO

#erro_flex_ombro_direito_ouro_frontal = erro_medio_absoluto(flexao_ombro_direito_ouro, flexao_ombro_direito_video_frontal)
#erro_flex_ombro_direito_ouro_lateral = erro_medio_absoluto(flexao_ombro_direito_ouro, flexao_ombro_direito_video_lateral)
#erro_flex_ombro_direito_frontal_lateral = erro_medio_absoluto(flexao_ombro_direito_video_frontal, flexao_ombro_esquerdo_video_lateral)


#print(f"Erro Médio Absoluto para flex_ombro_direito entre o video FRONTAL e o Padrão Ouro: {erro_flex_ombro_direito_ouro_frontal}")
#print(f"Erro Médio Absoluto para flex_ombro_direito entre o video LATERAL e o Padrão Ouro: {erro_flex_ombro_direito_ouro_lateral}")
#print(f"Erro Médio Absoluto para flex_ombro_direito entre o video FRONTAL e o video LATERAL: {erro_flex_ombro_direito_frontal_lateral}")

# FLEXÃO OMBRO ESQUERDO

#erro_flex_ombro_esquerdo_ouro_frontal = erro_medio_absoluto(flexao_ombro_esquerdo_ouro, flexao_ombro_esquerdo_video_frontal)
#erro_flex_ombro_esquerdo_ouro_lateral = erro_medio_absoluto(flexao_ombro_esquerdo_ouro, flexao_ombro_esquerdo_video_lateral)
#erro_flex_ombro_esquerdo_frontal_lateral = erro_medio_absoluto(flexao_ombro_esquerdo_video_frontal, flexao_ombro_esquerdo_video_lateral)
'''
print(f"Erro Médio Absoluto para flex_ombro_esquerdo entre o video FRONTAL e o Padrão Ouro: {erro_flex_ombro_esquerdo_ouro_frontal}")
print(f"Erro Médio Absoluto para flex_ombro_esquerdo entre o video LATERAL e o Padrão Ouro: {erro_flex_ombro_esquerdo_ouro_lateral}")
#print(f"Erro Médio Absoluto para flex_ombro_esquerdo entre o video FRONTAL e o video LATERAL: {erro_flex_ombro_esquerdo_frontal_lateral}")


# FLEXÃO COTOVELO DIREITO

erro_flex_cot_direito_ouro_frontal = erro_medio_absoluto(flexao_cotov_direito_ouro, flexao_cotov_direito_video_frontal)
erro_flex_cot_direito_ouro_lateral = erro_medio_absoluto(flexao_cotov_direito_ouro, flexao_cotov_direito_video_lateral)
#erro_flex_cot_direito_frontal_lateral = erro_medio_absoluto(flexao_cotov_direito_video_frontal, flexao_cotov_direito_video_lateral)

print(f"Erro Médio Absoluto para flex_cot_direito entre o video FRONTAL e o Padrão Ouro: {erro_flex_cot_direito_ouro_frontal}")
print(f"Erro Médio Absoluto para flex_cot_direito entre o video LATERAL e o Padrão Ouro: {erro_flex_cot_direito_ouro_lateral}")
#print(f"Erro Médio Absoluto para flex_cot_direito entre o video FRONTAL e o video LATERAL: {erro_flex_cot_direito_frontal_lateral}")


# FLEXÃO COTOVELO ESQUERDO

erro_flex_cot_esquerdo_ouro_frontal = erro_medio_absoluto(flexao_cotov_esquerdo_ouro, flexao_cotov_esquerdo_video_frontal)
erro_flex_cot_esquerdo_ouro_lateral = erro_medio_absoluto(flexao_cotov_esquerdo_ouro, flexao_cotov_esquerdo_video_lateral)
#erro_flex_cot_esquerdo_frontal_lateral = erro_medio_absoluto(flexao_cotov_esquerdo_video_frontal, flexao_cotov_esquerdo_video_lateral)


print(f"Erro Médio Absoluto para flex_cot_esquerdo entre o video FRONTAL e o Padrão Ouro: {erro_flex_cot_esquerdo_ouro_frontal}")
print(f"Erro Médio Absoluto para flex_cot_esquerdo entre o video LATERAL e o Padrão Ouro: {erro_flex_cot_esquerdo_ouro_lateral}")
#print(f"Erro Médio Absoluto para flex_cot_esquerdo entre o video FRONTAL e o video LATERAL: {erro_flex_cot_esquerdo_frontal_lateral}")

'''