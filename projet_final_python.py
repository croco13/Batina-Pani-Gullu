
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import random
import time
import pandas as pd
import bs4
from bs4 import BeautifulSoup
import re

 
option = webdriver.ChromeOptions()
 
wd = webdriver.Chrome(ChromeDriverManager().install())

wd.implicitly_wait(10)


def checkForStock(url):
    
    wd = webdriver.Chrome(ChromeDriverManager().install())
    # Prendre le nom de domaine du site
    site_base_url = '/'.join(url.split('/')[:3])
    #Accéder au lien
    wd.get(url)
    #accepter les 
    tout_accepter=wd.find_element_by_xpath('//*[@id="rgpd-btn-index-accept"]')
    tout_accepter.click()
    # Initialisation
    soup = BeautifulSoup(wd.page_source,features="html.parser")
    items_processed = []
    # Obtenir le nombre d'articles
    nb_articles = soup.find("span", {"class": "products-count"}).text
    # Boucle sur les articles de la page
    for i in range(int(nb_articles)):
        # initialiser 'row' par les élément de 'article'
        row=soup.find("article" , {'item item-{}'.format(str(i))})
        row_processed = []
        # stockage des éléments d'article dans des variables
        itemTitle = row.find("h2", {"class": "item__title"})
        itemPromoText = row.find("span", {"class": "item__promo--percent"})
        itemPrice = row.find("p", {"class": "item__price"})
        #print(itemTitle)
           
        # la vérification et le remplissage du tableau
        if itemTitle:
            row_processed.append(itemTitle.text)
        else :
            row_processed.append(None)
        if itemPrice :   
            price = itemPrice.find("span",{"class":"item__price--new-box"}).text
            # commutation du , avec .
            price = re.sub(',','.',price)
            # commutation du € et \n avec espace
            price = re.sub('€| |\n','',price)
            # la vérification du prix, si disponible ou non
            try:
                price = float(price)
                status = "disponible"
            except:
                price = 0
                status = 'Bientôt Disponible'
            row_processed.append(price)
           
        else :
            row_processed.append(None) 
        # le remplissage de l'url de chaque article
        if itemTitle :   
            # basé sur la combinaison du nom de domaine obtenu et du href dans le titre de l'article 
            row_processed.append(site_base_url+itemTitle.find(href=True)['href'])
            #
        if status :   
            row_processed.append(status)
        else :
            row_processed.append(None)
           
        if row_processed:
            items_processed.append(row_processed)
 
    # le formatage du tableau
    df = pd.DataFrame.from_records(items_processed, columns=["Item Title","Item Price","URL","Status"])
    # commutation du \n avec espace dans le titre de l'article
    df["Item Title"] = df["Item Title"].apply(lambda x: x.replace("\n"," "))
   
    
    return df
    

