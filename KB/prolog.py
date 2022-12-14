from pyswip import Prolog

prolog = Prolog()
prolog.consult("exo2.pl")


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


#TODO si rompe se cercato pianeta inserito: non abbastanza info
# funzione che restituisce una breve descrizione del pianeta
def getInfo(planet):  

    selectedFeatures = ["is_hab_class", "hostname", "was_discovered_in", "has_mass", "has_radius"]
    values = []  

    for f in selectedFeatures:
        myQuery = "prop("+ planet + ", "+ f +", V)"
        resultQuery = prolog.query(myQuery)
        for elem in resultQuery:
            values.append(str(elem["V"]))

    featureDict = {"hab": values[0], "star": values[1], "year": values[2], "mass": values[3], "radius": values[4]}

    massRadiusClass = getMassRadiusClass(featureDict["mass"], featureDict["radius"])

    print("\n"+ planet + " is a " + featureDict["hab"]+ " exoplanet discovered in " + featureDict["year"] + " and it is in a planetary system" +
    " whose star is " + featureDict["star"] + ".\nIt is a " + massRadiusClass +"-like planet.")    

        
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
    property = feature.replace(" ", "_")  
    print(property)

    if(property == "effective_temperature"):
        verb = "his_star_has_temp"
        myQuery = "prop(" + planet + ", " + verb + ", X)"
        
    elif(property == "metallicity"):
        verb = "his_star_has_met"
        myQuery = "prop(" + planet + ", " + verb + ", X)"
   
    elif(property == "spectral_classification"):
        verb = "his_star_is_class"
        myQuery = "prop(" + planet + ", " + verb + ", X)"
        
    elif(property == "planets_in_system"):
        verb = "planets_in_sys"       
        myQuery = "prop(" + planet + ", " + verb + ", X)."

    resultQuery = list(prolog.query(myQuery))
    for elem in resultQuery:
        result = elem["X"]   

    print(property + " for the chosen star is: " + str(result))  
        
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
    "has_eccentricity", "has_orbit_period", "distance_from_star", "planets_in_sys", "his_star_has_met", "his_star_has_temp",
    "was_discovered_in", "is_hab_class"]  

    return features


def classifyValues(featureDict):

    massRadius = getMassRadiusClass(featureDict["mass"], featureDict["radius"])
    densityClass = getDensityClass(featureDict["density"])
    gravityClass = getGravityClass(featureDict["gravity"])
    eqTempClass = getEqTempClass(featureDict["eqTemp"])
    eccentricityClass = getEccClass(featureDict["eccentricity"])
    oPeriodClass = getOPeriodClass(featureDict["oPeriod"])
    hzdClass = getHZDClass(featureDict["hzd"])
    metClass = getMetallicityClass(featureDict["met"])
    sTempClass = getStarTempClass(featureDict["starTemp"])
    
    return massRadius, densityClass, gravityClass, eqTempClass, eccentricityClass, oPeriodClass, hzdClass, metClass, sTempClass


def classifyExample(example):   

    resultClass = classify(example)
    print("\nThe exoplanet entered belongs to the class: " + resultClass)

    return resultClass 


#funzione che prende tutti i valori di tutti i pianeti per ogni feature
def listProp(planetList):

    features = getFeatures()

    # non creo manualmente lista dei pianeti perch?? lista non statica, se ne possono aggiungere altri 
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
        featureDict = createDict(values)                      
        transform(featureDict) 
    

#creo dizionario per accedere pi?? semplicemente ai dati e rendere pi?? leggibile il programma
def createDict(values):    
   
    featureDict = {"star": values[0],"radius": values[1], "mass": values[2], "density": values[3], "gravity": values[4], "eqTemp": values[5],
                    "composition": values[6], "atmosphere": values[7], "eccentricity": values[8], "oPeriod": values[9], "hzd": values[10],
                    "numPlanets": values[11], "met": values[12], "starTemp": values[13], "year": values[14], "hab": values[15]}

    return featureDict      

        
#funzione che trasforma in notazione "esempio(C,O)" tutti i fatti presenti
def transform(featureDict):

    massRadius, densityClass, gravityClass, eqTempClass, eccentricityClass, oPeriodClass, hzdClass, metClass, sTempClass = classifyValues(featureDict)  
              
    exampleFact = "esempio("+featureDict["hab"]+", [massRadius_class = "+ massRadius +", density = "+ densityClass +", gravity = "+gravityClass+",  eq_temp = "+eqTempClass+", composition = "+featureDict["composition"]+", atmosphere = "+featureDict["atmosphere"]+", eccentricity = "+eccentricityClass+", orbit_period_days = "+oPeriodClass+", zone_class = "+hzdClass+", num_planets = "+featureDict["numPlanets"]+", metallicity = "+metClass+", star_temp_class = "+sTempClass+"])"
    prolog.assertz(exampleFact)
        