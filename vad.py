def Ennama_Keela_Satham(vadivelu):
    if len(vadivelu)==0:
        return
    else:
        print(vadivelu[0],end='')
        Ennama_Keela_Satham(vadivelu[1:])
print('\n')
Ennama_Keela_Satham('Pesikitriken Mama')