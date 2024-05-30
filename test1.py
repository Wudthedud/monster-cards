import easygui

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

def console_print():
    """prints formatted cards to console"""
    for name, stats in data.items():
        msg = "\n"
        width = len(name) + 8
        msg += '-' * (width)
        msg += f'\n|   {name}   |\n'
        msg += '-' * (width)
        msg += '\n'   
        key = ['Strength', 'Speed', 'Stealth', 'Cunning']
        for i, (key, stats) in enumerate(zip(key, stats)):
            stats_msg = f'|{key}: {stats}'
            filler = width - len(stats_msg) - 1
            msg += stats_msg
            msg += ' ' * filler
            msg += '|\n'
        msg += '-' * (width)
        print(msg)
