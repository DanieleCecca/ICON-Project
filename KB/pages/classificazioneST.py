import streamlit as st

st.markdown("# Confronto tra diversi *modelli di apprendimento supervisionato* per la classificazione di esopianeti scoperti durante le diverse missioni spaziali.")
# 
st.markdown("# L'obbiettivo è sicuramente quello di trovare il migliore modello di classificazione in grado di deteminare la classe si abitibilità dell'esopianeta sottoposto al modello, sebbene i dati a nostra disposizione non sono sicuramente dei migliori.")
# 
st.markdown("# Questo sistema inoltre si pone come modulo complementare del sistema più ampio progettato per l'esame di ingeneria della conoscenza, il quale permetterà di agire un sistema esperto.")
# 
st.markdown('''# I modelli valutati in questo modulo sono i seguenti:
# - **Decision**
# - **Naive Bayes**
# - **Random Forest**
# - **Gradiend Boost**
# - **Support vector machine**'''

st.markdown("## Analisi Esplorativa & Preparazione dei Dati.")

st.caption("Importo i moduli e le librerie di interesse, utili per la realizzazione del sistema.")
code = '''import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.impute import SimpleImputer

from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import OneHotEncoder

from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay 
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.svm import SVC

from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.preprocessing import MinMaxScaler

from imblearn.over_sampling import SMOTE, ADASYN
from imblearn.pipeline import Pipeline as imbpipeline

from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import matthews_corrcoef
from imblearn.metrics import geometric_mean_score'''

st.code(code)

st.caption("Carichiamo il dataset in locale.")


code = '''planets = pd.read_csv("../PHL-EC.csv")
planets.head()'''

st.code(code)

st.markdown("### Pulizia dei dati")

st.caption("Verichiamo quanti esempi sono presenti per ogni classe di abitibilità.") 

st.caption("Quali siano le tipologie di pianeti con meno esempi?")

code = '''target_count = planets['P. Habitable Class'].value_counts()
target_count'''
st.code(code)

st.write("Eliminiamo le tipologie di pianeti per i quali abbiamo pochi esempi.")

st.write("elimino effettivamente i pianeti appartenenyi alla classe dei 'thermoplanet' e 'hypopsychroplanet' per i quali abbiamo solamente 3 esempi ciscuno.")

code = '''indexNames = planets[planets['P. Habitable Class'] == 'thermoplanet'].index
planets.drop(indexNames, inplace= True)

indexNames = planets[planets['P. Habitable Class'] == 'hypopsychroplanet'].index
planets.drop(indexNames, inplace= True)'''

st.code(code)

st.markdown('''Dopo l'eliminazione delle classi con pochi esempi avrà la seguente situazione; le classi di abitabilità non saranno più 5 ma saranno ridotte a 3 classi di abitabilita:
# + **non-habitable**
# + **mesoplanet**
# + **psychroplanet**''')

# %%
# ora la situazione sarà la seguente

target_count = planets['P. Habitable Class'].value_counts()
target_count

# %% [markdown]
# Avendo eliminato degli esempi, ossia delle righe dal nostro dataframe devo resettare di conseguenza l'index.

# %%
# resetto l'index del nostro database che è cambiato avendo tolto alcuni esempi

planets.reset_index(inplace = True, drop= True)

# %% [markdown]
# Continuamo rimuovendo ulteriori features in input, in modo tale da ridurre la dimensionalità del feautures space e in modo tale da rimuovere quelle features per le quali si hanno pochi dati.

# %%
# funzione che permette di rimuovere le feutures la cui densità è sotto un certo treshold
# count = valori nulli in una colonna specifica(in una feature)
# lenplanet(planet) = numero di righe totali(tot pianeti)
# count/len(planet) = ci dice in percentuale quanti valori ci saranno in quella colonna

def remove_missing(feauture):
    count = len(planets[planets[feauture].isnull()])
    if count/len(planets) > 0.2:
        return 1
    else:
        return 0
    
missing_values = [x for x in planets.columns if remove_missing(x)]
planets = planets.drop(missing_values, axis=1)

# %% [markdown]
# Rimuoviamo anche le seguenti features che non hanno alcuna valenza per il nostro obbiettivo, rappresentando alcune di esse l'incertezza di alcune features, e altre non hanno valenza da un punto di vista fisico.

# %%
# rimuovo altre features che rappresentano l'incertezza di alcune feautures e
# altre feautures che non interessano direttamente la classificazione

cols_to_drop = ['P. Name','S. Constellation', 'S. Type', 'P. Int ESI', 
                'P. Surf ESI', 'P. Disc. Method', 'P. Disc. Year','P. Hab Moon', 'P. SFlux Min (EU)', 'P. SFlux Max (EU)',
                'P. Teq Min (K)','P. Teq Max (K)','P. SFlux Mean (EU)','S. Name', 'S. Hab Zone Min (AU)', 'S. Hab Zone Max (AU)']

# TODO decidere se eliminare altre features tipo HZC ecc

planets = planets.drop(cols_to_drop, axis=1)

# %% [markdown]
# Le features rimaste per il momento saranno pertanto le seguenti.

# %%
pd.options.display.max_columns = None
pd.options.display.max_rows = None

print(planets.columns.tolist())

# %% [markdown]
# Per decidere se eliminare altre features osserviamo la correlazione tra le feutures creando una visualizzazione che traccia la misura di correlazione per ogni feature nel set di dati.

# %% [markdown]
# Prima di poter fare questo però devo :
# 1. *riempire il dataset con dati mancanti*
# 2. *trasformare le feauture categoriche in feauturs numeriche*
# 

# %% [markdown]
# Prima di tutto determiniamoo quali siano le features categoriche

# %%
pd.options.display.max_columns = None
pd.options.display.max_rows = None
print(planets.dtypes.tolist)

# %% [markdown]
# Si noti come le uniche features categoriche siano le prime 5:
# 
# 1. *P. Zone Class*
# 2. *P. Mass Class*
# 3. *P. Composition Class*
# 4. *P. Atmosphere Class*
# 5. *P. Habitable Class'*
# 

# %% [markdown]
# Verifichiamo quanti siano i dati mancanti in totale, considerando quindi sia le features categoriche che quelle numeriche.
# Sfruttiamo inoltre un heatmap per facilitare la lettura di tali valori.
# 

# %%
print(planets.isnull().sum())
sns.heatmap(planets.isnull())

# %% [markdown]
# ##### FASE 1 : riempire il dataset con dati mancanti

# %% [markdown]
# Per le features numeriche adottiamo il** simple Imputer di sklearn** che permette di riempire il valore mancante con il valore medio all'interno della colonna, specificando come strategia *mean*

# %%
# inserisco le features numeriche in una lista
numeric_features = list(planets[planets._get_numeric_data().columns])

simple_inputer = SimpleImputer(missing_values=np.nan, strategy='mean')
planets[numeric_features] = simple_inputer.fit_transform(planets[numeric_features])

planets[numeric_features].isnull().sum()

# %% [markdown]
# Per le features categoriche adottiamo il **simple Imputer di sklearn** che permette di riempire il valore mancante con quello più ricorrente all'interno della colonna, specificando come strategia *most frequent*

# %%
# inserisco le features categoriche in una lista
categorical_features = [col for col in planets.columns if planets[col].dtype=="O"]

simple_inputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
planets[categorical_features] = simple_inputer.fit_transform(planets[categorical_features])

planets[categorical_features].isnull().sum()


# %% [markdown]
# Il risultato finale sarà il seguente.
# 

# %%
sns.heatmap(planets.isnull())

# %% [markdown]
# ##### FASE 2 : trasformare le feauture categoriche in feauturs numeriche

# %% [markdown]
# Le prime 3 features (*P. Zone Class, P. Mass Class, new P. Habitable Class*) verranno trasformate utilizzando il **label encoding**, essendoci effettivamente un ordine tra i values le features. 

# %%
ord_enc = OrdinalEncoder()
planets["new P. Zone Class_code"] = ord_enc.fit_transform(planets[["P. Zone Class"]])

planets["new P. Mass Class"] = ord_enc.fit_transform(planets[["P. Mass Class"]])

planets["new P. Habitable Class"] = ord_enc.fit_transform(planets[["P. Habitable Class"]])



# %% [markdown]
# N.B 
# Poichè si è scoperto che stratifiedKFold non funziona con le feututres target multilabel ossia con le variabili indicatrici
# si è deciso di optare per il label encoding sebbene questa non sia stata la prima scelta
# Errore uscito : 'Supported target types are: ('binary', 'multiclass'). Got 'multilabel-indicator' instead'
# Link stackOverflow : https://stackoverflow.com/questions/54890899/not-able-to-use-stratified-k-fold-on-multi-label-classifier.
# Scrivere la risposta del link nella doc.

# %% [markdown]
# Le altre tre features (*P. Composition Class, P. Atmosphere Class)* verranno traformate utilizzando **l'hot encoder** che crea nuove feutures booleane a partire dai values delle feautures, ossia crea le *variabili indicatrici*
# 

# %%
# Il punto chiave è che devi utilizzare toarray() per convertire i risultati in un 
# formato che può essere convertito in un DataFrame.

# traformazione feature P. Composition Class
oe_style = OneHotEncoder()
oe_results = oe_style.fit_transform(planets[["P. Composition Class"]])
pd.DataFrame(oe_results.toarray(), columns=oe_style.categories_)

# Il passaggio successivo è unire questi dati al dataframe originale.
planets = planets.join(pd.DataFrame(oe_results.toarray(), columns=oe_style.categories_))

# traformazione feature P. Atmosphere Class
oe_results = oe_style.fit_transform(planets[["P. Atmosphere Class"]])
pd.DataFrame(oe_results.toarray(), columns=oe_style.categories_)

planets = planets.join(pd.DataFrame(oe_results.toarray(), columns=oe_style.categories_))


# NON FUNZIONA LEGGERE SOPRA(blocco markdown sotto il blocco 67)
#  traformazione feature P. Habitable Class
#oe_results = oe_style.fit_transform(planets[["P. Habitable Class"]])
#pd.DataFrame(oe_results.toarray(), columns=oe_style.categories_)

#planets = planets.join(pd.DataFrame(oe_results.toarray(), columns=oe_style.categories_))

# %% [markdown]
# Il dataframe con le nuove features sarà il seguente

# %%
planets.head()

# %% [markdown]
# Rinomiano il label delle nuove features create.
# 

# %%
planets.rename({('gas',): 'Composition gas', 
                ('iron',): 'Composition iron',
                ('rocky-iron',): 'Composition rocky-iron', 
                ('rocky-water',): 'Composition rocky-water',
                ('water-gas',): 'Composition water-gas'}, axis=1, inplace= True) 

planets.rename({('hydrogen-rich',): 'Atmosphere hydrogen-rich', 
                ('metals-rich',): 'Atmosphere metals-rich',
                ('no-atmosphere',): 'Atmosphere no-atmosphere'}, axis=1, inplace= True) 

# NON FUNZIONA LEGGERE SOPRA(blocco markdown sotto il blocco 67)
#planets.rename({('mesoplanet',): 'Habitable mesoplanet', 
                # ('non-habitable',): 'Habitable non-habitable',
                # ('psychroplanet',): 'Habitable psychroplanet'}, axis=1, inplace= True) 


# %% [markdown]
# Osserviamo la correlazione

# %%
# pands .corr() per calcolare la correlazione a coppie tra le features del dataframes
corr = planets.corr()

# visualizzo i dati con seaborn
mask = np.triu(np.ones_like(corr, dtype=bool))
sns.set_style(style = 'white')
f, ax = plt.subplots(figsize=(11, 9))
cmap = sns.diverging_palette(10, 250, as_cmap=True)
sns.heatmap(corr, mask=mask, cmap=cmap, 
        square=True,
        linewidths=.5, cbar_kws={"shrink": .5}, ax=ax)

# %% [markdown]
# Si noti come tra le features rimaste ci siano delle feautures altamente correlate tra di loro, che restituiscono sostanzialmente le stesse informazioni, pertanto le rimuoviamo:
# 
# - **P. Mass Class ---> P. Radius (EU) and P. Mass (EU)**
# - **P. Zone Class ---> HZD**
# 

# %%
cols_to_drop = ["P. Mass Class", "P. Zone Class"]

planets = planets.drop(cols_to_drop, axis=1)

# %% [markdown]
# Possiamo ora notare comee il nostro dataset sia molto sbilanciato

# %%
target_count = planets['P. Habitable Class'].value_counts()
print(f'non-habitable: {target_count[0]}')
print(f'mesoplanet: {target_count[1]}')
print(f'psychroplanet : {target_count[2]}')
print(f'Percentage of Majority Class: {round(target_count[0] / sum(target_count), 4)*100}')
print(f'Percentage of Minority Class: {round(target_count[1] / sum(target_count), 4)*100}')
print(f'Percentage of Minority Class: {round(target_count[2] / sum(target_count), 4)*100}')

target_count.plot(kind='bar', title='Count (target)')

# %%
planets.head()

# %% [markdown]
# N.B 
# Poichè si è scoperto che stratifiedKFold non funziona con le feututres target multilabel ossia con le variabili indicatrici
# si è deciso di optare per il label encoding sebbene questa non sia stata la prima scelta
# Errore uscito : 'Supported target types are: ('binary', 'multiclass'). Got 'multilabel-indicator' instead'
# Link stackOverflow : https://stackoverflow.com/questions/54890899/not-able-to-use-stratified-k-fold-on-multi-label-classifier
# 
# 

# %% [markdown]
# Divido il dataset

# %%
# TODO fare una copia forse
cols_to_drop = ["P. Composition Class", "P. Atmosphere Class","P. Habitable Class"]

planets = planets.drop(cols_to_drop, axis=1)

# %%
target_features = ['new P. Habitable Class']

# X: set di samples con le input features
# y: set di samples con la target feature

X = planets.drop(target_features, axis=1)
y = planets[target_features]



# %%
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, stratify=y, random_state=11)


