"""The Pokémon Card Storer.

This programme is designed to store the user's Pokémon cards,
and allow them to add, edit, delete,
and view the cards that they have stored.
"""


import easygui as eg
# This is the nested dictionary, where all card information is added and stored
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
    Pokémon cards, whether it's editing, viewing, deleting, adding, or quitting
    the programme.
    """
    # Allows the user to pick an action, which runs the corresponding function
    do = eg.buttonbox("What would you like to you do with your cards?",
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
    """Add a new Pokémon card.

    This function allows the user to add a new Pokémon card to their viewable
    collection.
    """
    # While loop allows for as many cards to be  added as needed
    while True:
        name = eg.enterbox("Please enter the Pokémon's name:")
        while name == "":  # Checks that a valid name is entered
            eg.msgbox("That is an invalid entry. Please try again.")
            name = eg.enterbox("Please enter the Pokémon's name:")
        cards[name] = {}
        hp = eg.integerbox("Please enter the Pokémons's HP:\n"
                           "(Range: 1-500)", lowerbound=1, upperbound=500)
        cards[name]["HP"] = hp
        type = eg.enterbox("Please enter the Pokémon's type:")
        cards[name]["Type"] = type
        number = eg.integerbox("Please enter the Pokémon's pokedex number:\n"
                               "(Range: 1-1100)", lowerbound=1,
                               upperbound=1100)
        cards[name]["Number"] = number
        gen = eg.enterbox("Please enter the Pokémon's generation:")
        while gen == "":
            eg.msgbox("That is an invalid entry. Please try again.")
            gen = eg.enterbox("Please enter the Pokémon's name:")
        cards[name]["Generation"] = gen
        mm = eg.ynbox("Are there any additional comments about the card?")
        if mm is True:
            comment = eg.enterbox("Please write any comments:")
            cards[name]["Comment"] = comment
        again = eg.buttonbox("Would you like to add another Pokémon?",
                             choices=["Yes", "No"])
        if again == "No":
            main_menu()


def delete():
    """Delete a pre-existing Pokémon card.

    This function allows the user to delete a card from their dictionary.
    """
    while True:
        choice_list = []
        for x in cards:
            choice_list.append(x)  # adds the values to the empty choice_list
        pokémon = eg.enterbox("Which card would you like to remove?")
        pokémon = pokémon.capitalize()
        # This while loop ensures that the Pokémon entered is in the dictionary
        # If it is not, it will allow them to enter again or return to menu
        while pokémon not in cards:
            uh_oh = eg.buttonbox("""Sorry, that card is not in our system.
                                    Please check spelling
                                    and try again,or return to main menu.""",
                                 choices=["Enter again", "Main Menu"])
            if uh_oh == "Enter again":
                pokémon = eg.enterbox("""Which card would
                                           you like to remove?""")

            elif uh_oh == "Main Menu":
                main_menu()
# Asks user for confirmation before deleting the card
        remove = eg.buttonbox("Are you sure you want to delete " +
                              pokémon + "?", choices=["Yes", "No"])
        if remove == "Yes":
            cards.pop(pokémon)
            eg.msgbox(str(pokémon) + " has been deleted")
            again = eg.buttonbox("Would you like to remove another card?",
                                 choices=["Yes", "No"])
            if again == "No":
                main_menu()


def view():
    """View one or all preexisting Pokémon cards.

    This function allows the user to view a Pokémon card's info from their
    collection, or view all cards at once.
    """
    card_choice = eg.buttonbox("""Would you like to view all card info,
                                    or just one card?""",
                               choices=["All Cards", "One Card"])
    if card_choice == "All Cards":
        eg.msgbox("Please look at the output printed to Shell:")
        # Formatting the card info that is printed to shell
        for card_id, card_info in cards.items():
            print("\nCard:", card_id)

            for key in card_info:
                print(key + ":", card_info[key])

        options = eg.buttonbox("""Would you like to view a solo card
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
    # This while loop allows the code to be run as often as necessary
    while True:
        specific_card = eg.enterbox("Which card would you like to view?")
        specific_card = specific_card.capitalize()
        # This while loop forces the user to enter a correct input or exit
        while specific_card.capitalize() not in cards:
            uh_oh = eg.buttonbox("""Sorry, that card is not in our system.
                                      Please check spelling and try again,
                                      or return to main menu.""",
                                 choices=["Enter again", "Main Menu"])
            if uh_oh == "Enter again":
                one_card()

            elif uh_oh == "Main Menu":
                main_menu()

        eg.msgbox(cards[specific_card], title=specific_card + " info:")

        name = specific_card
        # directory tells the code where to find the image files
        directory = r"C:/Users/Leah/Documents/DGT Python/assessment_stuff"
        file_name = (f"{directory}/{name.lower()}.png")
        eg.msgbox("This is the Pokémon", image=file_name)

        again = eg.ynbox("Would you like to view another card?")
        if again is False:
            main_menu()


def edit():
    """Edit a Pokémon card.

    This function allows the user to edit a preexisting card
    from their collection.
    """
    choice_list = []
    for x in cards:
        choice_list.append(x)  # adds the information to the empty choice_list

    choice = eg.choicebox("Which card would you like to edit?",
                          choices=choice_list)

    change = eg.buttonbox("Are you sure about editing " + choice + " ?",
                          choices=["Yes", "No"])
    if change == "Yes":
        value_list = []
        for x in cards[choice]:
            value_list.append(x)  # adds stored card values to the list

        while True:
            value = eg.buttonbox("Which value would you like to change?",
                                 choices=value_list)

            new = eg.enterbox("What would you like to change it to?")

            cards[choice][value] = new  # changing the value to the new input
            eg.msgbox("The values for " + choice +
                      " are now: " + str(cards[choice]))
            repeat = eg.buttonbox("Would you like to edit another value?",
                                  choices=["Yes", "No"])
            if repeat == "No":
                menu_card = eg.buttonbox("""Would you like to edit another
                                              card or return to main menu?""",
                                         choices=["Edit another",
                                                  "Main Menu"])
                if menu_card == "Edit another":
                    edit()

                elif menu_card == "Main Menu":
                    main_menu()

    elif change == "No":
        menu_card = eg.buttonbox("""Would you like to edit another card or
                           return to main menu?""", choices=["Edit another",
                                                             "Main Menu"])
        if menu_card == "Edit another":
            edit()

        elif menu_card == "Main Menu":
            main_menu()


eg.msgbox("Welcome to the Pokémon card storer!")
main_menu()
