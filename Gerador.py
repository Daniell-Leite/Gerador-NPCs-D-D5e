import random

aparencia = random.choice([
    "Joia chamativa: brincos, colar, pulseira, braceletes",
    "Piercings",
    "Roupas extravagantes ou estrangeiras",
    "Roupas formais e limpas",
    "Roupas rasgadas e sujas",
    "Cicatriz notória",
    "Dente faltando",
    "Dedos faltando",
    "Cor de olho incomum (ou duas cores diferentes)",
    "Tatuagens",
    "Marca de nascença",
    "Cor de pele incomum",
    "Careca",
    "Barba ou cabelo trançado",
    "Cor de cabelo incomum",
    "Movimento de olhos nervoso",
    "Nariz distinto",
    "Postura distinta (torta ou rígida)",
    "Excepcionalmente belo",
    "Excepcionalmente feio",
])

defeitos_segredos = random.choice([
    "Amor perdido ou suscetível a se apaixonar",
    "Gosta de prazeres escusos",
    "Arrogante",
    "Inveja as posses ou posto de outra criatura",
    "Ganância desenfreada",
    "Inclinado a se enfurecer",
    "Tem um inimigo poderoso",
    "Fobia específica",
    "História vergonhosa ou escandalosa",
    "Crime ou delito secreto",
    "Possui conhecimento proibido",
    "Bravura imprudente",
])

dons = random.choice([
    "Toca um instrumento musical",
    "Fala diversos idiomas fluentemente",
    "Inacreditavelmente sortudo",
    "Memória perfeita",
    "Bom com animais",
    "Bom com crianças",
    "Bom em resolver enigmas",
    "Bom em um jogo",
    "Bom em imitação",
    "Desenha lindamente",
    "Pinta lindamente",
    "Canta lindamente",
    "Bebe tudo sobre a mesa",
    "Carpinteiro especialista",
    "Cozinheiro especialista",
    "Especialista em arremessar dardos e fazer pedras saltarem",
    "Malabarista especialista",
    "Ator e mestre dos disfarces perito",
    "Dançarino experiente",
    "Conhece gírias de ladrão",
])

habilidades_altas = [
    "Força – poderoso, musculoso, forte como um touro",
    "Destreza – esbelto, ágil, gracioso",
    "Constituição – resistente, robusto, sadio",
    "Inteligência – estudioso, escolado, curioso",
    "Sabedoria – perceptivo, espiritualizado, intuitivo",
    "Carisma – persuasivo, convincente, líder natural",
]
habilidades_baixas = [
    "Força – fraco, magrelo",
    "Destreza – desajeitado, desastrado",
    "Constituição – doentio, pálido",
    "Inteligência – estúpido, lento",
    "Sabedoria – esquecido, distraído",
    "Carisma – enfadonho, chato",
]

indice_habilidade_alta = random.randrange(len(habilidades_altas))
indice_habilidade_baixa = random.choice([
    indice for indice in range(len(habilidades_baixas))
    if indice != indice_habilidade_alta
])
habilidade_alta = habilidades_altas[indice_habilidade_alta]
habilidade_baixa = habilidades_baixas[indice_habilidade_baixa]

ideal_bom_mau = random.choice([
    # ideal bom
    "Beleza",
    "Caridade",
    "Bem maior",
    "Vida",
    "Respeito",
    "Auto sacrifício",
    # ideal mau
    "Dominação",
    "Ganância",
    "Força",
    "Dor",
    "Retribuição",
    "Matança",])

ideal_leal_caotico = random.choice([
    # ideal leal
    "Comunidade",
    "Justiça",
    "Honra",
    "Lógica",
    "Responsabilidade",
    "Tradição",
    # ideal caótico
    "Mudança",
    "Criatividade",
    "Liberdade",
    "Independência",
    "Sem limites",
    "Extravagância",
])

ideal_neutro_outro = random.choice([
    # ideal neutro
        "Equilíbrio",
        "Conhecimento",
        "Viva e deixe viver",
        "Moderação",
        "Neutralidade",
        "Povo",
        # outro ideal
        "Aspiração",
        "Descoberta",
        "Glória",
        "Nação",
        "Redenção",
        "Autoconhecimento",
])

maneirismos = random.choice([
    "Inclinado a cantar, assobiar ou resmungar rapidamente",
    "Fala em rimas ou de alguma outra forma peculiar",
    "Voz particularmente baixa ou alta",
    "Palavra incompreensíveis, balbucia ou gagueja",
    "Fala excessivamente clara",
    "Fala gritando",
    "Sussurros",
    "Fala de forma rebuscada ou com palavras longas",
    "Usa palavras erradas com frequência",
    "Usa injúrias e exclamações",
    "Faz piadas e trocadilhos constantemente",
    "Inclinado a previsões dramáticas",
    "Impaciente",
    "Vesgo",
    "Olhar distante",
    "Masca alguma coisa",
    "Paciente",
    "Estala os dedos",
    "Rói as unhas",
    "Enrola os cabelos ou puxa a barba",
])

tracos_interacao = [
    "Argumentativo",
    "Arrogante",
    "Barulhento",
    "Rude",
    "Curioso",
    "Amigável",
    "Honesto",
    "Esquentado",
    "Irritado",
    "Ponderado",
    "Quieto",
    "Desconfiado",
]
interacao = random.choice(tracos_interacao)

vinculo = random.choice([
    "Dedicado a completar um objetivo de vida pessoal",
    "Protege membros próximos da família",
    "Protege colegas ou compatriotas",
    "Leal a um benfeitor, patrono ou empregador",
    "Cativado por um interesse romântico",
    "Atraído por um local especial",
    "Protege uma lembrança especial",
    "Protege um bem valioso",
    "Em busca de vingança",
    "Role duas vezes, ignorando resultados iguais a 10",
])
