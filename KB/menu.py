from lib2to3.pgen2.token import OP
import prolog as pl

import streamlit as st

def menu():       
    
    flag = True   

    while(flag):
    
        print("\nCommands available:"
            +"\n1) Visualize exoplanets list"
            +"\n2) Visualize habitable exoplanets list"
            +"\n3) Search for an exoplanet"
            +"\n4) Add a new exoplanet"  
            +"\n5) Classify an exoplanet: is it habitable or not?")        
        
        command = input("\nEnter a command...\n> ")

        planetList = pl.getExoplanets() #posizione corretta: aggiorna lista pianeti dopo che è uscito da addPlanet()
        initialization(planetList) 

        if(command == "1"):      
            pl.printExoplanets(planetList)
            subMenuPlanet()
        elif(command == "2"):
            pl.getHabitableExoplanets()            
        elif(command == "3"):
            subMenuPlanet() 
        elif(command == "4"):
            menuAddingPlanet()
        elif(command == "5"):  
            classificationMenu()                
        elif(command == "e"):
            flag = False             
        else:
            print("\nWrong command!")
            

def initialization(planetList):                  
    pl.listProp(planetList) #converte i fatti nel formato prop in quello necessario per algo ILP
    pl.learn()   
        

def subMenuPlanet():
    
    print("\nPress 'e' to escape\n"
          + "'d' to get a brief description of a chosen planet\n"
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
            pl.getValue(planet, feature)

            res = input("\nDo you want to know something about his star either? [y/n]\n> ")
            if(res == "y"):
                subMenuStar(planet)
            else:
                return
        

def menuAddingPlanet():

    valueList = []
    is_hab_class = ""

    planet = input("\nEnter the name of the exoplanet to add to the Knowledge Base:\n> ")
    hostname = input("\nWhat is the name of the star system where " + planet + " is located?\n> ")
    year = input("\nIn which year its discovery was announced?\n> ")

    has_radius,has_mass,has_density,has_gravity,has_temp,has_composition,has_atmosphere,has_eccentricity,has_orbit_period,distance_from_star,planets_in_sys,his_star_has_met,his_star_has_temp = inputExample()
    valueList.extend([hostname,has_radius,has_mass,has_density,has_gravity,has_temp,has_composition,has_atmosphere,has_eccentricity,has_orbit_period,distance_from_star,planets_in_sys,his_star_has_met,his_star_has_temp, year, ""])  

    featureDict = pl.createDict(valueList)
    
    #sai se è abitabile?
        # Y -> inserisci classe hab.
        # N -> chiama funz. di classificaz.

    response = input("\nDo you know if this exoplanet is habitable or not? [y/n]:\n> ")

    if(response == "y"):
        is_hab_class = input("\nEnter habitability class [habitable/non_habitable]:\n> ")        

    elif(response == "n"):
        massRadius, densityClass, gravityClass, eqTempClass, eccentricityClass, oPeriodClass, hzdClass, metClass, sTempClass = pl.classifyValues(featureDict)      
        example = "[massRadius_class = "+ massRadius +", density = "+ densityClass +", gravity = "+gravityClass+",  eq_temp = "+eqTempClass+", composition = "+has_composition+", atmosphere = "+has_atmosphere+", eccentricity = "+eccentricityClass+", orbit_period_days = "+oPeriodClass+", zone_class = "+hzdClass+", num_planets = "+planets_in_sys+", metallicity = "+metClass+", star_temp_class = "+sTempClass+"]"
        is_hab_class = pl.classifyExample(example)
    else:
        print("Wrong command!")
        return

    valueList.pop()
    valueList.append(is_hab_class)
    print(valueList)
    #print(is_hab_class)
    pl.addPlanet(planet, valueList)

    print("\nExoplanet: inserted")

def printPlanetFeatures():
    st.write("\nFeatures:"
          +"\n- radius"
          +"\n- mass"
          +"\n- density"
          +"\n- gravity"
          +"\n- equilibrium temperature"
          +"\n- composition"
          +"\n- atmosphere type"
          +"\n- orbit period"
          +"\n- eccentricity"
          +"\n- discovery year"    
          +"\n- planetary system")  


def subMenuStar(planet):
    
    print("\nPress 'e' to escape\n"
          + "'f' to get information about a feature of a chosen star")
    
    command = input("> ")
    
    if(command == 'e'):
        return   

    elif(command == 'f'):
        printStarFeatures()       
        feature = input("\nEnter feature: ")
        pl.getStarFeatures(planet, feature)


def printStarFeatures():
    st.write("Features of the star:"
          +"\n- metallicity"
          +"\n- effective temperature"
          +"\n- planets in system"
          +"\n- spectral classification")   

##########################################################################################################################    

def classificationMenu():

    print("\nEnter an example to classify: ") 

    featureDict = classificationInput()

    #i valori numerici inseriti vengono classificati
    massRadius, densityClass, gravityClass, eqTempClass, eccentricityClass, oPeriodClass, hzdClass, metClass, sTempClass = pl.classifyValues(featureDict)

    #esempio che sarà asserito nella KB e classificato (hab/non_hab) 
    example = "[massRadius_class = "+ massRadius +", density = "+ densityClass +", gravity = "+gravityClass+", eq_temp = "+eqTempClass+", composition = "+featureDict["composition"]+", atmosphere = "+featureDict["atmosphere"]+", eccentricity = "+eccentricityClass+", orbit_period_days = "+oPeriodClass+", zone_class = "+hzdClass+", num_planets = "+featureDict["numPlanets"]+", metallicity = "+metClass+", star_temp_class = "+sTempClass+"]"
    
    pl.classifyExample(example)  #risultato classificazione hab. class 


#funzione restituisce un dizionario che contiene le feature come chiavi e come valori quelli inseriti in input
def classificationInput():

    values = []
    radius, mass, density, gravity, eqTemp, composition, atmosphere, eccentricity, oPeriod, hzd, nPlanets, met, sTemp = inputExample()  
    
    values.extend(["",radius,mass,density,gravity,eqTemp,composition,atmosphere,eccentricity,oPeriod,hzd,nPlanets,met,sTemp,"",""])
    featureDict = pl.createDict(values)

    return featureDict

    
def inputExample():    

    print("\nNB] in the square brackets we suggest the typical values for each feature")  

    radius = input("\n> enter radius [> 0]: ",)
    mass = input("> enter mass [> 0]: ",)
    density = input("> enter density [> 0]: ",)
    gravity = input("> enter gravity [> 0]: ",)
    eqTemp = input("> enter equilibrium temperature [> 200]: ",)
    composition = input("> enter composition [gas/rocky_iron/rocky_water]: ",)
    atmosphere = input("> enter atmosphere [hydrogene_rich/metals_rich]: ",)
    eccentricity = input("> enter eccentricity [>= 0]: ",)
    oPeriod = input("> enter orbit period [> 0]: ",)
    hzd = input("> enter zone distance [-3, 3]: ",)
    nPlanets = input("> enter number of planets [1, 7]: ",)
    met = input("> enter star metallicity [-2, 2]: ",)
    sTemp = input("> enter star temperature [> 2000]: ",)

    return radius, mass, density, gravity, eqTemp, composition, atmosphere, eccentricity, oPeriod, hzd, nPlanets, met, sTemp