# %% [markdown]
# ## Costruzione dei modelli & Addestramento

# %% [markdown]
# ### Classificazione con  DecisionTreeClassifier

# %%
pipeline = imbpipeline(steps = [['smote', SMOTE(random_state=11)],
                                ['scaler', MinMaxScaler()],
                                ['classifier', DecisionTreeClassifier(random_state=11)]])

# %% [markdown]
# si è deciso di usare lo StratifiedKFold in modo tale da mantenere le proporzioni avendo un dataset molto sbilanciato

# %%
stratified_kfold = StratifiedKFold(n_splits=3,
                                       shuffle=True,
                                       random_state=11)

# %%

# in param_grid sono definiti gli iperparametri
# TODO definire iper parametri per ogni metodo di classificazione
param_grid = {
    'criterion':['gini', 'entropy'],
    'max_depth':range(1,10),
    'min_samples_split':range(2,10),
    'min_samples_leaf':range(1,5)    
}
new_params = {'classifier__' + key: param_grid[key] for key in param_grid}


# permette di provare tutte le combinazioni degli iper parametri in modo tale da ottenre 
# i valori ottimali per il modello
# quindi itera per ogni fold creata sugli iperparametri 
# Niper = numero iper paratri                   
# Nfold = numero fold
# Viper = values per ogni per parametro
# complessita credo = ((Nfold)^Viper)^Niper

