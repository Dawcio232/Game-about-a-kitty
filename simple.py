import time

# Language dictionaries
TEXT = {
    "en": {
        "welcome": "Welcome to the adventure of Whiskers, the cool cat!",
        "wake": "Whiskers wakes up in the middle of a sunny field, ready to explore the world.",
        "where": "Where should Whiskers go?",
        "north": "1. North to the snowy mountains",
        "east": "2. East to the bustling city",
        "south": "3. South to the sandy beach",
        "west": "4. West to the mysterious forest",
        "choose": "Type 1, 2, 3, or 4 to choose a direction: ",
        "invalid": "Please enter a valid option (1-4).",
        "mountains": "\nWhiskers heads north and finds the snowy mountains!",
        "mountains2": "It's cold, but Whiskers finds a friendly snow fox to play with.",
        "mountains3": "After a fun day, Whiskers decides to head home. Adventure complete!",
        "city": "\nWhiskers strolls east into the bustling city.",
        "city2": "There are lots of people and tall buildings. Whiskers finds a cozy café and gets a treat.",
        "city3": "Satisfied, Whiskers returns home. Adventure complete!",
        "beach": "\nWhiskers pads south to the sandy beach.",
        "beach2": "The sun is warm and the waves are gentle. Whiskers chases crabs and naps in the sun.",
        "beach3": "After a relaxing day, Whiskers heads home. Adventure complete!",
        "forest": "\nWhiskers wanders west into the mysterious forest.",
        "forest2": "The trees are tall and the air is cool. Whiskers meets an owl who tells stories of the forest.",
        "forest3": "With new friends and stories, Whiskers returns home. Adventure complete!",
        "home": "Whiskers is back home, tired but happy, he got pretty full after that treat.",
        "again": "Would you like to go on another adventure, or do you want to rest? (adventure/rest): ",
        "adventure": "Whiskers is ready for another adventure!",
        "rest": "Whiskers decides to take a nap. Adventure complete!",
        "invalid_ar": "Please enter a valid option (adventure/rest).",
        "lang": "Choose language / Wybierz język (en/pl): ",
        "invalid_lang": "Invalid language, defaulting to English."
    },
    "pl": {
        "welcome": "Witaj w przygodzie Wąsacza, fajnego kota!",
        "wake": "Wąsacz budzi się na środku słonecznej łąki, gotowy odkrywać świat.",
        "where": "Dokąd powinien pójść Wąsacz?",
        "north": "1. Na północ, w śnieżne góry",
        "east": "2. Na wschód, do tętniącego życiem miasta",
        "south": "3. Na południe, na piaszczystą plażę",
        "west": "4. Na zachód, do tajemniczego lasu",
        "choose": "Wpisz 1, 2, 3 lub 4, aby wybrać kierunek: ",
        "invalid": "Wpisz poprawną opcję (1-4).",
        "mountains": "\nWąsacz rusza na północ i trafia w śnieżne góry!",
        "mountains2": "Jest zimno, ale Wąsacz poznaje przyjaznego lisa polarnego.",
        "mountains3": "Po wesołym dniu Wąsacz wraca do domu. Przygoda zakończona!",
        "city": "\nWąsacz idzie na wschód do tętniącego życiem miasta.",
        "city2": "Wokół mnóstwo ludzi i wysokich budynków. Wąsacz znajduje przytulną kawiarnię i dostaje smakołyk.",
        "city3": "Najedzony i zadowolony, Wąsacz wraca do domu. Przygoda zakończona!",
        "beach": "\nWąsacz podąża na południe, na piaszczystą plażę.",
        "beach2": "Słońce grzeje, a fale są łagodne. Wąsacz goni kraby i drzemię w słońcu.",
        "beach3": "Po relaksującym dniu Wąsacz wraca do domu. Przygoda zakończona!",
        "forest": "\nWąsacz wędruje na zachód, do tajemniczego lasu.",
        "forest2": "Drzewa są wysokie, a powietrze rześkie. Wąsacz spotyka sowę, która opowiada leśne historie.",
        "forest3": "Z nowymi przyjaciółmi i opowieściami Wąsacz wraca do domu. Przygoda zakończona!",
        "home": "Wąsacz wraca do domu, zmęczony, ale szczęśliwy, najadł się po smakołyku.",
        "again": "Chcesz przeżyć kolejną przygodę, czy odpocząć? (przygoda/odpoczynek): ",
        "adventure": "Wąsacz jest gotowy na kolejną przygodę!",
        "rest": "Wąsacz postanawia się zdrzemnąć. Przygoda zakończona!",
        "invalid_ar": "Wpisz poprawną opcję (przygoda/odpoczynek).",
        "lang": "Choose language / Wybierz język (en/pl): ",
        "invalid_lang": "Nieprawidłowy język, domyślnie angielski."
    }
}