def acheter_2(lien):
    wd = webdriver.Chrome(ChromeDriverManager().install())
    wd.get(lien)
    tout_accepter=wd.find_element_by_xpath('//*[@id="rgpd-btn-index-accept"]')
    tout_accepter.click()
   
 
    je_foncee=wd.find_element_by_xpath('//*[@id="add-product"]')
    je_foncee.click()
    random_wait_time = random.randrange(5.0, 15.0)
    print(random_wait_time)
    time.sleep(random_wait_time)
    wd.get("https://www.rueducommerce.fr/shopping_cart.html")
    random_wait_time = random.randrange(5.0, 15.0)
    print(random_wait_time)
    time.sleep(random_wait_time)
 
    je_passe_ma_commande=wd.find_element_by_xpath('//*[@id="to-order"]/a')
    je_passe_ma_commande.click()
 
    random_wait_time = random.randrange(2.0, 15.0)
    print(random_wait_time)
    time.sleep(random_wait_time)
 
    adresse_mail=wd.find_element_by_xpath('//*[@id="login"]')
    email = "othmanepani@gmail.com"
    adresse_mail.send_keys(email)
 
    mot_de_passe=wd.find_element_by_xpath('//*[@id="login_pass"]')
    mot_de_passe.send_keys("osmanfervent")
 
    se_connecter=wd.find_element_by_xpath('//*[@id="form_login"]/div/button')
    se_connecter.click()
    random_wait_time = random.randrange(5.0, 15.0)
    print(random_wait_time)
    time.sleep(random_wait_time)
    pas_assurance=wd.find_element_by_xpath('//*[@id="service_0"]/p[1]')
    pas_assurance.click()
    je_passe_ma_commande=wd.find_element_by_xpath('//*[@id="to-order"]/a')
    je_passe_ma_commande.click()
    
    #chrono_post=wd.find_element_by_xpath('//*[@id="block_normal"]/table/tbody/tr[3]/td[1]/div/input')
    #chrono_post.click()
    if wd.find_elements(by=By.XPATH, value='//*[@id="block_normal"]/table/tbody/tr[3]/td[2]/p'):
        chrono_post=wd.find_element_by_xpath('//*[@id="block_normal"]/table/tbody/tr[3]/td[2]/p')
        chrono_post.click()
    
    time.sleep(15.0)
    
    valider_1=wd.find_element_by_xpath('//*[@id="cart-delivery-content"]/div/div[5]/a')
    valider_1.click()
    
    random_wait_time = random.randrange(5.0, 15.0)
    print(random_wait_time)
    time.sleep(random_wait_time)
    
    carte_bancaire=wd.find_element_by_xpath('//*[@id="cart-payment-content"]/div[1]/div[1]/table/tbody/tr[1]/td[3]/p')
    carte_bancaire.click()
    
    random_wait_time = random.randrange(5.0, 15.0)
    print(random_wait_time)
    time.sleep(random_wait_time)
    
    numero_carte=wd.find_element_by_xpath('//*[@id="pl-pm-cards_4-cardNumber"]')
    numero_carte.send_keys("4 1 6 5")
    numero_carte.send_keys("9 8 1 5")
    numero_carte.send_keys("0 1 0 3")
    numero_carte.send_keys("3 1 3 1")
    date_expiration=wd.find_element_by_xpath('//*[@id="pl-pm-cards_4-expirationDate"]')
    date_expiration.send_keys ("0 9")
    date_expiration.send_keys ("2 7")
    crypto = wd.find_element_by_xpath('//*[@id="pl-pm-cards_4-cvv"]')
    crypto.send_keys ("539")
    
    payer_par_carte = wd.find_element_by_xpath('//*[@id="pl-pm-cards_4-payBtn"]')
    payer_par_carte.click()
    
    return 0
 

def acheter(lien):

    tout_accepter=wd.find_element_by_xpath('//*[@id="rgpd-btn-index-accept"]')
    tout_accepter.click()
   
    je_foncee=wd.find_element_by_xpath('//*[@id="add-product"]')
    je_foncee.click()                               
 
 
    finaliser_ma_commande=wd.find_element_by_xpath('//*[@id="popup-add"]/div[1]/p[3]/a[1]')
    finaliser_ma_commande.click()
 
   
    random_wait_time = random.randrange(5.0, 15.0)
    print(random_wait_time)
    time.sleep(random_wait_time)
 
    je_passe_ma_commande=wd.find_element_by_xpath('//*[@id="to-order"]/a')
    je_passe_ma_commande.click()
 
    random_wait_time = random.randrange(5.0, 15.0)
    print(random_wait_time)
    time.sleep(random_wait_time)
   
    adresse_mail=wd.find_element_by_xpath('//*[@id="login"]')
    email = "othmanepani@gmail.com"
    adresse_mail.send_keys(email)
 
 
    mot_de_passe=wd.find_element_by_xpath('//*[@id="login_pass"]')
    mot_de_passe.send_keys("osmanfervent")
   
    
 
 
    se_connecter=wd.find_element_by_xpath('//*[@id="form_login"]/div/button')
    se_connecter.click()
 
    random_wait_time = random.randrange(5.0, 15.0)
    print(random_wait_time)
    time.sleep(random_wait_time)
 
    pas_assurance=wd.find_element_by_xpath('//*[@id="service_0"]/p[1]')
    pas_assurance.click()
 
 
    je_passe_ma_commande=wd.find_element_by_xpath('//*[@id="to-order"]/a')
    je_passe_ma_commande.click()
 
 
    if wd.find_elements(by=By.XPATH, value='//*[@id="block_normal"]/table/tbody/tr[3]/td[2]/p'):
        chrono_post=wd.find_element_by_xpath('//*[@id="block_normal"]/table/tbody/tr[3]/td[2]/p')
        chrono_post.click()
    
    random_wait_time = random.randrange(5.0, 15.0)
    print(random_wait_time)
    time.sleep(random_wait_time)
 
    valider_1=wd.find_element_by_xpath('//*[@id="cart-delivery-content"]/div/div[5]/a')
    #//*[@id="cart-delivery-content"]/div/div[5]/a
    valider_1.click()
   
    random_wait_time = random.randrange(5.0, 15.0)
    print(random_wait_time)
    time.sleep(random_wait_time)
 
    carte_bancaire=wd.find_element_by_xpath('//*[@id="cart-payment-content"]/div[1]/div[1]/table/tbody/tr[1]/td[3]/p')
    carte_bancaire.click()
 
    numero_carte=wd.find_element_by_xpath('//*[@id="pl-pm-cards_4-cardNumber"]')
   
    numero_carte.send_keys("4 1 6 5")
    numero_carte.send_keys("9 8 1 5")
    numero_carte.send_keys("0 1 0 3")
    numero_carte.send_keys("3 1 3 1")
    
 

    date_expiration=wd.find_element_by_xpath('//*[@id="pl-pm-cards_4-expirationDate"]')
    date_expiration.send_keys ("0 9")
    date_expiration.send_keys ("2 7")
 
 
    crypto = wd.find_element_by_xpath('//*[@id="pl-pm-cards_4-cvv"]')
    crypto.send_keys ("539")
 
    payer_par_carte = wd.find_element_by_xpath('//*[@id="pl-pm-cards_4-payBtn"]')
    payer_par_carte.click()
    
    return 0
 
 
 