# TODO verificare per quale motivo non funzionano le altre metriche
grid_search = GridSearchCV(estimator=pipeline,
                           param_grid=new_params,
                           scoring='accuracy',
                           cv=stratified_kfold,
                           verbose = 5,
                           n_jobs=-1) # utilizzerà tutti i processori disponibili

# %%
# troviamo il modello migliore
grid_search.fit(X_train, y_train)
cv_score = grid_search.best_score_
best_params = grid_search.best_params_

print(f'Best parameters: {best_params}')
print(f'Cross-validation score: {cv_score}')
# effetuamo la predizione sul set di test
y_test_predict = grid_search.predict(X_test)


# %%
# calcoliamo le metriche di valutazione
accuracy = accuracy_score(y_test, y_test_predict)
precision = precision_score(y_test, y_test_predict, average='macro')
recall = recall_score(y_test, y_test_predict, average='macro')
f1 = f1_score(y_test, y_test_predict, average='macro')
mcc = matthews_corrcoef(y_test, y_test_predict)
# auc = roc_auc_score(y_test, y_test_predict, multi_class = 'ovr',average='macro')
gm = geometric_mean_score(y_test, y_test_predict, average='macro')
ConfusionMatrixDisplay.from_predictions(y_test, 
                                        y_test_predict, 
                                        cmap=plt.cm.inferno)

