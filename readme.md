Titre du projet :Automatiser l’achat d’une carte graphique 

Une petite description du projet:
En ce moment les cartes graphiques sont énormément sollicitées, ce qui fait qu’elles sont souvent en rupture de stock et donc difficiles à trouver.
C’est pour cela que nous avons eu l’idée de faire un construire un programme qui, grâce à la technique du web scraping, achète automatiquement un article sur une site de vente en ligne.
Dans notre cas, c’est le site "Rue de commerce".

Pour commencer:
Le langage de programmation utilisé est celui de Python(c’est préférable d’avoir Spyder).
Installation
On commence par installer les différents outils et packages tels que Web driver, Selenium,  BeautifulSoup, Pandas, google chrome

Pour les installer :
pip install selenium
pip install python-chromedriver-binary
pip install pandas
pip install bs4
pip install webdriver-manager
pip install -c conda-forge python-chromedriver-binary 

Fonctionnement du programme :
En lançant notre programme (Run File ou F5) et après que le WebDriver s’est lancé (il n’y a rien dedans), on aura deux possibilités (ou options) :

Choisissez une option:
1 - Acheter un article déjà choisi
2 - Acheter un article en fonction d'un budget

Première option : Si on tape "1" dans le terminal on sait précisément quel article(carte graphique précise) on veut acheter.
Dans ce cas, on doit juste entrer entrer l’URL précis de l’article(du site Rue du Commerce) qu’on veut et il sera acheté automatiquement.
S’il est en rupture de stock, on sera notifié et la page va s’actualiser toutes les 10 secondes jusqu’à ce que l’article soit de nouveau disponible et va l’acheter automatiquement. 

Deuxième option : Si on a un budget bien défini, le programme achètera automatiquement le premier modèle d’article, ici une carte graphique, qui entrera dans notre budget.
Dans ce cas, on commencera par entrer notre budget, par exemple 1300 euros, ensuite le programme va parcourir la page et lister toutes les cartes graphiques disponibles sur la page et va nous les afficher dans un tableau (modèle, prix, disponibilité, etc.).
Enfin, il va acheter automatiquement le premier article de notre liste qui aura un prix inférieur ou égal à 1300 euros. S’il n’y a pas de carte graphique adaptée à notre budget, la page va s’actualiser (jusqu’à ce qu’il y ait de nouveau une carte graphique)


Les fonctions utilisées pour le programme :

•	Fonction acheter : Elle permet d’acheter l’article souhaité grâce à un URL
•	Fonction acheter_2 : Elle porte des légères modification pour nous permettre d’ouvrir d’autres page web 
•	Fonction CheckForStock : Elle nous permet de lister les carte graphique disponible sur un URL 
•	Fonction LessThan : Elle appelle la fonction CheckForStock et achète le premier article qu’on a listé (pour la deuxième partie du projet )
•	Fonction check dispo pour la première partie du projet il regarde si l’article est disponible elle achète a l’aide de la fonction acheter 
•       Fonction BuyOne pour la premiere partie de projet elle nous permet de renter le lien de l’article après elle appelle la fonction checkDispo 
•       Fonction BuyOne pour la deuxième partie de projet elle nous permet de renter le prix  de l’article ( notre budget ) après elle appelle la fonction LessThan 



Les liens pour tester la première fonction :

Après avoir cliqué sur "1",  voici le lien pour tester si l’article est disponible  : https://www.rueducommerce.fr/p-tuf-gaming-dash-tuf516pm-hn206w-gris-eclipse-asus-3352194-28409.html?articleOfferId=30933564    
si l’article est en rupture de stock : https://www.rueducommerce.fr/produit/msi-radeon-rx-5700-xt-evoke-oc-8-go-ddr6-84085528?awc=6901_1644163829_b0b823a45151fe0dfea76b2a4862a5fc

Si vous choisissez l'option "2",veuillez juste indiquer votre budget: 1300 €


Auteurs

Fervent BATINA , Osman GULLU , Othmane PANI