lang = "en"

def set_language():
    global lang
    choice = input(TEXT["en"]["lang"]).strip().lower()
    if choice == "pl":
        lang = "pl"
    elif choice == "en":
        lang = "en"
    else:
        print(TEXT["en"]["invalid_lang"])
        lang = "en"

def intro():
    # Cute ASCII cat face
    print(r"""
      /\_/\  
     ( o.o ) 
      > ^ <  
    """)
    # Big text banner
    if lang == "pl":
        print("""
| |      | |   | |   | |   | |   | |   | |   | |   | |   | |   | |   | |   | |
| | WĄSACZ - PRZYGODA KOTA | | 
| |      | |   | |   | |   | |   | |   | |   | |   | |   | |   | |   | |   | |
""")
    else:
        print("""
| |      | |   | |   | |   | |   | |   | |   | |   | |   | |   | |   | |   | |
| |   WHISKERS ADVENTURE   | | 
| |      | |   | |   | |   | |   | |   | |   | |   | |   | |   | |   | |   | |
""")
    # Print the intro with bold text using ANSI escape codes
    print("\033[1m" + TEXT[lang]["welcome"] + "\033[0m")
    time.sleep(1)
    print("\033[1m" + TEXT[lang]["wake"] + "\033[0m")
    time.sleep(1)
    print("\033[1m" + TEXT[lang]["where"] + "\033[0m")
    time.sleep(1)
    print(TEXT[lang]["north"])
    print(TEXT[lang]["east"])
    print(TEXT[lang]["south"])
    print(TEXT[lang]["west"])
    print()

def choose_direction():
    while True:
        choice = input(TEXT[lang]["choose"]).strip()
        if choice == '1':
            mountains()
            break
        elif choice == '2':
            city()
            break
        elif choice == '3':
            beach()
            break
        elif choice == '4':
            forest()
            break
        elif choice == '5':
            genius()
            break
        elif choice == 'genius':  # Optional: allow the word 'genius' as a secret
            genius()
            break
        else:
            # Only print invalid if not the secret option
            if choice not in ['5', 'genius']:
                print(TEXT[lang]["invalid"])

def mountains():
    print(TEXT[lang]["mountains"])
    time.sleep(1)
    print(TEXT[lang]["mountains2"])
    time.sleep(1)
    print(TEXT[lang]["mountains3"])

def city():
    print(TEXT[lang]["city"])
    time.sleep(1)
    print(TEXT[lang]["city2"])
    time.sleep(1)
    print(TEXT[lang]["city3"])

def beach():
    print(TEXT[lang]["beach"])
    time.sleep(1)
    print(TEXT[lang]["beach2"])
    time.sleep(1)
    print(TEXT[lang]["beach3"])

def forest():
    print(TEXT[lang]["forest"])
    time.sleep(1)
    print(TEXT[lang]["forest2"])
    time.sleep(1)
    print(TEXT[lang]["forest3"])

def main_game_loop():
    while True:
        intro()
        choose_direction()
        print(TEXT[lang]["home"])
        time.sleep(1)
        if lang == "pl":
            choice = input(TEXT[lang]["again"]).strip().lower()
            if choice == 'przygoda':
                print(TEXT[lang]["adventure"])
                continue
            elif choice == 'odpoczynek':
                print(TEXT[lang]["rest"])
                break
            else:
                print(TEXT[lang]["invalid_ar"])
        else:
            choice = input(TEXT[lang]["again"]).strip().lower()
            if choice == 'adventure':
                print(TEXT[lang]["adventure"])
                continue
            elif choice == 'rest':
                print(TEXT[lang]["rest"])
                break
            else:
                print(TEXT[lang]["invalid_ar"])
def genius():
    if lang == "pl":
        print("\nPróbowałeś wybrać geniusza, ale Wąsacz nie zna takiej drogi!")
        time.sleep(2)
        print("Chciałeś przechytrzyć grę, ale Wąsacz jest sprytny i nie da się tak łatwo oszukać!")
        time.sleep(2)
        print("Za karę kicia musi teraz odpocząć i pomyśleć nad swoimi wyborami.")
        time.sleep(5)
        print("Łał, nie wiedziałem, że będziesz czekać tak długo, ale Wąsacz jest cierpliwy i gotowy na kolejną przygodę!")
    else:
        print("\nYou tried to choose genius, but Whiskers doesn't know that path!")
        time.sleep(2)
        print("You tried to outsmart the game, but Whiskers is clever and can't be fooled so easily!")
        time.sleep(2)
        print("As a penalty, the kitty must rest and think about their choices.")
        time.sleep(5)
        print("Wow, I didn't think you'd wait so long, but Whiskers is patient and ready for another adventure!")

if __name__ == "__main__":
    set_language()
    main_game_loop()