Price = 1300
URL = "https://www.rueducommerce.fr/rayon/composants-16/nvidia-geforce-rtx-3080-124303"
def lessThan(URL, Price):
    while (True):
        try:
            # l'appele la fonction checkforstock .
            items = checkForStock(URL)
            # choisir les articles à un prix inférieur au prix souhaité et disponible
            in_stock = items[(items["Item Price"]< Price) & (items.Status == "disponible")]
            if not in_stock.empty:
                # prendre le premier article
                item_to_purchase = in_stock.iloc[0]
                # Achète-le
                acheter_2(item_to_purchase["URL"])
                # Puis la boucle se referme
                break
           
            else:
                time.sleep(120)
        except NoSuchElementException:
            # Si le produit demandé n'est pas disponible, les messages suivants s'afficheront
            print("Out of stock")
            print("waiting for some time....")
            time.sleep(120)


 
def checkDispo(URL):  
    while (True) :
        try : 
            #wd.get("https://www.rueducommerce.fr/produit/msi-radeon-rx-5700-xt-evoke-oc-8-go-ddr6-84085528?awc=6901_1644163829_b0b823a45151fe0dfea76b2a4862a5fc")
            wd.get(URL)
            #lien=wd.get("https://www.rueducommerce.fr/p-tuf-gaming-dash-tuf516pm-hn206w-gris-eclipse-asus-3352194-28409.html?articleOfferId=30933564")
            acheter(URL)
           
            break
        except :
            print("il y a plus de stock ")
            print("attend un peu ")
            time.sleep(10)



def buyOne():
    try:
        # Message de demande
        print("Veuillez entrer le lien de l'article") 
        # Mettre l'entrée de l'utilisateur dans une variable
        lien = input()
        # Appeler la fonction "checkDispo"
        checkDispo(lien)
        print("Cet article a été acheté avec succès")
    except NoSuchElementException:
        # si un problème survient, le message suivant s'affichera
        print("un problème est survenu, réessayez s'il vous plait")



def selecOne():
    try:
        # Message de demande
        print("Veuillez entrer une limite de prix")
        # Mettre le prix saisi par l'utilisateur dans une variable
        Price = input()
        # vérification du prix
        #while (int(Price) < 1300):
            #Price = input("erreur : saisie erronée. Veuillez mettre un prix supérieur à "+Price)

        URL = "https://www.rueducommerce.fr/rayon/composants-16/nvidia-geforce-rtx-3080-124303"
        # Appeler la fonction "lessThan"
        lessThan(URL, int(Price))
        # message de réussite
        print("Vous avez réussi à acheter une voiture moins chère que "+Price+" €")
    except NoSuchElementException:
        # si un problème survient, le message suivant s'affichera
        print("un problème est survenu, réessayez s'il vous plait")


print("Choisissez une option:")
print("1 - Acheter un article déjà choisi")
print("2 - Acheter un article en fonction d'un budget")
x = input()
if x == "1":
     buyOne()
elif x == "2": 
    selecOne()
else: 
    print("Veuillez entrer 1 ou 2")

#https://www.rueducommerce.fr/p-tuf-gaming-dash-tuf516pm-hn206w-gris-eclipse-asus-3352194-28409.html?articleOfferId=30933564
#https://www.rueducommerce.fr/produit/msi-radeon-rx-5700-xt-evoke-oc-8-go-ddr6-84085528?awc=6901_1644163829_b0b823a45151fe0dfea76b2a4862a5fc
#https://www.rueducommerce.fr/p-geforce-rtx-2060-twin-fan-12gb-zotac-3358614-18279.html?articleOfferId=27867298
