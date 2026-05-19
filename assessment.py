import easygui

cards = {"Lunala": {"HP": "250",
                    "Type": "Psychic",
                    "Number": "792",
                    "Generation": "7",
                    "Comment": "It is a holographic GX card"},
         "Dragonair":{"HP": "90",
                      "Type": "Dragon",
                      "Number": "148",
                      "Generation": "1",
                      "Comment": "It's illustration was done by Hatachu"},
        "Pikachu":{"HP": "40",
                   "Type": "Electric",
                   "Number": "25",
                   "Generation": "1",
                   "Comment": "The original pikachu card. He is round."}}

def main_menu():
    do = easygui.buttonbox("What would you like to do with your pokemon cards?", 
                      choices = ["Add", "Delete", "View", "Quit"])
    if do == "Add":
        add()

    elif do == "Delete":
        delete()

    elif do == "View":
        view()
    

    elif do == "Quit":
        quit ()

def add():
    while True:
        name = easygui.enterbox("Please enter your pokemon's name:")
        cards[name] = {}
        hp = easygui.enterbox("Please enter your pokemons's HP:")
        cards[name] ["HP"] = hp
        type = easygui.enterbox("Please enter your pokemon's type:")
        cards[name] ["Type"] = type
        number = easygui.enterbox("Please enter your pokemon's pokedex number:")
        cards[name] ["Number"] = number
        gen = easygui.enterbox("Please enter your pokemon's generation:")
        cards[name] ["Generation"] = gen
        mm = easygui.ynbox("Do you have any additional comments about the card?")
        if mm == True:
            comment = easygui.enterbox("Please write any comments:")
            cards[name] ["Comment"] = comment
        print(cards)
        again = easygui.buttonbox("Would you like to add another pokemon?",
                                choices = ["Yes", "No"])
        if again == "No":
            main_menu()

def delete():
    while True:
        choice_list = []
        for x in cards:
            choice_list.append(x)  
        pokemon = easygui.enterbox("Which card would you like to remove?")
        while pokemon not in cards:
            uh_oh = easygui.buttonbox("""Sorry, that card is not in our system.
                               Please check spelling and try again,
                               or return to main menu.""",
                               choices = ["Enter again", "Main Menu"])
            if uh_oh == "Enter again":
                pokemon = easygui.enterbox("Which card would you like to remove?")

            elif uh_oh == "Main Menu":
                main_menu()
            
        kill = easygui.buttonbox("Are you sure you want to delete " + 
                               pokemon + "?",choices = ["Yes", "No"])
        if kill == "Yes":
            pop_cards = cards.pop(pokemon)
            easygui.msgbox(str(pokemon) + " has been deleted")
            again = easygui.buttonbox("Would you like to remove another card?",
                                    choices = ["Yes","No"])
            if again == "No":
                main_menu()

def view():
    card_choice = easygui.buttonbox("""Would you like to view all card info, 
                      or just one card?""",
                      choices = ["All Cards", "One Card"])
    
    if card_choice == "All Cards":
        easygui.msgbox("Please look at the output printed to Shell:")
        
        for card_id, card_info in cards.items():
            print("\nCard:", card_id)

            for key in card_info:
                    print (key + ":", card_info[key])

        options = easygui.buttonbox("""Would you like to view a solo card 
                          or return to menu?""",
                          choices = ["Solo Card", "Main Menu"])
        
        if options == "Main Menu":
            main_menu()

        elif options == "Solo Card":
            one_card()

    if card_choice == "One Card":
        one_card()
        
       
def one_card():
    while True:
        specific_card = easygui.enterbox("Which card would you like to view?")
        while specific_card not in cards:
            uh_oh = easygui.buttonbox("""Sorry, that card is not in our system.
                                Please check spelling and try again,
                                or return to main menu.""",
                                choices = ["Enter again", "Main Menu"])
            if uh_oh == "Enter again":
                specific_card = easygui.enterbox("""Which card would 
                                                    you like to view?""")

            elif uh_oh == "Main Menu":
                main_menu()

        easygui.msgbox(cards[specific_card], title = specific_card + " info:")
        again = easygui.ynbox("Would you like to view another card?")
        if again is False:
            main_menu()
            


main_menu()



    


