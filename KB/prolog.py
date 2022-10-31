from pyswip import Prolog

prolog = Prolog()
prolog.consult("C:/Users/follo/OneDrive/Documenti/GitHub/ICON-Project/KB/exo2.pl")

# funzione per richiamare la query prolog che restituisce tutti gli esopianeti
def getExoplanets():    
    myQuery = "prop(P, hostname, _)."
    planets = list(prolog.query(myQuery))          
    return planets

def printExoplanets(planets):
    print("\nList of all the exoplanets:")
    for elem in planets:
        queryPlanets = "> "+ elem["P"] + ""  
        print(queryPlanets)

        
# funzione per richiamare la query prolog che restituisce tutti gli esopianeti abitabili
def getExoplanetsHabitable():

    print("\nList of all the habitable exoplanets:")
    myQuery = "prop(P ,is_habitable)."
    planets = list(prolog.query(myQuery))
    for elem in planets:
        queryPlanets = "> "+ elem["P"] +""
        print(queryPlanets)


# funzione per richiamare la query prolog che restituisce una descrizione del pianeta
def getInfo(planet):  

    myQuery = "get_info_about("+ planet + ")"
    info = list(prolog.query(myQuery))
    
    
#TO DO gestire gli errori
# funzione per richiamare la query prolog che restituisce il valore della feuture indicata del pianeta dato
def getFeatures(planet, feature):
    
    verb = ""    
    property = feature.replace(" ", "_")
    print(property)

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
        print("The chosen exoplanet for the feature '" + feature + "' has value: ")
        print(result)

    
#funzione che permette di aggiungere un pianeta
def addPlanet(planet,feature,value):
    
    verb = ""
    property = feature.replace(" ", "_")
    print(property)

    if(feature == "equilibrium_temperature"):
        verb = "has_temp"
        myQuery = "prop(" + planet + ", " + verb + ", " + value + " )"

    elif(property == "atmosphere_type"):
        verb = "has_atmosphere"
        myQuery = "prop(" + planet + ", " + verb + ", " + value + " )"
        
    elif(feature == "discovery_year"):
        verb = "was_discovered"
        myQuery = "prop(" + planet + ", " + verb + ", " + value + ")"

    elif(feature == "hostname"):
        verb = feature
        myQuery = "prop(" + planet + ", " + verb + ", " + value + ")"
    
    else:
        verb = "has_" + feature
        myQuery = "prop(" + planet + ", " + verb + ", "+value+")"
        
    prolog.assertz(myQuery)
    
#da disabilitare (?)    
#funzione che permette di determinare se un pianeta è abitabile e la classe di appartenenza
def isHabitable(planet): 
    myQuery = "prop("+planet+", is_habitable, X)"    
    resultQuery = list(prolog.query(myQuery))        
    for elem in resultQuery:
        result = elem["X"]
        print("The answer is " + result)        
        if(result == "true"):
            classQuery = "prop("+planet+", is_in_habitable_class, C)"
            resultQuery = list(prolog.query(classQuery))                 
            for elem in resultQuery:
                result = elem["C"]            
                print("The chosen exoplanet is habitable and belongs to the class: " + result)            


#funzione che richiama query prolog delel classificazione della massa
def getMassClass(planet):
    myQuery = "prop("+planet+", is_mass_class, T)"
    resultQuery = list(prolog.query(myQuery))
    for elem in resultQuery:
        result = elem["C"]            
        print("The chosen exoplanet is classified by mass as a: " + result)    


# funzione per richiamare la query prolog che restituisce il valore della feuture indicata della stella data
def getStarFeatures(planet, feature):
    flag = False
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

# funzione per richiamare la funzione learning tramite algoritmo ILP(inductive logic programming)
def learnNonHab():
    myQuery = "apprendi(non_habitable)"    
    prolog.query(myQuery)
    rule1 = list(prolog.query(myQuery))

def learnHab():    
    myQuery = "apprendi(habitable)"    
    prolog.query(myQuery)    
    rule2 = list(prolog.query(myQuery))      

# funzione per richiamare la funzione classify tramite algoritmo ILP (inductive logic programming) 
def classify(example):
    myQuery = "classifica(" + example +", Classe)"
    print(myQuery)
    prolog.query(myQuery)
    resultQuery = list(prolog.query(myQuery))
    for elem in resultQuery:
       result = elem["Classe"]            
    return result
    
# funzione per richiamare una classe
def getDensityClass(density):
    myQuery = "prop("+density+", density_is_class, C)"
    resultQuery = list(prolog.query(myQuery))
    for elem in resultQuery:
        result = elem["C"]                 
        print(result)
        return result

# funzione per richiamare una classe
def getGravityClass(gravity):
    myQuery = "prop("+gravity+", gravity_is_class, C)"
    resultQuery = list(prolog.query(myQuery))
    for elem in resultQuery:
        result = elem["C"]                 
        print(result)
        return result

