from pyswip import Prolog

prolog = Prolog()
prolog.consult("C:/Users/follo/OneDrive/Documenti/GitHub/ICON-Project/KB/exo2.pl")


# funzione per richiamare la query prolog che restituisce tutti gli esopianeti
def getExoplanets():    
    myQuery = "prop(P, hostname, _)."
    planets = list(prolog.query(myQuery))          
    return planets


# funzione che stampa tutti gli esopianeti
def printExoplanets(planets):
    print("\nList of all the exoplanets:")
    for elem in planets:
        queryPlanets = "> "+ elem["P"] + ""  
        print(queryPlanets)

        
# funzione per richiamare la query prolog che restituisce tutti gli esopianeti abitabili
def getHabitableExoplanets():

    print("\nList of all the habitable exoplanets:")
    myQuery = "prop(P, is_hab_class, habitable)."
    planets = list(prolog.query(myQuery))
    for elem in planets:
        queryPlanets = "> "+ elem["P"] +""
        print(queryPlanets)


# funzione per richiamare la query prolog che restituisce una descrizione del pianeta
def getInfo(planet):  

    myQuery = "get_info_about("+ planet + ")"
    list(prolog.query(myQuery))      
        
    #prop(Planet, is_hab_class, Hab),
    #write(' is an '),
    #write(Hab),
    #write(' exoplanet in a planetary system whose star is '),
    #write(Star),
    #prop(Planet, is_mass_class, Class),
    #write(', it was classified by mass as a '),
    #write(Class),
    #prop(Planet, was_discovered_in, Year),
    #write(' and it was discovered in '),
    #write(Year).
    
    
#TO DO gestire gli errori
# funzione per richiamare la query prolog che restituisce il valore della feature indicata del pianeta dato
def getValue(planet, feature):
    
    verb = ""    
    property = feature.replace(" ", "_")    

    if(property == "equilibrium_temperature"):
        verb = "has_temp"
        myQuery = "prop(" + planet + ", " + verb + ", X)."

    elif(property == "atmosphere_type"):
        verb = "has_atmosphere"
        myQuery = "prop(" + planet + ", " + verb + ", X)."
        
    elif(property == "discovery_year"):
        verb = "was_discovered"
        myQuery = "prop(" + planet + ", " + verb + ", X)."
   
    elif(property == "planetary_system"):
        verb = "hostname"
        myQuery = "prop(" + planet + ", " + verb + ", X)."        

    else:
        verb = "has_" + property
        myQuery = "prop(" + planet + ", " + verb + ", X)."        
 
    resultQuery = list(prolog.query(myQuery))      
    for elem in resultQuery:
        result = elem["X"]        

    featureClass = featureClassification(feature, str(result)) #le funz. di classif. vogliono stringhe

    print("\nThe chosen exoplanet for the feature '" + feature + "' has value: "+str(result)+",")
    print("and belongs to the feature class: "+featureClass+"")


def featureClassification(feature, value):
    if(feature == "mass"):
        featureClass = getMassRadiusClass(value, "0") #valore "fantasma"
    elif(feature == "radius"):
        featureClass = getMassRadiusClass("0", value)
    elif(feature == "density"):
        featureClass = getDensityClass(value)
    elif(feature == "gravity"):
        featureClass = getGravityClass(value)
    elif(feature == "equilibrium temperature"):
        featureClass = getEqTempClass(value)
    elif(feature == "eccentricity"):
        featureClass = getEccClass(value)
    else:
        featureClass = "none" 

    return featureClass
    
#funzione che permette di aggiungere un pianeta
def addPlanet(planet, valueList):

    features = getFeatures()  

    for value, verb in zip(valueList, features): #prende entrambi i valori 
        
        myQuery = "prop(" + planet + ", " + verb + ", " + value + " )"        
            
        prolog.assertz(myQuery)     
   

# funzione per richiamare la query prolog che restituisce il valore della feuture indicata della stella data
def getStarFeatures(planet, feature):    
    verb = ""
    feature.strip()

    if(feature == "effectivetemperature"):
        verb = "his_star_has_temp"
        myQuery = "prop(" + planet + ", " + verb + ", X)"
        
    elif(feature == "metallicity"):
        verb = "his_star_has_met"
        myQuery = "prop(" + planet + ", " + verb + ", X)"
   
    elif(feature == "spectralclassification"):
        verb = "his_star_is_class"
        myQuery = "prop(" + planet + ", " + verb + ", X)"

    resultQuery = list(prolog.query(myQuery))
    for elem in resultQuery:
        result = elem["X"]            
        print("The metallicity of the chosen star is: " + result)  
        
