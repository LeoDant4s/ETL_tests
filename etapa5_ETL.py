with open('actors.csv') as table:
    atores = {}
    next(table)
    # Para facilitar quando precisar pesquisar
    # Actor[0],Total Gross[1],Number of Movies[2],Average per Movie[3],#1 Movie[4],Gross[5]
    for line in table:

        data = line.strip().split(',')
        #Seguirei usando esse tratamento para a questão das aspas e a vírgula dentro
        if(data[0].startswith('"')):
            name = data[0]+data[1]
            atores[name] = data[2]
        else:
            atores[data[0]] = data[1]
    atores = dict(sorted(atores.items(), key=lambda item: item[1], reverse=True))
    with open('etapa-5.txt', 'w') as saida:
        for ator, receita in atores.items():
            print("{} - {}".format(ator, receita), file=saida)
