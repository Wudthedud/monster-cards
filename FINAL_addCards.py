"""FINAL_addCards.py.

adds card to dictionary
"""
import shelve
import easygui as eg


def add_card(name):
    """Asks for name and stats, adds to dictionary once confirmed."""
    d = shelve.open("cards.txt")
    data = d["cards"]
    try:
        if name in data:
            eg.msgbox(f"The card '{name.capitalize()} already exists",
                      "Cancelled add card")
            return
        stats = []
        key = ["strength", "speed", "stealth", "cunning"]
        for i in range(4):
            while True:
                stat = eg.integerbox(f"Enter {key[i]} (1-25):", "Add card",
                                     lowerbound=1, upperbound=25)
                if stat is None:
                    eg.msgbox("Operation cancelled", "Add card")
                    return
                break
            stats.append(stat)

        if eg.ynbox(f"Are all the details correct?"
                    f"\n\n---{name.capitalize()}---"
                    f"\nStrength: {stats[0]}\nSpeed: {stats[1]}\nStealth: "
                    f"{stats[2]}\nCunning: {stats[3]}", "Add card"):
            data[name] = stats
            d["cards"] = data
            d.close()
            eg.msgbox("Card added!", "Add card")
        else:
            choice = eg.ynbox("Would you like to try again?", "Add card")
            if choice:
                name = eg.enterbox("What is the name of the card "
                                   "you would like to add?", "Add card")
                add_card(name)
            else:
                return
    except TypeError:
        return