#######################################################################################################################################################################

def learn():    
    myQuery = "apprendi(habitable)"  
    list(prolog.query(myQuery))    

    myQuery = "apprendi(non_habitable)"   
    list(prolog.query(myQuery))  


# funzione per richiamare la funzione classify tramite algoritmo ILP (inductive logic programming) 
def classify(example):    
    myQuery = "classifica(" + example +", Classe)"   
    prolog.query(myQuery)
    resultQuery = list(prolog.query(myQuery))
    for elem in resultQuery:
       result = elem["Classe"]            
    return result
    
# funzione per richiamare una classif
def getDensityClass(density):
    myQuery = "prop("+density+", density_is_class, C)"
    resultQuery = list(prolog.query(myQuery))
    for elem in resultQuery:
        result = elem["C"]               
        
        return result

# funzione per richiamare una classif
def getGravityClass(gravity):
    myQuery = "prop("+gravity+", gravity_is_class, C)"
    resultQuery = list(prolog.query(myQuery))
    for elem in resultQuery:
        result = elem["C"]                
   
        return result

# funzione per richiamare una classif
def getEqTempClass(eqTemp):
    myQuery = "prop("+eqTemp+", temp_is_class, C)"
    resultQuery = list(prolog.query(myQuery))
    for elem in resultQuery:
        result = elem["C"]                 
       
        return result
        
# funzione per richiamare una classif
def getEccClass(eccentricity):
    myQuery = "prop("+eccentricity+", eccentricity_is_class, C)"
    resultQuery = list(prolog.query(myQuery))
    for elem in resultQuery:
        result = elem["C"]                 
     
        return result

# funzione per richiamare una classif
def getOPeriodClass(operiod):
    myQuery = "prop("+operiod+", operiod__is_class, C)"
    resultQuery = list(prolog.query(myQuery))
    for elem in resultQuery:
        result = elem["C"]                 
    
        return result   

# funzione per richiamare una classif
def getMetallicityClass(metallicity):
    myQuery = "prop("+metallicity+", metallicity_is_class, C)"
    resultQuery = list(prolog.query(myQuery))
    for elem in resultQuery:
        result = elem["C"]                 
    
        return result
        
# funzione che richiama la classificazione per massa/raggio del pianeta
def getMassRadiusClass(mass, radius): 
    myQuery = "prop("+"["+mass+"|"+radius+"]"+", massRadius_is_class, C)"
    resultQuery = list(prolog.query(myQuery))
    for elem in resultQuery:
        result = elem["C"]                 
       
        return result

# funzione per richiamare una classif
def getHZDClass(operiod):
    myQuery = "prop("+operiod+", habitability_is_class, C)"
    resultQuery = list(prolog.query(myQuery))
    for elem in resultQuery:
        result = elem["C"]                 
    
        return result

# funzione che richiama la classificazione spettrale della stella
def getStarTempClass(starTemp):
    myQuery = "prop("+starTemp+", starTemp_is_class, C)"
    resultQuery = list(prolog.query(myQuery)) #prologilp
    for elem in resultQuery:
        result = elem["C"]        
        
        return result

        
def getFeatures(): #n potrei anche usare query prolog ma le features sono sempre le stesse...

    features = ["hostname", "has_radius", "has_mass", "has_density", "has_gravity", "has_temp", "has_composition", "has_atmosphere",
    "has_eccentricity", "has_orbit_period", "distance_from_star", "has_stars_in_sys", "his_star_has_met", "his_star_has_temp", "is_hab_class"]  

    return features


def classifyValues(radius, mass, density, gravity, eqTemp, eccentricity, oPeriod, hzd, met, sTemp):

    massRadius = getMassRadiusClass(mass, radius)
    densityClass = getDensityClass(density)
    gravityClass = getGravityClass(gravity)
    eqTempClass = getEqTempClass(eqTemp)
    eccentricityClass = getEccClass(eccentricity)
    oPeriodClass = getOPeriodClass(oPeriod)
    hzdClass = getHZDClass(hzd)
    metClass = getMetallicityClass(met)
    sTempClass = getStarTempClass(sTemp)
    
    return massRadius, densityClass, gravityClass, eqTempClass, eccentricityClass, oPeriodClass, hzdClass, metClass, sTempClass

def classifyExample(example):   

    resultClass = classify(example)
    print("The exoplanet entered belongs to the class: " + resultClass)

    return resultClass 


