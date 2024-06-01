"""FINAL_monsterCards.py.

main program that calls other functions, welcome message and string checker
"""
import sys
import easygui as eg
from FINAL_addCards import add_card
from FINAL_printCards import print_gui
from FINAL_searchCards import search_card
from FINAL_removeCard import remove_card
from FINAL_cardsDict import reset


def welcome():
    """Welcome message, and option to reset catalogue."""
    msg = (
        "Welcome to the Monster Card Game Catalogue!\n"
        "This program allows you to manage a collection of monster cards.\n\n"
        "Menu Options:\nAdd a new monster card: "
        "Create a new card and assign statistics to it.\n"
        "Search for a monster card: Find an existing card and "
        "verify its details, with the option to edit or remove if required.\n"
        "Delete a monster card: Remove a card from the catalogue.\n"
        "Exit: Quit the program.\n\n"
        "Note: Any changes made to the catalogue will apply even when the "
        "program is closed. If you wish to reset the catalogue to it's "
        "default state, press the 'reset' button below.")
    welcome_choice = eg.buttonbox(msg, "Welcome",
                                  ["Continue", "Reset catalogue", "Exit"])
    if welcome_choice == "Exit":
        sys.exit()
    elif welcome_choice == "Reset catalogue":
        reset()
        eg.msgbox("Operation complete", "Reset catalogue")
    else:
        return


def input_check(question):
    """Check name input is valid and not empty."""
    while True:
        user_input = eg.enterbox(f"What is the name of the card you would"
                                 f" like to {question}?",
                                 f"{question.capitalize()} card")
        if user_input == "":
            retry = eg.ynbox("This field cannot be empty\nTry again?",
                             f"{question.capitalize()} card")
            if not retry:
                eg.msgbox("Operation cancelled",
                          f"{question.capitalize()} card")
                return None
        elif user_input is None:
            eg.msgbox("Operation cancelled",
                      f"{question.capitalize()} card")
            return None
        elif not user_input.isalpha():
            retry = eg.ynbox("This field can only contain alphabetic "
                             "characters\nTry again?",
                             f"{question.capitalize()} card")
            if not retry:
                eg.msgbox("Operation cancelled",
                          f"{question.capitalize()} card")
                return None
        else:
            return user_input.lower().strip()


def main():
    """Display main menu."""
    while True:
        choice = eg.buttonbox("Welcome to Monster Cards Catalogue\n"
                              "What would you like to do?", "Welcome",
                              ["Add card", "Remove card",
                               "Search for card", "Print cards", "Exit"])
        if choice == "Add card":
            name = input_check("add")
            if name is not None:
                add_card(name)
        elif choice == "Remove card":
            remove_card()
        elif choice == "Search for card":
            search_card()
        elif choice == "Print cards":
            print_gui()
        elif choice == "Exit":
            eg.msgbox("Goodbye")
            sys.exit()


if __name__ == "__main__":
    welcome()
    main()