print(f'accuracy: {accuracy}')
print(f'precision: {precision}')
print(f'recall: {recall}')
print(f'f1: {f1}')
#print(f'f1: {auc}')
print(f'matthews_corrcoef: {mcc}')
print(f'geometric_mean_score: {gm}')

plt.plot()



# %%
scoring_list = []
scoring_list.append(dict([
    ('Model', 'DecisionTreeClassifier'),
    ('Train Accuracy', round(cv_score, 3)),
    ('Test Accuracy', round(accuracy, 3)),
    ('Precision', round(precision, 3)),
    ('Recall', round(recall, 3)),
    ('F1', round(f1, 3)),
    ('Matthews Corrcoef', round(mcc)),
    ('Geometric Mean Score', round(gm, 3))
     ]))

# %% [markdown]
# ### Classificazione con  Naive Bayes

# %% [markdown]
# non ci sono iperparametri quindi è inutile fare grid search
# capire quindi se ha senso fare anche la cross validation

# %%
pipeline = imbpipeline(steps = [['smote', SMOTE(random_state=11)],
                                ['scaler', MinMaxScaler()],
                                ['classifier', GaussianNB()]]) 

# %%
stratified_kfold = StratifiedKFold(n_splits=3,
                                       shuffle=True,
                                       random_state=11)