def listProp(planetList):

    features = getFeatures()

    # non creo manualmente lista dei pianeti perchè lista non statica, se ne possono aggiungere altri 
    planets = [] # lista dei pianeti creata a partire dal risultato (planetList) di una query precedente
    for elem in planetList:
        planets.append(elem["P"])    
 
    #per ogni pianeta e per ogni feature cerco il valore corrispondente
    for p in planets: 
        values = []  #lista dei valori
        for f in features:                         
            myQuery = "prop("+ p +","+ f +", V)."
            resultQuery = prolog.query(myQuery)    
            for elem in resultQuery:
                values.append(str(elem["V"]))     #aggiungo man mano i valori alla lista in formato stringa
        #print("\nvalues for: ", p, "= ", values)                      
        transform(values)        

        
#TODO IMPLEMENTAZIONE FUTURA ?: cambiare struttura dati, magari HashMap {feature: value}
def transform(values):
  
    massRadius, densityClass, gravityClass, eqTempClass, eccentricityClass, oPeriodClass, hzdClass, metClass, sTempClass = classifyValues(values[1], values[2], values[3], values[4], values[5], values[8], values[9], values[10], values[12], values[13])      
        
    exampleFact = "esempio("+values[14]+", [massRadius_class = "+ massRadius +", density = "+ densityClass +", gravity = "+gravityClass+",  eq_temp = "+eqTempClass+", composition = "+values[6]+", atmosphere = "+values[7]+", eccentricity = "+eccentricityClass+", orbit_period_days = "+oPeriodClass+", zone_class = "+hzdClass+", num_stars = "+values[11]+", metallicity = "+metClass+", star_temp_class = "+sTempClass+"])"
    prolog.assertz(exampleFact)

    ################################   TODO: FINIRE DI RISCRIVERLI NELLA KB IN FORMATO PROP(...)   ############################################    
    #hd283869
    exampleFact = "esempio(habitable, [massRadius_class = superterran, density = medium, gravity = medium, eq_temp = acceptable, composition = rocky_iron, atmosphere = metals_rich, eccentricity = circular, orbit_period_days = a_lot, zone_class = warm, num_stars = 1, metallicity = low, star_temp_class = k])"
    prolog.assertz(exampleFact)
    #k272e
    exampleFact = "esempio(habitable, [massRadius_class = terran, density = medium, gravity = weak, eq_temp = acceptable, composition = rocky_iron, atmosphere = metals_rich, eccentricity = circular, orbit_period_days = a_lot, zone_class = warm, num_stars = 4, metallicity = medium, star_temp_class = m])"
    prolog.assertz(exampleFact)
    #kepler61b
    exampleFact = "esempio(habitable, [massRadius_class = superterran, density = medium, gravity = medium, eq_temp = acceptable, composition = rocky_iron, atmosphere = hydrogene_rich, eccentricity = elliptic, orbit_period_days = a_lot, zone_class = warm, num_stars = 1, metallicity = low, star_temp_class = k])"
    prolog.assertz(exampleFact)
    #kepler443
    exampleFact = "esempio(habitable, [massRadius_class = superterran, density = medium, gravity = strong, eq_temp = acceptable, composition = rocky_iron, atmosphere = hydrogene_rich, eccentricity = elliptic, orbit_period_days = a_lot, zone_class = warm, num_stars = 1, metallicity = medium, star_temp_class = k])"
    prolog.assertz(exampleFact)
    #wolf1071c
    exampleFact = "esempio(habitable, [massRadius_class = terran, density = medium, gravity = medium, eq_temp = acceptable, composition = rocky_iron, atmosphere = metals_rich, eccentricity = elliptic, orbit_period_days = many, zone_class = warm, num_stars = 3, metallicity = low, star_temp_class = m])"
    prolog.assertz(exampleFact)

    ##############

    #gj163c (psychroplanet TUTTI)
    exampleFact = "esempio(habitable, [massRadius_class = superterran, density = medium, gravity = medium, eq_temp = acceptable, composition = rocky_iron, atmosphere = metals_rich, eccentricity = elliptic, orbit_period_days = a_lot, zone_class = warm, num_stars = 3, metallicity = low, star_temp_class = k])"
    prolog.assertz(exampleFact)
    #gj367Ce
    exampleFact = "esempio(habitable, [massRadius_class = terran, density = medium, gravity = weak, eq_temp = acceptable, composition = rocky_iron, atmosphere = metals_rich, eccentricity = elliptic, orbit_period_days = a_lot, zone_class = warm, num_stars = 6, metallicity = low, star_temp_class = m])"
    prolog.assertz(exampleFact)
    #kapteynB
    exampleFact = "esempio(habitable, [massRadius_class = terran, density = medium, gravity = medium, eq_temp = acceptable, composition = rocky_iron, atmosphere = metals_rich, eccentricity = elliptic, orbit_period_days = a_lot, zone_class = warm, num_stars = 2, metallicity = medium, star_temp_class = m])"
    prolog.assertz(exampleFact)
    #trappist1e
    exampleFact = "esempio(habitable, [massRadius_class = terran, density = medium, gravity = weak, eq_temp = acceptable, composition = rocky_iron, atmosphere = metals_rich, eccentricity = circular, orbit_period_days = few, zone_class = warm, num_stars = 7, metallicity = low, star_temp_class = m])"
    prolog.assertz(exampleFact)
    #kepler1652b
    exampleFact = "esempio(habitable, [massRadius_class = terran, density = medium, gravity = weak, eq_temp = acceptable, composition = rocky_iron, atmosphere = metals_rich, eccentricity = circular, orbit_period_days = a_lot, zone_class = warm, num_stars = 1, metallicity = low, star_temp_class = m])"
    prolog.assertz(exampleFact)
    #kepler442b
    exampleFact = "esempio(habitable, [massRadius_class = terran, density = medium, gravity = weak, eq_temp = acceptable, composition = rocky_iron, atmosphere = metals_rich, eccentricity = elliptic, orbit_period_days = a_lot, zone_class = warm, num_stars = 1, metallicity = medium, star_temp_class = k])"
    prolog.assertz(exampleFact)
    #kepler1229b
    exampleFact = "esempio(habitable, [massRadius_class = terran, density = medium, gravity = weak, eq_temp = acceptable, composition = rocky_iron, atmosphere = metals_rich, eccentricity = circular, orbit_period_days = a_lot, zone_class = warm, num_stars = 1, metallicity = low, star_temp_class = k])"
    prolog.assertz(exampleFact)
    #proximaCenB
    exampleFact = "esempio(habitable, [massRadius_class = terran, density = medium, gravity = weak, eq_temp = acceptable, composition = rocky_iron, atmosphere = metals_rich, eccentricity = circular, orbit_period_days = many, zone_class = warm, num_stars = 1, metallicity = medium, star_temp_class = m])"
    prolog.assertz(exampleFact)

    #################

    #gj86ab
    exampleFact = "esempio(non_habitable, [massRadius_class = jovian, density = medium, gravity = strong, eq_temp = too_high, composition = gas, atmosphere = hydrogene_rich, eccentricity = elliptic, orbit_period_days = many, zone_class = hot, num_stars = 1, metallicity = low, star_temp_class = g])"
    prolog.assertz(exampleFact)   
    #gj581b
    exampleFact = "esempio(non_habitable, [massRadius_class = neptunian, density = low, gravity = weak, eq_temp = too_high, composition = gas, atmosphere = metals_rich, eccentricity = circular, orbit_period_days = few, zone_class = hot, num_stars = 3, metallicity = medium, star_temp_class = m])"
    prolog.assertz(exampleFact)
    #hd38283b
    exampleFact = "esempio(non_habitable, [massRadius_class = jovian, density = low, gravity = medium, eq_temp = too_high, composition = gas, atmosphere = hydrogene_rich, eccentricity = elliptic, orbit_period_days = a_lot, zone_class = hot, num_stars = 1, metallicity = medium, star_temp_class = g])"
    prolog.assertz(exampleFact)
    #k217b
    exampleFact = "esempio(non_habitable, [massRadius_class = superterran, density = medium, gravity = strong, eq_temp = too_high, composition = rocky_iron, atmosphere = metals_rich, eccentricity = circular, orbit_period_days = many, zone_class = hot, num_stars = 1, metallicity = low, star_temp_class = k])"
    prolog.assertz(exampleFact)
    #kepler68b
    exampleFact = "esempio(non_habitable, [massRadius_class = jovian, density = low, gravity = medium, eq_temp = too_high, composition = gas, atmosphere = hydrogene_rich, eccentricity = elliptic, orbit_period_days = a_lot, zone_class = warm, num_stars = 3, metallicity = medium, star_temp_class = g])"
    prolog.assertz(exampleFact)
    #wasp80b
    exampleFact = "esempio(non_habitable, [massRadius_class = jovian, density = low, gravity = medium, eq_temp = too_high, composition = gas, atmosphere = hydrogene_rich, eccentricity = elliptic, orbit_period_days = few, zone_class = hot, num_stars = 1, metallicity = medium, star_temp_class = k])"
    prolog.assertz(exampleFact)
        