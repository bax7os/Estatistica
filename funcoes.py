################ ------- ERRO MEDIO ABSOLUTO ------- ######################

#-------------------------- MMSS ------------------------------------ #
# ABDUÇÃO OMBRO DIREITO

erro_abd_ombro_direito_ouro_frontal = erro_medio_absoluto(abd_ombro_direito_ouro, abd_ombro_direito_video_frontal)
erro_abd_ombro_direito_ouro_lateral = erro_medio_absoluto(abd_ombro_direito_ouro, abd_ombro_direito_video_lateral)
erro_abd_ombro_direito_frontal_lateral = erro_medio_absoluto(abd_ombro_direito_video_frontal, abd_ombro_direito_video_lateral)


# ABDUÇÃO OMBRO ESQUERDO

erro_abd_ombro_esquerdo_ouro_frontal = erro_medio_absoluto(abd_ombro_esquerdo_ouro, abd_ombro_esquerdo_video_frontal)
erro_abd_ombro_esquerdo_ouro_lateral = erro_medio_absoluto(abd_ombro_esquerdo_ouro, abd_ombro_esquerdo_video_lateral)
erro_abd_ombro_esquerdo_frontal_lateral = erro_medio_absoluto(abd_ombro_esquerdo_video_frontal, abd_ombro_esquerdo_video_lateral)


# FLEXÃO OMBRO DIREITO

erro_flex_ombro_direito_ouro_frontal = erro_medio_absoluto(flexao_ombro_direito_ouro, flexao_ombro_direito_video_frontal)
erro_flex_ombro_direito_ouro_lateral = erro_medio_absoluto(flexao_ombro_direito_ouro, flexao_ombro_direito_video_lateral)
erro_flex_ombro_direito_frontal_lateral = erro_medio_absoluto(flexao_ombro_direito_video_frontal, flexao_ombro_esquerdo_video_lateral)


# FLEXÃO OMBRO ESQUERDO

erro_flex_ombro_esquerdo_ouro_frontal = erro_medio_absoluto(flexao_ombro_esquerdo_ouro, flexao_ombro_esquerdo_video_frontal)
erro_flex_ombro_esquerdo_ouro_lateral = erro_medio_absoluto(flexao_ombro_esquerdo_ouro, flexao_ombro_esquerdo_video_lateral)
erro_flex_ombro_esquerdo_frontal_lateral = erro_medio_absoluto(flexao_ombro_esquerdo_video_frontal, flexao_ombro_esquerdo_video_lateral)

# FLEXÃO COTOVELO DIREITO

erro_flex_cot_direito_ouro_frontal = erro_medio_absoluto(flexao_cotov_direito_ouro, flexao_cotov_direito_video_frontal)
erro_flex_cot_direito_ouro_lateral = erro_medio_absoluto(flexao_cotov_direito_ouro, flexao_cotov_direito_video_lateral)
erro_flex_cot_direito_frontal_lateral = erro_medio_absoluto(flexao_cotov_direito_video_frontal, flexao_cotov_direito_video_lateral)

# FLEXÃO COTOVELO ESQUERDO

erro_flex_cot_esquerdo_ouro_frontal = erro_medio_absoluto(flexao_cotov_esquerdo_ouro, flexao_cotov_esquerdo_video_frontal)
erro_flex_cot_esquerdo_ouro_lateral = erro_medio_absoluto(flexao_cotov_esquerdo_ouro, flexao_cotov_esquerdo_video_lateral)
erro_flex_cot_esquerdo_frontal_lateral = erro_medio_absoluto(flexao_cotov_esquerdo_video_frontal, flexao_cotov_esquerdo_video_lateral)


movimento_ouro_MMSS =  [abd_ombro_direito_ouro, abd_ombro_esquerdo_ouro, flexao_ombro_direito_ouro, 
                    flexao_ombro_esquerdo_ouro, flexao_cotov_direito_ouro, flexao_cotov_esquerdo_ouro]