# %%
# in param_grid sono definiti gli iperparametri
# TODO definire iper parametri per ogni metodo di classificazione
param_grid = {}

# TODO verificare per quale motivo non funzionano le altre metriche
grid_search = GridSearchCV(estimator=pipeline,
                           param_grid=param_grid,
                           scoring='accuracy',
                           cv=stratified_kfold,
                           verbose = 5,
                           n_jobs=-1) # utilizzerà tutti i processori disponibili

# %%
# troviamo il modello migliore
grid_search.fit(X_train, y_train)

cv_score = grid_search.best_score_

# effetuamo la predizione sul set di test
y_test_predict = grid_search.predict(X_test)


# %%
# calcoliamo le metriche di valutazione
accuracy = accuracy_score(y_test, y_test_predict)
precision = precision_score(y_test, y_test_predict, average='macro')
recall = recall_score(y_test, y_test_predict, average='macro')
f1 = f1_score(y_test, y_test_predict, average='macro')
mcc = matthews_corrcoef(y_test, y_test_predict)
# auc = roc_auc_score(y_test, y_test_predict, multi_class = 'ovr',average='macro')
gm = geometric_mean_score(y_test, y_test_predict, average='macro')
ConfusionMatrixDisplay.from_predictions(y_test, 
                                        y_test_predict, 
                                        cmap=plt.cm.inferno)

print(f'accuracy: {accuracy}')
print(f'precision: {precision}')
print(f'recall: {recall}')
print(f'f1: {f1}')
#print(f'f1: {auc}')
print(f'matthews_corrcoef: {mcc}')
print(f'geometric_mean_score: {gm}')

plt.plot()

# %%
scoring_list.append(dict([
    ('Model', 'Naive Bayes'),
    ('Train Accuracy', round(cv_score, 3)),
    ('Test Accuracy', round(accuracy, 3)),
    ('Precision', round(precision, 3)),
    ('Recall', round(recall, 3)),
    ('F1', round(f1, 3)),
    ('Matthews Corrcoef', round(mcc)),
    ('Geometric Mean Score', round(gm, 3))
     ]))

# %% [markdown]
# ### Classificazione con  RandomForest

# %%
pipeline = imbpipeline(steps = [['smote', SMOTE(random_state=11)],
                                ['scaler', MinMaxScaler()],
                                ['classifier', RandomForestClassifier(max_depth=None, random_state=None)]]) #decidete se mettere qualche parametro

# %%
stratified_kfold = StratifiedKFold(n_splits=3,
                                       shuffle=True,
                                       random_state=11)

# %%
# in param_grid sono definiti gli iperparametri
# TODO definire iper parametri per ogni metodo di classificazione
param_grid = {
                'n_estimators': [50, 100, 200],
                'max_depth': [4, 6, 10, 12],
                'random_state': [13]
                }

new_params = {'classifier__' + key: param_grid[key] for key in param_grid}

