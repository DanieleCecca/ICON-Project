from math import fabs
import prolog as pl


def menu():    
    
        print("\nCommands: press 'e' to esc"
            +"\n1) Visualize exoplanets list"
            +"\n2) Visualize habitable exoplanets list"
            +"\n3) Search planet"
            +"\n4) Add new exoplanet" 
            +"\n5) Check if an exoplanet is habitable")                
               #6)indovina pianeta abitabile
        
        command = input("\n> ")
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
            planet = input("\nEnter exoplanet name:\n")
            pl.isHabitable(planet)
        else:
            return

def subMenuPlanet():
    
    print("\nPress 'e' to escape\n"
          + "'d' to get a description of a chosen planet\n"
          + "'f' to get information about a feature of a chosen planet")
    
    command = input("\n> ")
    
    if(command == 'e'):
        return
    else:
        planet = input("\nEnter exoplanet name:\n")
        
        if(command == 'd'):
            pl.getInfo(planet)
            
        elif(command == 'f'):
            printPlanetFeatures()            
            feature = input("\nEnter feature : ")
            pl.getFeatures(planet, feature)
            if(feature=="p"):
                subMenuStar(planet)
        

def menuAddingPlanet():    
    
    planet = input("\nEnter the name of the new exoplanet:")
    
    exit=False
    while(exit !=True):
        print("Choose the feature to enter or press 'e' to escape:")
        printPlanetFeatures()
        feature = input()
        if(feature == "e"):           
            flag = True
            break            
        else:         
            value = input("\nEnter value: ")        
            pl.addPlanet(planet,feature,value)

    
def printPlanetFeatures():
    print("\nFeatures:"
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
          + "f to get information about a feature of a chosen star")
    
    command = input()
    
    if(command == 'e'):
        return   
    elif(command == 'f'):
        printStarFeatures()       
        feature = input("\nEnter feature: ")
        pl.getStarFeatures(planet, feature)


def printStarFeatures():
    print("Features of the star:"
          +"\n- metallicity"
          +"\n- effective temperature"
          +"\n- spectral classification")   
    
    
    