# funzione per richiamare una classe
def getETempClass(eqTemp):
    myQuery = "prop("+eqTemp+", temp_is_class, C)"
    resultQuery = list(prolog.query(myQuery))
    for elem in resultQuery:
        result = elem["C"]                 
        print(result)
        return result
        
# funzione per richiamare una classe
def getEccClass(eccentricity):
    myQuery = "prop("+eccentricity+", eccentricity_is_class, C)"
    resultQuery = list(prolog.query(myQuery))
    for elem in resultQuery:
        result = elem["C"]                 
        print(result)
        return result


# funzione per richiamare una classe
def getOPeriodClass(operiod):
    myQuery = "prop("+operiod+", operiod__is_class, C)"
    resultQuery = list(prolog.query(myQuery))
    for elem in resultQuery:
        result = elem["C"]                 
        print(result)
        return result   

# funzione per richiamare una classe
def getMetallicityClass(metallicity):
    myQuery = "prop("+metallicity+", metallicity_is_class, C)"
    resultQuery = list(prolog.query(myQuery))
    for elem in resultQuery:
        result = elem["C"]                 
        print(result)
        return result
        
# funzione per richiamare una classe
def getMassRadiusClass(mass, radius): #TODO crash se inseriti intervalli non consentiti (RISOLTO mettendo OR)
    myQuery = "prop("+"["+mass+"|"+radius+"]"+", massRadius_is_class, C)"
    resultQuery = list(prolog.query(myQuery))
    for elem in resultQuery:
        result = elem["C"]                 
        print(result)
        return result

# funzione per richiamare una classe
def getHZDClass(operiod):
    myQuery = "prop("+operiod+", habitability_is_class, C)"
    resultQuery = list(prolog.query(myQuery))
    for elem in resultQuery:
        result = elem["C"]                 
        print(result)
        return result

# funzione per richiamare una classe
def getStarTempClass(starTemp):
    myQuery = "prop("+starTemp+", starTemp_is_class, C)"
    resultQuery = list(prolog.query(myQuery)) #prologilp
    for elem in resultQuery:
        result = elem["C"]                 
        print(result)
        return result
        
        
def listProp(planetList):

    features = ["hostname", "has_radius", "has_mass", "has_density", "has_gravity", "has_temp", "has_composition", "has_atmosphere",
    "has_eccentricity", "has_orbit_period", "distance_from_star", "has_stars_in_sys", "his_star_has_met", "his_star_has_temp"]  

    # non creo manualmente lista dei pianeti perchè lista non statica, se ne possono aggiungere altri 
    planets = [] # lista dei pianeti creata a partire dal risultato (planetList) di una query precedente
    for elem in planetList:
        planets.append(elem["P"])    
 
    for p in planets: 
        values = []      
        for f in features:             
            #myQuery = "findall(prop("+p+","+f+",V), prop("+p+","+f+", V), Esempi)."
            myQuery = "prop("+ p +","+ f +", V)."
            resultQuery = prolog.query(myQuery)    
            for elem in resultQuery:
                values.append(str(elem["V"]))     
        #print("\nvalues for: ", p, "= ", values)                      
        transform(p, f, values)        

        
#TODO IMPLEMENTAZIONE FUTURA: cambiare struttura dati, magari HashMap {feature: value}
def transform(planets, features, values):      

    massRadius = getMassRadiusClass(values[2], values[1]) #TODO AGgiustuarea
    density = getDensityClass(values[3])
    gravity = getGravityClass(values[4])
    eqTemp = getETempClass(values[5])
    eccentricity = getEccClass(values[8])
    oPeriod = getOPeriodClass(values[9])
    hzd = getHZDClass(values[10])
    met = getMetallicityClass(values[12])
    sTemp = getStarTempClass(values[13])
    
    example = "[massRadius_class = "+ massRadius +", density = "+ density +", gravity = "+gravity+",  eq_temp = "+eqTemp+", composition = "+values[6]+", atmosphere = "+values[7]+", eccentricity = "+eccentricity+", orbit_period_days = "+oPeriod+", zone_class = "+hzd+", num_stars = "+values[11]+" ,metallicity = "+met+" , star_temp_class = "+sTemp+"]"
    resultClass = classify(example)    

    exampleFact = "esempio("+resultClass+", [massRadius_class = "+ massRadius +", density = "+ density +", gravity = "+gravity+",  eq_temp = "+eqTemp+", composition = "+values[6]+", atmosphere = "+values[7]+", eccentricity = "+eccentricity+", orbit_period_days = "+oPeriod+", zone_class = "+hzd+", num_stars = "+values[11]+" ,metallicity = "+met+" , star_temp_class = "+sTemp+"]"
