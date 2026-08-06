"""The Pokemon Card Storer.

This programme is designed to store the user's Pokemon cards,
and allow them to add, edit, delete,
and view the cards that they have stored.
"""


import easygui

cards = {"Lunala": {"HP": "250",
                    "Type": "Psychic",
                    "Number": "792",
                    "Generation": "7",
                    "Comment": "It is a holographic GX card"},
         "Dragonair": {"HP": "90",
                       "Type": "Dragon",
                       "Number": "148",
                       "Generation": "1",
                       "Comment": "It's illustration was done by Hatachu"},
         "Pikachu": {"HP": "60",
                     "Type": "Electric",
                     "Number": "25",
                     "Generation": "1",
                     "Comment": "The original pikachu card. He is round."}}


def main_menu():
    """Display the main menu.

    This function allows the user to see all the options available for their
    Pokemon cards, whether it's editing, viewing, deleting, adding, or quitting
    the programme.
    """
    do = easygui.buttonbox("What would you like to you do with your cards?",
                           choices=["Add",
                                    "Delete",
                                    "View",
                                    "Edit",
                                    "Quit"])
    if do == "Add":
        add()

    elif do == "Delete":
        delete()

    elif do == "View":
        view()

    elif do == "Edit":
        edit()

    elif do == "Quit":
        quit()


def add():
    """Add a new Pokemon card.

    This function allows the user to add a new pokemon card to their viewable
    collection.
    """
    while True:
        name = easygui.enterbox("Please enter the pokemon's name:")
        while name == "":
            easygui.msgbox("That is an invalid entry. Please try again.")
            name = easygui.enterbox("Please enter the pokemon's name:")    
        cards[name] = {}
        hp = easygui.integerbox("Please enter the pokemons's HP:\n"
        "(Range: 1-500)", lowerbound = 1, upperbound = 500)
        cards[name]["HP"] = hp
        type = easygui.enterbox("Please enter the pokemon's type:")
        cards[name]["Type"] = type
        number = easygui.integerbox("Please enter the pokemon's pokedex number:\n" 
        "(Range: 1-1000)", lowerbound = 1, upperbound = 1000)
        cards[name]["Number"] = number
        gen = easygui.enterbox("Please enter the pokemon's generation:")
        while gen == "":
                easygui.msgbox("That is an invalid entry. Please try again.")
                gen = easygui.enterbox("Please enter the pokemon's name:") 
        cards[name]["Generation"] = gen
        mm = easygui.ynbox("Are there any additional comments about the card?")
        if mm is True:
            comment = easygui.enterbox("Please write any comments:")
            cards[name]["Comment"] = comment
        again = easygui.buttonbox("Would you like to add another pokemon?",
                                  choices=["Yes", "No"])
        if again == "No":
            main_menu()


def delete():
    """Delete a pre-existing Pokemon card.

    This function allows the user to delete a card from their dictionary.
    """
    while True:
        choice_list = []
        for x in cards:
            choice_list.append(x)
        pokemon = easygui.enterbox("Which card would you like to remove?")
        pokemon = pokemon.capitalize()
        while pokemon not in cards:
            uh_oh = easygui.buttonbox("""Sorry, that card is not in our system.
                                      Please check spelling
                                      and try again,or return to main menu.""",
                                      choices=["Enter again", "Main Menu"])
            if uh_oh == "Enter again":
                pokemon = easygui.enterbox("""Which card would
                                           you like to remove?""")

            elif uh_oh == "Main Menu":
                main_menu()

        kill = easygui.buttonbox("Are you sure you want to delete " +
                                 pokemon + "?", choices=["Yes", "No"])
        if kill == "Yes":
            cards.pop(pokemon)
            easygui.msgbox(str(pokemon) + " has been deleted")
            again = easygui.buttonbox("Would you like to remove another card?",
                                      choices=["Yes", "No"])
            if again == "No":
                main_menu()


def view():
    """View one or all preexisting Pokemon cards.

    This function allows the user to view a pokemon card's info from their
    collection, or view all cards at once.
    """
    card_choice = easygui.buttonbox("""Would you like to view all card info,
                                    or just one card?""",
                                    choices=["All Cards", "One Card"])

    if card_choice == "All Cards":
        easygui.msgbox("Please look at the output printed to Shell:")

        for card_id, card_info in cards.items():
            print("\nCard:", card_id)

            for key in card_info:
                print(key + ":", card_info[key])

        options = easygui.buttonbox("""Would you like to view a solo card
                                    or return to menu?""",
                                    choices=["Solo Card", "Main Menu"])

        if options == "Main Menu":
            main_menu()

        elif options == "Solo Card":
            one_card()

    if card_choice == "One Card":
        one_card()


def one_card():
    """View a single card.

    This function allows the user to view one specific card
    from their collection.
    """
    while True:
        specific_card = easygui.enterbox("Which card would you like to view?")
        specific_card = specific_card.capitalize()
        while specific_card.capitalize() not in cards:
            uh_oh = easygui.buttonbox("""Sorry, that card is not in our system.
                                      Please check spelling and try again,
                                      or return to main menu.""",
                                      choices=["Enter again", "Main Menu"])
            if uh_oh == "Enter again":
                one_card()

            elif uh_oh == "Main Menu":
                main_menu()

        easygui.msgbox(cards[specific_card], title=specific_card + " info:")

        name = specific_card
        directory = r"C:\Users\Leah\Documents\DGT Python\assessment_stuff"
        file_name = (f"{directory}\{name.lower()}.png")
        easygui.msgbox("This is the pokemon", image=file_name)

        again = easygui.ynbox("Would you like to view another card?")
        if again is False:
            main_menu()


def edit():
    """Edit a Pokemon card.

    This function allows the user to edit a preexisting card
    from their collection.
    """
    choice_list = []
    for x in cards:
        choice_list.append(x)

    choice = easygui.choicebox("Which card would you like to edit?",
                               choices=choice_list)

    change = easygui.buttonbox("Are you sure about editing " + choice + " ?",
                               choices=["Yes", "No"])
    if change == "Yes":
        value_list = []
        for x in cards[choice]:
            value_list.append(x)

        while True:
            value = easygui.buttonbox("Which value would you like to change?",
                                      choices=value_list)

            new = easygui.enterbox("What would you like to change it to?")

            cards[choice][value] = new
            easygui.msgbox("The values for " + choice +
                           " are now: " + str(cards[choice]))
            repeat = easygui.buttonbox("Would you like to edit another value?",
                                       choices=["Yes", "No"])
            if repeat == "No":
                menu_card = easygui.buttonbox("""Would you like to edit another
                                              card or return to main menu?""",
                                              choices=["Edit another",
                                                       "Main Menu"])
                if menu_card == "Edit another":
                    edit()

                elif menu_card == "Main Menu":
                    main_menu()

    elif change == "No":
        menu_card = easygui.buttonbox("""Would you like to edit another card or
                           return to main menu?""", choices=["Edit another",
                                                             "Main Menu"])
        if menu_card == "Edit another":
            edit()

        elif menu_card == "Main Menu":
            main_menu()


easygui.msgbox("Welcome to the Pokemon card storer!")
main_menu()
