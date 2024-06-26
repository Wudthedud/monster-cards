"""FINAL_search_cards.

Search for a card and returns its details, option to edit if user wants to
"""
import shelve
import easygui as eg
from FINAL_removeCard import remove_card


def input_check():
    """Check name input is valid and not empty."""
    while True:
        user_input = eg.enterbox("What would you like to rename "
                                 "the card to?", "Edit card")
        if user_input == "":
            retry = eg.ynbox("This field cannot be empty\nTry again?",
                             "Edit card")
            if not retry:
                eg.msgbox("Operation cancelled", "Edit card")
                return None
        elif user_input is None:
            eg.msgbox("Operation cancelled", "Edit card")
            return None
        elif not user_input.isalpha():
            retry = eg.ynbox("This field can only contain alphabetic "
                             "characters\nTry again?",
                             "Edit card")
            if not retry:
                eg.msgbox("Operation cancelled", "Edit card")
                return None
        else:
            return user_input.lower().strip()


def search_card(name=None):
    """Search for card within the dictionary, if found prints card details."""
    from FINAL_monsterCards import main
    while True:
        d = shelve.open("cards.txt")
        data = d["cards"]
        d.close()
        if name is None:
            keys = [key.title() for key in data.keys()]
            name = eg.choicebox("Which card would you like to search "
                                "for?", "Search/Edit card", keys)
            if name is None:
                eg.msgbox("Operation cancelled", "Search/Edit card")
                return

        name = name.lower()
        stats = data.get(name)
        choice = eg.buttonbox(f"Card found:\n\n---{name.capitalize()}---"
                              f"\nStrength: {stats[0]}\nSpeed: {stats[1]}\n"
                              f"Stealth: {stats[2]}\nCunning: {stats[3]}\n"
                              f"\nWhat would you like to do?",
                              "Search for a card",
                              ["Edit card", "Remove Card", "Go back"])
        if choice == "Edit card":
            choice2 = eg.buttonbox("What would you like to edit",
                                   "Edit a card", ["Edit name",
                                                   "Edit stats", "Go back"])
            if choice2 == "Edit name":
                edit_name(name)
                break
            elif choice2 == "Edit stats":
                edit_stats(name)
                break
            else:
                main()
                break
        elif choice == "Remove Card":
            remove_card(name)
            return
        else:
            main()


def edit_name(name):
    """Edit a key within a dictionary."""
    d = shelve.open("cards.txt")
    data = d["cards"]
    stats = data.get(name)
    while True:
        new_name = input_check()
        if new_name is None:
            search_card(name)
            return

        if new_name in data:
            try_again = eg.ynbox(f"The card '{new_name.capitalize()}'"
                                 f" already exists\nTry again?",
                                 "Edit card")
            if not try_again:
                d.close()
                search_card(name)
                return
        else:
            confirm = eg.ynbox(
                f"Here is your edited card:\n\n---{new_name.capitalize()}"
                f"---\nStrength: {stats[0]}\nSpeed: {stats[1]}\nStealth: "
                f"{stats[2]}\nCunning: {stats[3]}\n\nConfirm?", "Edit card"
            )
            if confirm:
                data[new_name] = data.pop(name)
                d["cards"] = data
                d.close()
                eg.msgbox("Operation complete", "Edit card")
                search_card(new_name)
                return
            else:
                d.close()
                eg.msgbox("Operation cancelled", "Edit card")
                search_card(name)
                return


def edit_stats(name):
    """Edit a key's data within a dictionary."""
    d = shelve.open("cards.txt")
    data = d["cards"]
    stats = data.get(name)
    while True:
        choice = eg.buttonbox("Which statistic would you like to edit?"
                              f"\n\n---{name.capitalize()}---\nStrength: "
                              f"{stats[0]}\nSpeed: {stats[1]}\nStealth: "
                              f"{stats[2]}\nCunning: {stats[3]}\n\n",
                              "Edit card", ["Strength", "Speed",
                                            "Stealth", "Cunning", "Cancel"])
        if choice in ["Strength", "Speed", "Stealth", "Cunning"]:
            new_stat = eg.integerbox(f"What would you like to change the "
                                     f"{choice.lower()} to?",
                                     "Edit card", lowerbound=1,
                                     upperbound=25)
            if new_stat is None:
                eg.msgbox("Operation cancelled")
                search_card(name)
            elif new_stat == "":
                eg.msgbox("This field cannot be empty", "Edit card")
            key = {"Strength": 0, "Speed": 1, "Stealth": 2, "Cunning": 3}
            stats[key[choice]] = new_stat
            confirm = eg.ynbox(f"Here is your new card:"
                               f"\n\n---{name.capitalize()}---\nStrength: "
                               f"{stats[0]}\nSpeed: {stats[1]}\nStealth: "
                               f"{stats[2]}\nCunning: {stats[3]}\n\nConfirm?",
                               "Edit card")
            if confirm:
                data[name] = stats
                eg.msgbox("Operation completed", "Edit card")
                d["cards"] = data
                d.close()
                search_card(name)
                break
            else:
                eg.msgbox("Operation cancelled")
                search_card(name)
                break
        else:
            search_card(name)
            break