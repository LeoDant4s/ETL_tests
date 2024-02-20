with open('actors.csv') as table:
    ator = ''
    mediaPorFilme = 0
    next(table)
    # Para facilitar quando precisar pesquisar
    # Actor[0],Total Gross[1],Number of Movies[2],Average per Movie[3],#1 Movie[4],Gross[5]
    for line in table:

        data = line.strip().split(',')
        #Estava dando erro em determinado nome que começava com aspas e tinha vírgula no 
        #meio, fazendo com que o split desse errado, então fiz isso pra tratar essa exceção
        if(data[0].startswith('"')):
            actor_name = data[0] + data[1]
            mediaDoAtor = float(data[4])
            if(mediaDoAtor > mediaPorFilme):
                ator = actor_name
                mediaPorFilme = mediaDoAtor
        else:
            mediaDoAtor = float(data[3])
            if(mediaDoAtor > mediaPorFilme):
                ator = data[0]
                mediaPorFilme = mediaDoAtor

    with open('etapa-3.txt', 'w') as saida:
        print("Ator com maior média de salário por filme: {}. Valor médio: {}".format(ator, mediaPorFilme), file=saida)