movimento_frontal_MMSS = [abd_ombro_direito_video_frontal, abd_ombro_esquerdo_video_frontal, flexao_ombro_direito_video_frontal, 
                    flexao_ombro_esquerdo_video_frontal, flexao_cotov_direito_video_frontal, flexao_cotov_esquerdo_video_frontal]

movimento_lateral_MMSS = [abd_ombro_direito_video_lateral, abd_ombro_esquerdo_video_lateral, flexao_ombro_direito_video_lateral, 
                    flexao_ombro_esquerdo_video_lateral, flexao_cotov_direito_video_lateral, flexao_cotov_esquerdo_video_lateral]




amplitude_frontal_MMSS = []
amplitude_lateral_MMSS = []
amplitude_ouro_MMSS = []

for i in movimento_ouro_MMSS:
    amplitude_ouro_MMSS.append(max(i) - min(i))

for i in movimento_frontal_MMSS:
    amplitude_frontal_MMSS.append(max(i) - min(i))

for i in movimento_lateral_MMSS:
    amplitude_lateral_MMSS.append(max(i) - min(i))


#------------------------------- COLUNA ---------------------------------------#

# FLEXÃO CABEÇA

erro_flex_cabeca_ouro_frontal = erro_medio_absoluto(flexao_cabeca_ouro, flexao_cabeca_video_frontal)
erro_flex_cabeca_ouro_lateral = erro_medio_absoluto(flexao_cabeca_ouro, flexao_cabeca_video_lateral)
erro_flex_cabeca_frontal_lateral = erro_medio_absoluto(flexao_cabeca_video_frontal, flexao_cabeca_video_lateral)


# FLEXÃO TRONCO

erro_flex_tronco_ouro_frontal = erro_medio_absoluto(flexao_tronco_ouro, flexao_tronco_video_frontal)
erro_flex_tronco_ouro_lateral = erro_medio_absoluto(flexao_tronco_ouro, flexao_tronco_video_lateral)
erro_flex_tronco_frontal_lateral = erro_medio_absoluto(flexao_tronco_video_frontal, flexao_tronco_video_lateral)


# ROTAÇÃO TRONCO

erro_rot_tronco_ouro_frontal = erro_medio_absoluto(rotacao_tronco_ouro, rotacao_tronco_video_frontal)
erro_rot_tronco_ouro_leteral = erro_medio_absoluto(rotacao_tronco_ouro, rotacao_tronco_video_lateral)
erro_rot_tronco_frontal_lateral = erro_medio_absoluto(rotacao_tronco_video_frontal, rotacao_tronco_video_lateral)

movimento_ouro_COLUNA = [flexao_cabeca_ouro, flexao_tronco_ouro, rotacao_tronco_ouro]
movimento_frontal_COLUNA = [flexao_cabeca_video_frontal, flexao_tronco_video_frontal, rotacao_tronco_video_frontal]
movimento_lateral_COLUNA = [flexao_cabeca_video_lateral, flexao_tronco_video_lateral, rotacao_tronco_video_lateral]


amplitude_ouro_COLUNA = []
amplitude_frontal_COLUNA = []
amplitude_lateral_COLUNA = []

for i in movimento_ouro_COLUNA:
    amplitude_ouro_COLUNA.append(max(i) - min(i))

for i in movimento_frontal_COLUNA:
    amplitude_frontal_COLUNA.append(max(i) - min(i))

for i in movimento_lateral_COLUNA:
    amplitude_lateral_COLUNA.append(max(i) - min(i))

#dois primeiros = MMSS; depois COLUNA
erro_medio_geral = []
correlacao_geral = []
compare_ouro_video = [amplitude_lateral_MMSS, amplitude_frontal_MMSS, amplitude_lateral_COLUNA, amplitude_frontal_COLUNA]

count = 0
for i in compare_ouro_video:
    if(count <= 1):
        erro_medio_geral.append(erro_medio_absoluto(amplitude_ouro_MMSS, i))
        correlacao_geral.append(correlacao(amplitude_ouro_MMSS, i))
    else:
        erro_medio_geral.append(erro_medio_absoluto(amplitude_ouro_COLUNA, i))
        correlacao_geral.append(correlacao(amplitude_ouro_COLUNA, i))
    count+= 1

