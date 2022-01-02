import sys
import pprint
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time


# selectionne le chrome drive à utiliser
drive = webdriver.Chrome(executable_path='chromedriver.exe')

# selectionne l'argument passé lors de l'execution du script,
# ex : "python loop.py arg 1" ici c'est le .txt spectacles qui est passé. CMD : "python loop.py spectacles.txt"
arg = sys.argv[1]


def traitement(arg):

    tab = []
    T = 0  # compteur pour les differents onglets chrome

    with open(arg, "r", encoding="UTF-8") as fichier:  # ouverture du fichier passé en argument

        lines = fichier.readlines()  # lecture ligne par ligne

        for line in lines:
            # (netoyage) permet dans une chaine de caractere de recuperer uniquament la chaine de caratctere qui est avant le premier pipe en selection "head" .
            head, sep, tail = line.partition('|')

            # ouvre un nouvel onglet dans chrome
            drive.execute_script("window.open()")
            # passe à l'onglet suivant
            drive.switch_to.window(drive.window_handles[T])

            # lance url avec la chaine de caractere selectionnée
            drive.get(f"https://bonlieu-annecy.com/?s={head}")

            try:
                # test si la class existe
                if drive.find_element_by_css_selector('.arrow-link:first-child'):
                    search_btn = drive.find_element_by_css_selector(
                        '.arrow-link:first-child')
                    search_btn.click()  # clic sur bouton correspondant a la class recherché
            except NoSuchElementException:  # si non passe l'erreur
                pass

            T = T+1  # + 1 au compteur d'onglet
            tab.append(head)
            # time.sleep(2)

    print(f'ma liste :{tab}')


# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint (line)
traitement(arg)
