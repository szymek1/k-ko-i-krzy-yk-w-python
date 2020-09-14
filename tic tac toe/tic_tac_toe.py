

def plansza(mapa_gry,rzad,kolumna,gracz,wyswietl=False):
    try:
        print("   0  1  2")
        if not wyswietl:
            mapa_gry[rzad][kolumna] = gracz
            for count ,row in enumerate(mapa_gry):
                print(count, row)
                #return mapa_gry czemu jak to nie jest komentarzem, to wyświetla sie tylko pierwszy wiersz???
    except: print("wyprowadzono niepoprawną wartość")


#gra = plansza(gra,rzad=0,kolumna=1,gracz=1, wyswietl=False)


def wygrana(aktualny_stan):

    for row in aktualny_stan:
       if row.count(row[0]) == len(row) and row[0] != 0:
           print("Winner! poziomo")

    new_list = list(map(list,zip(*aktualny_stan)))
    for row in new_list:
        if row.count(row[0]) == len(row) and row[0] != 0:
            print("Winner! pionowo")

    diags = []
    for x in range(len(aktualny_stan)):
        diags.append(aktualny_stan[x][x])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print("Winner! przekątna góra")

    diags = []
    cols = list(reversed(range(len(aktualny_stan))))
    rows = range(len(aktualny_stan))
    for x in rows:
        diags.append(aktualny_stan[x][cols[x]])
        if diags.count(diags[0]) == len(diags) and diags[0] != 0:
            print("Winner! przekątna dół")




play = True
gracze = [1,2]

while play:

    gra = [[0, 0, 0], 
           [0, 0, 0], 
           [0, 0, 0],]
    
    game_won = False
    while not game_won:
        current_player = 1
        column_choice = int(input("którą kolumnę: "))
        row_choice = int(input("który rząd: "))
        gra = plansza(gra,row_choice,column_choice,current_player, wyswietl=False)
        wygrana(gra)




