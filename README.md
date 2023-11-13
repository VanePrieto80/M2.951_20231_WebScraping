# **README - Web Scraping de SoundCloud**


# Albums top: Títol, Artista, Popularitat i més.


## Membres de l'Equip

- Vanesa Prieto (vprietop@uoc.edu)
- Sergi Benito (sbenitoiv@uoc.edu)


# Descripció del Projecte

Aquest projecte és una eina de web scraping dissenyada per recopilar dades de SoundCloud,
una plataforma de distribució de música en línia. Amb aquesta eina pots obtenir informació 
sobre cançons, àlbums i artistes disponibles a SoundCloud per fer-ne l'anàlisi.


## Funcions Destacades

Recopilar dades de les cançons més populars a SoundCloud.

Registrar la popularitat de cada cançó mitjançant indicadors com el nombre de reproduccions, "M'agrada" i "Repost."

Analitzar les tendències musicals dominants i els gèneres més representats a SoundCloud durant l'any 2023.

Identificar artistes emergents que han aconseguit notorietat a la plataforma SoundCloud.

Proporcionar una visió global i anual de les dades recopilades.


## Estructura del Repositori

El repositori està organitzat en les següents carpetes i arxius:

- `/dataset/`: Aquesta carpeta conté el conjunt de dades generat.

- `/dataset/examples/`: Aquesta carpeta conté exemples d'ús del codi.

- `/source/`: Aquesta carpeta conté els arxius de codi font.

- `/Requeriments.txt`: Aquest arxiu conté les biblioteques necessàries.
  
- `/README.md`: El present arxiu.



## Requisits i configuració

Instal·la les biblioteques necessàries mitjançant pip install -r requirements.txt.

L'script executa Chrome com a navegador.

L'IDE utilitzat és Spyder d'Anaconda.


## Ús del Codi Generat

Executa l'script SoundCloud.py per començar una recopilació de dades. 

Pots personalitzar els paràmetres de recerca mitjançant l'interfície de línia de comandes a cerca_SoundCloud.py.


## Exemples

Es presenten diferents exemples de com realitzar una nova recerca canviant els paràmetres que es troben a l'arxiu cerca_SoundCloud.py:

Exemple 1:

CERCA = "Alejandro Sanz" # Clave per a realitzar la bùsqueda a SoundCloud
N = 5 # Nombre de vegades que es realitzarà SCROLL per a descarregar les dades
NOM_ARXIU = "/AlejandroSanz.csv" # Nom de l'arxiu on es descarregaran les dades

Exemple 2:

CERCA = "Decada 90" # Clave per a realitzar la bùsqueda a SoundCloud
N = 10 # Nombre de vegades que es realitzarà SCROLL per a descarregar les dades
NOM_ARXIU = "/Decada90.csv" # Nom de l'arxiu on es descarregaran les dades

Exemple 3:

CERCA = "Pop Español" # Clave per a realitzar la bùsqueda a SoundCloud
N = 15 # Nombre de vegades que es realitzarà SCROLL per a descarregar les dades
NOM_ARXIU = "/PopEspañol.csv" # Nom de l'arxiu on es descarregaran les dades.


## Llicència

Aquest projecte es distribueix sota la llicència CC BY-SA 4.0. 

Si fas ús d'aquesta eina, recorda respectar els drets d'autor i les polítiques de privadesa de SoundCloud.


## DOI de Zenodo

El conjunt de dades generat en aquest projecte té un DOI de Zenodo. Podeu accedir-hi aquí: 

[enllaç al DOI] https://doi.org/10.5281/zenodo.10115525


## Contacte

Per a preguntes, suggeriments o problemes, posa't en contacte amb els autors a qualsevol de les adreces de correu electrònic adjuntes.


> **Data:** 14/11/2023
