from pyswip import Prolog

prolog = Prolog()
prolog.consult("exo.pl")

# funzione per richiamare la query prolog che restituisce tutti gli esopianeti
def getExoplanets():

    myQuery = "prop(P, hostname, _)."
    planets = list(prolog.query(myQuery))
    for elem in planets:
        queryPlanets = "- "+ elem["P"] +""
        print(queryPlanets)
        
# funzione per richiamare la query prolog che restituisce tutti gli esopianeti abitabili
def getExoplanetsHabitable():

    myQuery = "prop(P ,is_habitable, true)."
    planets = list(prolog.query(myQuery))
    for elem in planets:
        queryPlanets = "- "+ elem["P"] +""
        print(queryPlanets)

# funzione per richiamare la query prolog che restituisce una descrizione del pianeta
def getInfo(planet):
    myQuery = "get_info_about("+ planet+ ")"
    info = list(prolog.query(myQuery))
    
    
#TO DO gestire gli errori
# funzione per richiamare la query prolog che restituisce il valore della feuture indicata del pianeta dato
def getFeautures(planet, feauture):
    flag = False;
    verb =""
    feauture.strip()
    if(feauture == "equilibriumtemperature"):
        verb = "has_temp"
        myQuery = "prop(" + planet + ", " + verb + ", X)."
        
    elif(feauture == "discoveryyear"):
        verb = "was_discovered"
        myQuery = "prop(" + planet + ", " + verb + ", X)."
   
    elif(feauture == "p"):
        verb = "hostname"
        myQuery = "prop(" + planet + ", " + verb + ", X)."
        valueQuery = list(prolog.query(myQuery))

    else:
        verb = "has_" + feauture
        myQuery = "prop(" + planet + ", " + verb + ", X)."
 
    valueQuery = list(prolog.query(myQuery))    
    print(valueQuery)
    return
    
#funzione che permette di aggiungere un pianeta
def addPlanet(planet,feauture,value):
    
    verb =""
    feauture.strip()
    if(feauture == "equilibriumtemperature"):
        verb = "has_temp"
        myQuery = "prop(" + planet + ", " + verb + ", "+value+" )"
        
    elif(feauture == "discoveryyear"):
        verb = "was_discovered"
        myQuery = "prop(" + planet + ", " + verb + ", "+value+")"

    elif(feauture == "hostname"):
        verb = feauture
        myQuery = "prop(" + planet + ", " + verb + ", "+value+")"

    
    else:
        verb = "has_" + feauture
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
def getStarFeautures(planet, feauture):
    flag = False;
    verb =""
    feauture.strip()
    if(feauture == "effectivetemperature"):
        verb = "his_star_has_temp"
        myQuery = "prop(" + planet + ", " + verb + ", X)."
        
    elif(feauture == "metallicity"):
        verb = "his_star_has_met"
        myQuery = "prop(" + planet + ", " + verb + ", X)."
   
    elif(feauture == "spectralclassification"):
        verb = "his_star_is_class"
        myQuery = "prop(" + planet + ", " + verb + ", X)."

    valueQuery = list(prolog.query(myQuery))    
    print(valueQuery)
    



    
