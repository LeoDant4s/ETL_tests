with open('actors.csv') as table:
    filmesAnalisados = {}
    next(table)
    # Para facilitar quando precisar pesquisar
    # Actor[0],Total Gross[1],Number of Movies[2],Average per Movie[3],#1 Movie[4],Gross[5]
    for line in table:

        data = line.strip().split(',')
        #Seguirei usando esse tratamento para a questão das aspas e a vírgula dentro
        if(data[0].startswith('"')):
            if(filmesAnalisados.get(data[5]) == None):
                filmesAnalisados[data[5]] = 1
            else:
                filmesAnalisados[data[5]] += 1
        else:
            if(filmesAnalisados.get(data[4]) == None):
                filmesAnalisados[data[4]] = 1
            else:
                filmesAnalisados[data[4]] += 1
    filmesAnalisados = dict(sorted(filmesAnalisados.items(), key=lambda item: (-item[1], item[0])))
    with open('etapa-4.txt', 'w') as saida:
        index = 1
        for filme, quantidade in filmesAnalisados.items():
            print("{} - O filme {} aparece {} vez(es) no dataset".format(index, filme, quantidade), file=saida)
            index+=1