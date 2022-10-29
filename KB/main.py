import menu   
    
if __name__ == '__main__':
   menu.menu()


#comandi principali menu

#1 Lista pianeti
    #dato un pianeta puoi inferenziare su tutte le caratteristiche oppure chiedere una descizione completa oppure exit tra cui l'hostname
        #scelto l'hostname si può inferenziare sulle feautures della stella 
            #TODO atm funziona solamente con il formato "prop(...)" e non con "esempio(...)", poichè:
                #- non sono identificati da un nome
                #- e anche se lo fossero, non sono nel formato giusto --> risolvibile usando 'TPVR'
        
#2 Lista pianeti abitabili   ---> TODO togliere o modificare?
    #dato un pianeta puoi inferenziare su tutte le caratteristiche oppure chiedere una descizione completa oppure exit tra cui l'hostname
            #scelto l'hostname si può inferenziare sulle feautures della stella
            
#3 Dato un pianeta puoi inferenziare su tutte le caratteristiche tra cui l'hostname   
    #scelto l'hostname si può inferenziare sulle feautures della stella
    
#4 Aggiungi un pianeta  ---> TODO forzare l'inserimento di tutte le feautures

#5 Pianeta scelto abitabile? ---> TODO togliere o modificare?

#6 Induzione Logica per classificazione... 
    #TODO:
        #- aggiungere nuovi esempi
     
        #- usare la Tecnica Proibita del Viaggiatore Resiliente: auto-format dei fatti da dare in pasto all'algoritmo ILP, creando da 0 il fatto..
        #..esempio(Classe, [attributo1 = valore, attr = valore, ...]) a partire da valori numerici utilizzando i mini classif. creati 
