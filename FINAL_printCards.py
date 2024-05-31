"""FINAL_printCards.py.

returns card details form txt file, adds easyGUI functionality
"""
import shelve
import easygui as eg


def console_print(data):
    """Print formatted cards to console."""
    for name, card_stats in data.items():
        msg = "\n"
        width = len(name) + 8
        msg += "-" * width
        msg += f"\n|   {name}   |\n"
        msg += "-" * width
        msg += "\n"
        key = ["Strength", "Speed", "Stealth", "Cunning"]
        for i, (key, stat) in enumerate(zip(key, card_stats)):
            stats_msg = f"|{key}: {stat}"
            filler = width - len(stats_msg) - 1
            msg += stats_msg
            msg += " " * filler
            msg += "|\n"
        msg += "-" * width
        print(msg)


def print_gui():
    """Return card data from text file."""
    d = shelve.open("cards.txt")
    data = d["cards"]
    d.close()
    console_print(data)
    eg.msgbox("Cards printed to console", "Print cards")
    keys = list(data.keys())
    pages = []
    for i in range(0, len(keys), 4):
        page_keys = keys[i:i + 4]
        page_msg = "\n\n".join(f"---{key.capitalize()}---\nStrength: "
                               f"{data[key][0]}\nSpeed: {data[key][1]}"
                               f"\nStealth: {data[key][2]}\nCunning:"
                               f" {data[key][3]}\n" for key in page_keys)
        pages.append(page_msg)
    current_page = 0
    while True:
        msg = pages[current_page]
        buttons = ["Back", "Next", "Console Re-Print", "Exit"]
        reply = eg.buttonbox(msg, "Print cards", buttons)
        if reply == "Next":
            current_page = min(current_page + 1, len(pages) - 1)
        elif reply == "Back":
            current_page = max(current_page - 1, 0)
        elif reply == "Console Re-Print":
            console_print(data)
        elif reply == "Exit":
            break