erro_medio_geral.append(erro_medio_absoluto(compare_ouro_video[0], compare_ouro_video[1]))
erro_medio_geral.append(erro_medio_absoluto(compare_ouro_video[2], compare_ouro_video[3]))

correlacao_geral.append(correlacao(compare_ouro_video[0], compare_ouro_video[1]))
correlacao_geral.append(correlacao(compare_ouro_video[2], compare_ouro_video[3]))



############### ------- CORRELAÇÃO -------------- ####################

#------------------ MMSS ------------------------- #

# ABDUÇÃO OMBRO DIREITO

corr_abd_ombro_direito_ouro_frontal = correlacao(abd_ombro_direito_ouro, abd_ombro_direito_video_frontal)
corr_abd_ombro_direito_ouro_lateral = correlacao(abd_ombro_direito_ouro, abd_ombro_direito_video_lateral)
corr_abd_ombro_direito_frontal_lateral = correlacao(abd_ombro_direito_video_frontal, abd_ombro_direito_video_lateral)

# ABDUÇÃO OMBRO ESQUERDO

corr_abd_ombro_esquerdo_ouro_frontal = correlacao(abd_ombro_esquerdo_ouro, abd_ombro_esquerdo_video_frontal)
corr_abd_ombro_esquerdo_ouro_lateral = correlacao(abd_ombro_esquerdo_ouro, abd_ombro_esquerdo_video_lateral)
corr_abd_ombro_esquerdo_frontal_lateral = correlacao(abd_ombro_esquerdo_video_frontal, abd_ombro_esquerdo_video_lateral)

# FLEXÃO OMBRO DIREITO

corr_flex_ombro_direito_ouro_frontal = correlacao(flexao_ombro_direito_ouro, flexao_ombro_direito_video_frontal)
corr_flex_ombro_direito_ouro_lateral = correlacao(flexao_ombro_direito_ouro, flexao_ombro_direito_video_lateral)
corr_flex_ombro_direiro_frontal_lateral = correlacao(flexao_ombro_direito_video_frontal, flexao_ombro_direito_video_lateral)

# FLEXÃO OMBRO ESQUERDO

corr_flex_ombro_esquerdo_ouro_frontal = correlacao(flexao_ombro_esquerdo_ouro, flexao_ombro_esquerdo_video_frontal)
corr_flex_ombro_direito_ouro_lateral = correlacao(flexao_ombro_esquerdo_ouro, flexao_ombro_esquerdo_video_lateral)
corr_flex_ombro_direiro_frontal_lateral = correlacao(flexao_ombro_esquerdo_video_frontal, flexao_ombro_esquerdo_video_lateral)

# FLEXAO COTOVELO DIREITO

corr_flex_cot_direito_ouro_frontal = correlacao(flexao_cotov_direito_ouro, flexao_cotov_direito_video_frontal)
corr_flex_cot_direito_ouro_lateral = correlacao(flexao_cotov_direito_ouro, flexao_cotov_direito_video_lateral)
corr_flex_cot_direito_frontal_lateral = correlacao(flexao_cotov_direito_video_frontal, flexao_cotov_direito_video_lateral)


# FLEXAO COTOVELO ESQUERDO

corr_flex_cot_esquerdo_ouro_frontal = correlacao(flexao_cotov_esquerdo_ouro, flexao_cotov_esquerdo_video_frontal)
corr_flex_cot_esquerdo_ouro_lateral = correlacao(flexao_cotov_esquerdo_ouro, flexao_cotov_esquerdo_video_lateral)
corr_flex_cot_esquerdo_frontal_lateral = correlacao(flexao_cotov_esquerdo_video_frontal, flexao_cotov_esquerdo_video_lateral)


max_ouro_MMSS = []
min_ouro_MMSS = []

max_frontal_MMSS = []
min_frontal_MMSS = []

max_lateral_MMSS = []
min_lateral_MMSS = []

