from doctest import Example
from lib2to3.pgen2.token import OP
from math import fabs
import prolog as pl

def menu():    

    flag = True
    while(flag):
    
        print("\nCommands: press 'e' to esc"
            +"\n1) Visualize exoplanets list"
            +"\n2) Visualize habitable exoplanets list"
            +"\n3) Search planet"
            +"\n4) Add new exoplanet"  #to do forzare l'inserimento di tutte le feautures
            +"\n5) Check if an exoplanet is habitable"       
            +"\n6) Use induction to classify a planet")            
        
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
        elif(command == "5"):  #tramite regola        
            planet = input("\nEnter exoplanet name:\n")
            pl.isHabitable(planet)
        elif(command == "6" ):
            pl.learnHab()
            pl.learnNonHab()                      
        elif(command == "7"):
            classificationMenu()
            #far partire la classificazione
            #stampare le regole indotte
            #inserire pianeta da classificare
            #tramite induzione delle classi
        else:
            flag = False
            return

def subMenuPlanet():
    
    print("\nPress 'e' to escape\n"
          + "'d' to get a description of a chosen planet\n"
          + "'f' to get information about a feature of a chosen planet")
    
    command = input("\n> ")
    
    if(command == 'e'):
        return
    else:
        planet = input("\nEnter exoplanet name: ")
        
        if(command == 'd'):
            pl.getInfo(planet)
            
        elif(command == 'f'):
            printPlanetFeatures()            
            feature = input("\nEnter feature: ")
            pl.getFeatures(planet, feature)
            if(feature == "p"):
                subMenuStar(planet)
        

def menuAddingPlanet():    
    
    planet = input("\nEnter the name of the new exoplanet:")
    
    exit=False
    while(exit !=True):
        print("Choose the feature to enter or press 'e' to escape:")
        printPlanetFeatures()
        feature = input("> ")
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
    
##########################################################################################################################    

def classificationMenu():
    print("Enter example to classify: ")
    radius = input(" -enter radius : ",)
    mass = input(" -enter mass : ",)
    density = input(" -enter density : ",)
    gravity = input(" -enter gravity: ",)
    eqTemp = input(" -enter eq temperature : ",)
    composition = input(" -enter composition : ",)
    atmosphere = input(" -enter atmosphere : ",)
    eccentricity = input(" -enter eccentricity : ",)
    oPeriod = input(" -enter orbit period : ",)
    hzd = input(" -enter zone distance : ",)
    nStars = input(" -enter number of stars : ",)
    met = input(" -enter star metallicity : ",)
    sTemp = input(" -enter star temp : ",)
    
    massRadius = pl.getMassRadiusClass(mass, radius) #TODO AGgiustuarea
    density = pl.getDensityClass(density)
    gravity = pl.getGravityClass(gravity)
    eqTemp = pl.getETempClass(eqTemp)
    eccentricity = pl.getEccClass(eccentricity)
    oPeriod = pl.getOPeriodClass(oPeriod)
    hzd = pl.getHZDClass(hzd)
    met = pl.getMetallicityClass(met)
    sTemp = pl.getStarTempClass(sTemp)
        
    example = "[massRadius_class = "+ massRadius +", density = "+ density +", gravity = "+gravity+",  eq_temp = "+eqTemp+", composition = "+composition+", atmosphere = "+atmosphere+", eccentricity = "+eccentricity+", orbit_period_days = "+oPeriod+", zone_class = "+hzd+", num_stars = "+nStars+" ,metallicity = "+met+" , star_temp_class = "+sTemp+"]"
    #TODO usare la Tecnica proibita del viaggiatore resiliente: auto-format dei fatti da dare in pasto all'algoritmo ILP, creando da 0 il fatto..
    #..esempio(Classe, [attributo1 = valore, attr = valore, ...]) a partire da valori numerici utilizzando i mini classif. creati
   
    
    pl.classify(example)
    
    
          