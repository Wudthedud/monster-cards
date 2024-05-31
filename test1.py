import easygui as eg

data = {'stoneling': [7, 1, 25, 15],
        'vexscream': [1, 6, 21, 19],
        'dawnmirage': [5, 15, 18, 22],
        'blazegolem': [15, 20, 23, 6],
        'websnake': [7, 15, 10, 5],
        'moldvine': [21, 18, 14, 5],
        'vortexwing': [19, 13, 19, 2],
        'rotthing': [16, 7, 4, 12],
        'froststep': [14, 14, 17, 4],
        'wispgoul': [17, 19, 3, 2]}

keys = list(data.keys())
pages = []
for i in range(0, len(keys), 4):
    page_keys = keys[i:i+4]
    page_msg = "\n\n".join(f"---{key.capitalize()}---\nStrength: {data[key][0]}\n"
                           f"Speed: {data[key][1]}\nStealth: {data[key][2]}\n"
                           f"Cunning: {data[key][3]}\n" for key in page_keys)
    pages.append(page_msg)

current_page = 0

while True:
    msg = pages[current_page]
    buttons = ["Next", "Back", "Exit"]
    reply = eg.buttonbox(msg, "Data", buttons)

    if reply == "Next":
        current_page = min(current_page + 1, len(pages) - 1)
    elif reply == "Back":
        current_page = max(current_page - 1, 0)
    elif reply == "Exit":
        break