max_ouro_COLUNA = []
min_ouro_COLUNA = []

max_frontal_COLUNA = []
min_frontal_COLUNA = []

max_lateral_COLUNA = []
min_lateral_COLUNA = []



for o_MMSS, f_MMSS, l_MMSS, o_COLUNA, f_COLUNA, l_COLUNA in movimento_ouro_MMSS, movimento_frontal_MMSS, movimento_lateral_MMSS, movimento_ouro_COLUNA, movimento_frontal_COLUNA, movimento_lateral_COLUNA:
    max_ouro_MMSS.append(max(o_MMSS))
    min_ouro_MMSS.append(min(o_MMSS))

    max_frontal_MMSS.append(max(f_MMSS))
    min_frontal_MMSS.append(min(f_MMSS))

    max_lateral_MMSS.append(max(l_MMSS))
    min_frontal_MMSS.append(min(l_MMSS))

    max_ouro_COLUNA.append(max(o_COLUNA))
    min_ouro_COLUNA.append(min(o_COLUNA))

    max_frontal_COLUNA.append(max(f_COLUNA))
    min_frontal_COLUNA.append(min(f_COLUNA))

    max_lateral_COLUNA.append(max(l_COLUNA))
    min_frontal_COLUNA.append(min(l_COLUNA))


# correlacao entre os angulos maximos de todas as variaveis de MMSS
corr_max_ouro_frontal = correlacao(max_ouro_MMSS, max_frontal_MMSS)
corr_min_ouro_frontal = correlacao(min_ouro_MMSS, min_frontal_MMSS)

corr_max_ouro_lateral = correlacao(max_ouro_MMSS, max_lateral_MMSS)
corr_min_ouro_lateral = correlacao(min_ouro_MMSS, min_lateral_MMSS)

corr_max_frontal_lateral = correlacao(max_frontal_MMSS, max_lateral_MMSS)
corr_min_frontal_lateral = correlacao(min_frontal_MMSS, min_lateral_MMSS)

# correlacao entre os angulos maximos de todas as variaveis de COLUNA
corr_max_ouro_frontal = correlacao(max_ouro_COLUNA, max_frontal_COLUNA)
corr_min_ouro_frontal = correlacao(min_ouro_COLUNA, min_frontal_COLUNA)

corr_max_ouro_lateral = correlacao(max_ouro_COLUNA, max_lateral_COLUNA)
corr_min_ouro_lateral = correlacao(min_ouro_COLUNA, min_lateral_COLUNA)

corr_max_frontal_lateral = correlacao(max_frontal_COLUNA, max_lateral_COLUNA)
corr_min_frontal_lateral = correlacao(min_frontal_COLUNA, min_lateral_COLUNA)

#-------------------- COLUNA ------------------------- #

# FLEXAO CABEÇA

corr_flexao_cabeca_ouro_frontal = correlacao(flexao_cabeca_ouro, flexao_cabeca_video_frontal)
corr_flexao_cabeca_ouro_lateral = correlacao(flexao_cabeca_ouro, flexao_cabeca_video_lateral)
corr_flexao_cabeca_frontal_lateral = correlacao(flexao_cabeca_video_frontal, flexao_cabeca_video_lateral)

# FLEXAO TRONCO

corr_flexao_tronco_ouro_frontal = correlacao(flexao_tronco_ouro, flexao_tronco_video_frontal)
corr_flexao_tronco_ouro_lateral = correlacao(flexao_tronco_ouro, flexao_tronco_video_lateral)
corr_flexao_tronco_frontal_lateral = correlacao(flexao_tronco_video_frontal, flexao_tronco_video_lateral)

# ROTAÇÃO TRONCO

corr_rot_tronco_ouro_frontal = correlacao(rotacao_tronco_ouro, rotacao_tronco_video_frontal)
corr_rot_tronco_ouro_lateral = correlacao(rotacao_tronco_ouro, rotacao_tronco_video_lateral)
corr_rot_tronco_frontal_lateral = correlacao(rotacao_tronco_video_frontal, rotacao_tronco_video_lateral)
