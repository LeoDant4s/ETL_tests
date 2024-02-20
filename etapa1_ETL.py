with open('actors.csv') as table:
    ator = ''
    numeroDeFilmes = 0
    next(table)
    # Para facilitar quando precisar pesquisar
    # Actor[0],Total Gross[1],Number of Movies[2],Average per Movie[3],#1 Movie[4],Gross[5]
    for line in table:

        data = line.strip().split(',')
        #Estava dando erro em determinado nome que começava com aspas e tinha vírgula no 
        #meio, fazendo com que o split desse errado, então fiz isso pra tratar essa exceção
        if(data[0].startswith('"')):
            actor_name = data[0] + data[1]
            if(int(data[3]) > numeroDeFilmes):
                ator = actor_name
                numeroDeFilmes = int(data[3])
        else:
            if(int(data[2]) > numeroDeFilmes):
                ator = data[0]
                numeroDeFilmes = int(data[2])
    with open('etapa-1.txt', 'w') as saida:
        print("Ator com mais filmes: {}. Quantidade de filmes: {}".format(ator, numeroDeFilmes), file=saida)