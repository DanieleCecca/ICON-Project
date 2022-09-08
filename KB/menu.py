from math import fabs
import prolog as pl


def menu():
    while(True):
    
        print("Commands: press u cazz ca ue per uscire"
            +"\n1)visualize exo-planets list"
            +"\n2)visualize habitable exo-planets list"
            +"\n3)add new exoplanet"
            +"\n4)Search planet"
            +"\n5)Check if planet is habitable")
                
            #indovina pianeta abitabile

        command = input()
        if(command == "1"):
            pl.getExoplanets()
            subMenuPlanet()
        elif(command == "2"):
            pl.getExoplanetsHabitable()
            subMenuPlanet()
        elif(command == "3"):
            subMenuPlanet() 
        elif(command == "4"):
            menuAddingPlanet()
        elif(command == "5"):
            print("Insert planet name:")
            planet = input()
            pl.isHabitable(planet)
        else:
            return
        
        
        
    


def subMenuPlanet():
    
    print("Press e to escape\n"
          + "d to get a description of a chosen planet\n"
          + "f to get information about a feauture of a chosen planet")
    
    command = input()
    
    if(command=='e'):
        return
    else:
        print("Insert planet name:")
        planet = input()
        
        if(command == 'd'):
            pl.getInfo(planet)
            
        elif(command == 'f'):
            printPlanetFeautures()
            print("\nInsert feauture : ")
            feauture = input()
            pl.getFeautures(planet, feauture)
            if(feauture=="p"):
                subMenuStar(planet)
        

def menuAddingPlanet():
    
    print("Insert new exoplanet name:")
    planet = input()
    
    exit=False
    while(exit !=True):
        print("Chose the feauture to insert or press 'e' to escape:")
        printPlanetFeautures()
        feauture = input()
        if(feauture == "e"):           
            flag = True
            break
            
        else:
            print("Insert value:")
            value = input()
        
            pl.addPlanet(planet,feauture,value)
    
def printPlanetFeautures():
    print("Feautures:"
          +"\n- radius"
          +"\n- mass"
          +"\n- density"
          +"\n- volume"
          +"\n- gravity"
          +"\n- equilibrium temperature"
          +"\n- composition"
          +"\n- atmosphere type"
          +"\n- orbit period"
          +"\n- eccentricity"
          +"\n- discovery year"
          +"\n- planetary system")
    


def subMenuStar(planet):
    
    print("Press e to escape\n"
          + "f to get information about a feauture of a chosen star")
    
    command = input()
    
    if(command=='e'):
        return   
    elif(command == 'f'):
        printStarFeautures()
        print("\nInsert feauture : ")
        feauture = input()
        pl.getStarFeautures(planet, feauture)


def printStarFeautures():
    print("Feautures:"
          +"\n- metallicity"
          +"\n- effective temperature"
          +"\n- spectral classification")   
    
    
    
