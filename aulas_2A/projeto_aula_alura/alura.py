""""

Idade do cliente;
Classificação indicativa do filme.
No exemplo do cinema, a saída esperada poderia ser:

Exibir "Entrada permitida" caso a idade seja igual ou superior à classificação indicativa;
Exibir "Entrada não permitida" caso contrário.

Em um campeonato de videogame, o vencedor é determinado pela maior pontuação.
Leia o código a seguir, que representa o funcionamento dessa pontuação,
e observe que ele apresenta uma lacuna:
"""


def encontra_vencedor(pontuacao1, pontuacao2, pontuacao3): 

    maior_pontuacao = max(pontuacao1, pontuacao2, pontuacao3) 

    return maior_pontuacao 