# TODO verificare per quale motivo non funzionano le altre metriche
grid_search = GridSearchCV(estimator=pipeline,
                           param_grid=new_params,
                           scoring='accuracy',
                           cv=stratified_kfold,
                           verbose = 5,
                           n_jobs=-1) # utilizzerà tutti i processori disponibili

# %%
# troviamo il modello migliore
grid_search.fit(X_train, y_train)

cv_score = grid_search.best_score_
best_params = grid_search.best_params_

print(f'Best parameters: {best_params}')
print(f'Cross-validation score: {cv_score}')

# effetuamo la predizione sul set di test
y_test_predict = grid_search.predict(X_test)

# %%
# calcoliamo le metriche di valutazione
accuracy = accuracy_score(y_test, y_test_predict)
precision = precision_score(y_test, y_test_predict, average='macro')
recall = recall_score(y_test, y_test_predict, average='macro')
f1 = f1_score(y_test, y_test_predict, average='macro')
mcc = matthews_corrcoef(y_test, y_test_predict)
# auc = roc_auc_score(y_test, y_test_predict, multi_class = 'ovr',average='macro')
gm = geometric_mean_score(y_test, y_test_predict, average='macro')
ConfusionMatrixDisplay.from_predictions(y_test, 
                                        y_test_predict, 
                                        cmap=plt.cm.inferno)

print(f'accuracy: {accuracy}')
print(f'precision: {precision}')
print(f'recall: {recall}')
print(f'f1: {f1}')
#print(f'f1: {auc}')
print(f'matthews_corrcoef: {mcc}')
print(f'geometric_mean_score: {gm}')

plt.plot()

# %%
scoring_list.append(dict([
    ('Model', 'RandomForest'),
    ('Train Accuracy', round(cv_score, 3)),
    ('Test Accuracy', round(accuracy, 3)),
    ('Precision', round(precision, 3)),
    ('Recall', round(recall, 3)),
    ('F1', round(f1, 3)),
    ('Matthews Corrcoef', round(mcc)),
    ('Geometric Mean Score', round(gm, 3))
     ]))

# %% [markdown]
# ### Classificazione con Gradient Boosting

# %%
pipeline = imbpipeline(steps = [['smote', SMOTE(random_state=11)],
                                ['scaler', MinMaxScaler()],
                                ['classifier',GradientBoostingClassifier(n_estimators=100,
                                                                         learning_rate=1.0,
                                                                         max_depth=1, 
                                                                         random_state=11)]]) #decidete se mettere qualche parametro

# %%
stratified_kfold = StratifiedKFold(n_splits=3,
                                       shuffle=True,
                                       random_state=11)

# %%
# in param_grid sono definiti gli iperparametri
# TODO definire iper parametri per ogni metodo di classificazione
param_grid = {   
              'max_depth': range (2, 10, 1),
              'n_estimators': range(60, 220, 40),
              'learning_rate': [0.1, 0.01, 0.05]
              }

new_params = {'classifier__' + key: param_grid[key] for key in param_grid}

# TODO verificare per quale motivo non funzionano le altre metriche
grid_search = GridSearchCV(estimator=pipeline,
                           param_grid=new_params,
                           scoring='accuracy',
                           cv=stratified_kfold,
                           verbose = 5,
                           n_jobs=-1) # utilizzerà tutti i processori disponibili

# %%
# troviamo il modello migliore
grid_search.fit(X_train, y_train)

cv_score = grid_search.best_score_
best_params = grid_search.best_params_

print(f'Best parameters: {best_params}')
print(f'Cross-validation score: {cv_score}')

# effetuamo la predizione sul set di test
y_test_predict = grid_search.predict(X_test)

# %%
# calcoliamo le metriche di valutazione
accuracy = accuracy_score(y_test, y_test_predict)
precision = precision_score(y_test, y_test_predict, average='macro')
recall = recall_score(y_test, y_test_predict, average='macro')
f1 = f1_score(y_test, y_test_predict, average='macro')
mcc = matthews_corrcoef(y_test, y_test_predict)
# auc = roc_auc_score(y_test, y_test_predict, multi_class = 'ovr',average='macro')
gm = geometric_mean_score(y_test, y_test_predict, average='macro')
ConfusionMatrixDisplay.from_predictions(y_test, 
                                        y_test_predict, 
                                        cmap=plt.cm.inferno)

