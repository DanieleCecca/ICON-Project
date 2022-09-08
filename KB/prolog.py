from pyswip import Prolog

prolog = Prolog()
prolog.consult("C:/Users/follo/OneDrive/Documenti/GitHub/ICON-Project/KB/exo.pl")


# funzione per richiamare la query prolog che restituisce tutti gli esopianeti
def getExoplanets():

    print("\nList of all the exoplanets:")
    myQuery = "prop(P, hostname, _)."
    planets = list(prolog.query(myQuery))
    for elem in planets:
        queryPlanets = "> "+ elem["P"] +""
        print(queryPlanets)

        
# funzione per richiamare la query prolog che restituisce tutti gli esopianeti abitabili
def getExoplanetsHabitable():

    print("\nList of all the habitable exoplanets:")
    myQuery = "prop(P ,is_habitable, true)."
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
def getfeatures(planet, feature):
    
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
        valueQuery = list(prolog.query(myQuery))

    else:
        verb = "has_" + property
        myQuery = "prop(" + planet + ", " + verb + ", X)."
 
    valueQuery = list(prolog.query(myQuery))      
    print(valueQuery) 

    
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
    
    
#funzione che permette di determinare se un pianeta è abitabile e la classe di appartenenza
def isHabitable(planet):
    myQuery = "prop("+planet+", is_habitable, true)"    
    if(myQuery):
        classQuery = "prop("+planet+", is_in_habitable_class, C)"
        valueQuery = list(prolog.query(classQuery))    
        print(valueQuery)


#funzione che richiama query prolog delel classificazione della massa
def getMassClass(planet):
    myQuery = "prop("+planet+", is_mass_class, T)"
    valueQuery = list(prolog.query(myQuery))
    print(valueQuery)


# funzione per richiamare la query prolog che restituisce il valore della feuture indicata della stella data
def getStarfeatures(planet, feature):
    flag = False;
    verb =""
    feature.strip()

    if(feature == "effectivetemperature"):
        verb = "his_star_has_temp"
        myQuery = "prop(" + planet + ", " + verb + ", X)."
        
    elif(feature == "metallicity"):
        verb = "his_star_has_met"
        myQuery = "prop(" + planet + ", " + verb + ", X)."
   
    elif(feature == "spectralclassification"):
        verb = "his_star_is_class"
        myQuery = "prop(" + planet + ", " + verb + ", X)."

    valueQuery = list(prolog.query(myQuery))    
    print(valueQuery)    
