with open('actors.csv') as table:
    #Decidi organizar os filmes em um array para evitar a repetição, 
    #já que podem ter atores com mesmo filme em questão, as outras variáveis são para a média no final
    receitaTotal = 0
    quantidadeDeFilmes = 0
    next(table)
    # Para facilitar quando precisar pesquisar
    # Actor[0],Total Gross[1],Number of Movies[2],Average per Movie[3],#1 Movie[4],Gross[5]
    for line in table:

        data = line.strip().split(',')
        #Seguirei usando esse tratamento para a quesstão das aspas e a vírgula dentro
        if(data[0].startswith('"')):
            quantidadeDeFilmes +=1
            receitaTotal += float(data[6])
        else:
            quantidadeDeFilmes +=1
            receitaTotal += float(data[5])
    mediaPorFilmes = receitaTotal/quantidadeDeFilmes
    with open('etapa-2.txt', 'w') as saida:
        print("Média de receita de bilheteria bruta dos principais filmes {}".format(round(mediaPorFilmes, 2)), file=saida)