print(f'accuracy: {accuracy}')
print(f'precision: {precision}')
print(f'recall: {recall}')
print(f'f1: {f1}')
#print(f'f1: {auc}')
print(f'matthews_corrcoef: {mcc}')
print(f'geometric_mean_score: {gm}')

plt.plot()

# %%
scoring_list.append(dict([
    ('Model', 'Gradient Boosting'),
    ('Train Accuracy', round(cv_score, 3)),
    ('Test Accuracy', round(accuracy, 3)),
    ('Precision', round(precision, 3)),
    ('Recall', round(recall, 3)),
    ('F1', round(f1, 3)),
    ('Matthews Corrcoef', round(mcc)),
    ('Geometric Mean Score', round(gm, 3))
     ]))

# %% [markdown]
# ### Classificazione con SVM

# %%
pipeline = imbpipeline(steps = [['smote', SMOTE(random_state=11)],
                                ['scaler', MinMaxScaler()],
                                ['classifier',SVC(kernel=None,
                                                  gamma=None, 
                                                  C=None)]]) #decidete se mettere qualche parametro cambiare parametri con iper parametri

# %%
stratified_kfold = StratifiedKFold(n_splits=3,
                                       shuffle=True,
                                       random_state=11)

# %%
# in param_grid sono definiti gli iperparametri
# TODO definire iper parametri per ogni metodo di classificazione
param_grid = {'C': [0.1, 1, 10, 100, 1000], 
              'gamma': [1, 0.1, 0.01, 0.001, 0.0001],
              'kernel': ['rbf']
              }

new_params = {'classifier__' + key: param_grid[key] for key in param_grid}

# TODO verificare per quale motivo non funzionano le altre metriche
grid_search = GridSearchCV(estimator=pipeline,
                           param_grid=new_params,
                           scoring='accuracy',
                           cv=stratified_kfold,
                           verbose = 5,
                           n_jobs=-1) # utilizzerà tutti i processori disponibili

# %%
# troviamo il modello migliore
grid_search.fit(X_train, y_train)

cv_score = grid_search.best_score_
best_params = grid_search.best_params_

print(f'Best parameters: {best_params}')
print(f'Cross-validation score: {cv_score}')

# effetuamo la predizione sul set di test
y_test_predict = grid_search.predict(X_test)

# %%
# calcoliamo le metriche di valutazione
accuracy = accuracy_score(y_test, y_test_predict)
precision = precision_score(y_test, y_test_predict, average='macro')
recall = recall_score(y_test, y_test_predict, average='macro')
f1 = f1_score(y_test, y_test_predict, average='macro')
mcc = matthews_corrcoef(y_test, y_test_predict)
# auc = roc_auc_score(y_test, y_test_predict, multi_class = 'ovr',average='macro')
gm = geometric_mean_score(y_test, y_test_predict, average='macro')
ConfusionMatrixDisplay.from_predictions(y_test, 
                                        y_test_predict, 
                                        cmap=plt.cm.inferno)

print(f'accuracy: {accuracy}')
print(f'precision: {precision}')
print(f'recall: {recall}')
print(f'f1: {f1}')
#print(f'f1: {auc}')
print(f'matthews_corrcoef: {mcc}')
print(f'geometric_mean_score: {gm}')

plt.plot()

# %%
scoring_list.append(dict([
    ('Model', 'SVM'),
    ('Train Accuracy', round(cv_score, 3)),
    ('Test Accuracy', round(accuracy, 3)),
    ('Precision', round(precision, 3)),
    ('Recall', round(recall, 3)),
    ('F1', round(f1, 3)),
    ('Matthews Corrcoef', round(mcc)),
    ('Geometric Mean Score', round(gm, 3))
     ]))

# %% [markdown]
# Ora confrontiamo i vari modelli secondo le metriche usate
# 

# %%
results = pd.DataFrame(data=scoring_list)
results = results[['Model',
                   'Train Accuracy',
                   'Test Accuracy',
                   'Precision',
                   'Recall',
                   'F1',
                   'Matthews Corrcoef',
                   'Geometric Mean Score']]

results = results.sort_values(by='Recall', ascending=False)
results = results.set_index('Model')
results



