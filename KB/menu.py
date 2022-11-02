from doctest import Example
from lib2to3.pgen2.token import OP
from math import fabs
import prolog as pl

def menu():       
    
    flag = True

    while(flag):
    
        print("\nCommands: press 'e' to esc"
            +"\n1) Visualize exoplanets list"
            +"\n2) [TODO] Visualize habitable exoplanets list"
            +"\n3) Search planet"
            +"\n4) [TODO] Add new exoplanet"  
            +"\n5) Classify an exoplanet using ILP")                 
        
        command = input("\n> ")

        planetList = pl.getExoplanets() 
        initialization(planetList)

        if(command == "1"):            
            pl.printExoplanets(planetList)
            subMenuPlanet()
        elif(command == "2"):
            pl.getExoplanetsHabitable()
            subMenuPlanet()
        elif(command == "3"):
            subMenuPlanet() 
        elif(command == "4"):
            menuAddingPlanet()
        elif(command == "5"):       
            initialization(planetList)
            classificationMenu()                
        elif(command == "e"):
            flag = False             
        else:
            print("\nWrong command!")
            

def initialization(planetList):
    pl.learn()              
    pl.listProp(planetList) #converte i fatti nel formato prop in quello necessario per algo ILP
    pl.prolog.query("forall(esempio(C,O),format('esempio(~w, ~w)~n', [C,O]))") #rende i fatti asseriti "accessibili" all'algo ILP    
    

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
    exit = False
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

def menuAddingPlanet2():

    planet,has_radius,has_mass,has_density,has_gravity,has_temp,has_composition,has_atmosphere,has_eccentricity,has_orbit_period,distance_from_star,has_stars_in_sys,his_star_has_met,his_star_has_temp = inputExample()
    
    #sai se è abitabile?
        # Y -> inserisci classe hab.
        # N -> chiama funz. di classificaz.

    response = input("Do you know if this exoplanet is habitable or not? [y/n]")

    if(response == "y"):
        is_hab_class = input("> enter habitability class [habitable/non_habitable]")

    elif(response == "n"):
        massRadius, densityClass, gravityClass, eqTempClass, eccentricityClass, oPeriodClass, hzdClass, metClass, sTempClass = classifyValues(has_radius,has_mass,has_density,has_gravity,has_temp,has_composition,has_atmosphere,has_eccentricity,has_orbit_period,distance_from_star,has_stars_in_sys,his_star_has_met,his_star_has_temp)      
        example = "[massRadius_class = "+ massRadius +", density = "+ densityClass +", gravity = "+gravityClass+",  eq_temp = "+eqTempClass+", composition = "+has_composition+", atmosphere = "+has_atmosphere+", eccentricity = "+eccentricityClass+", orbit_period_days = "+oPeriodClass+", zone_class = "+hzdClass+", num_stars = "+has_stars_in_sys+", metallicity = "+metClass+", star_temp_class = "+sTempClass+"]"
        resultClass = pl.classify(example)


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

    radius, mass, density, gravity, eqTemp, composition, atmosphere, eccentricity, oPeriod, hzd, nStars, met, sTemp = inputExample()

    #i valori numerici inseriti vengono classificati
    massRadius, densityClass, gravityClass, eqTempClass, eccentricityClass, oPeriodClass, hzdClass, metClass, sTempClass = classifyValues(radius, mass, density, gravity, eqTemp, eccentricity, oPeriod, hzd, met, sTemp)

    #esempio che sarà asserito nella KB e classificato (hab/non_hab) 
    example = "[massRadius_class = "+ massRadius +", density = "+ densityClass +", gravity = "+gravityClass+", eq_temp = "+eqTempClass+", composition = "+composition+", atmosphere = "+atmosphere+", eccentricity = "+eccentricityClass+", orbit_period_days = "+oPeriodClass+", zone_class = "+hzdClass+", num_stars = "+nStars+", metallicity = "+metClass+", star_temp_class = "+sTempClass+"]"
    
    classifyExample(example)  #risultato classificazione hab. class 

    
def inputExample():

    print("Enter an example to classify: ")   

    radius = input("> enter radius: ",)
    mass = input("> enter mass: ",)
    density = input("> enter density: ",)
    gravity = input("> enter gravity: ",)
    eqTemp = input("> enter equilibrium temperature: ",)
    composition = input("> enter composition: ",)
    atmosphere = input("> enter atmosphere: ",)
    eccentricity = input("> enter eccentricity: ",)
    oPeriod = input("> enter orbit period: ",)
    hzd = input("> enter zone distance: ",)
    nStars = input("> enter number of stars: ",)
    met = input("> enter star metallicity: ",)
    sTemp = input("> enter star temperature: ",)

    return radius, mass, density, gravity, eqTemp, composition, atmosphere, eccentricity, oPeriod, hzd, nStars, met, sTemp


def classifyValues(radius, mass, density, gravity, eqTemp, eccentricity, oPeriod, hzd, met, sTemp):

    massRadius = pl.getMassRadiusClass(mass, radius)
    densityClass = pl.getDensityClass(density)
    gravityClass = pl.getGravityClass(gravity)
    eqTempClass = pl.getETempClass(eqTemp)
    eccentricityClass = pl.getEccClass(eccentricity)
    oPeriodClass = pl.getOPeriodClass(oPeriod)
    hzdClass = pl.getHZDClass(hzd)
    metClass = pl.getMetallicityClass(met)
    sTempClass = pl.getStarTempClass(sTemp)
    
    return massRadius, densityClass, gravityClass, eqTempClass, eccentricityClass, oPeriodClass, hzdClass, metClass, sTempClass

def classifyExample(example):   

    resultClass = pl.classify(example)
    print("The exoplanet entered belongs to the class: " + resultClass) 