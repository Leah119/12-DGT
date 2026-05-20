cards = {}

def main_menu():
    do = easygui.buttonbox("What would you like to do with your pokemon cards?", 
                      choices = ["Add", "Delete", "View", "Quit"])
    if do == "Add":
        add()

    elif do == "Delete":
        delete()

    elif do == "View":
        print("We will do this")

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
        pokemon = easygui.choicebox("Which card would you like to remove?", 
                                    choices = choice_list)
        kill = easygui.buttonbox("Are you sure you want to delete " + 
                               pokemon + "?",choices = ["Yes", "No"])
        if kill == "Yes":
            pop_cards = cards.pop(pokemon)
            easygui.msgbox(str(pokemon) + " has been deleted")
            again = easygui.buttonbox("Would you like to remove another combo?",
                                    choices = ["Yes","No"])
            if again == "No":
                main_menu()

main_menu()
