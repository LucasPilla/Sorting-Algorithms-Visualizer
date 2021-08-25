themesDict = {
            'default': {
                'grey': (100, 100, 100),
                'green': (125, 240, 125),
                'white': (250, 250, 250),
                'red': (255, 50, 50),
                'black': (0, 0, 0),
                'blue' : (50, 50, 255)
                },
            'monokai': {
                'grey': (10, 10, 10),
                'green': (180, 210, 115),
                'white': (46, 46, 46),
                'red': (232, 125, 62),
                'black': (214, 214, 214),
                'blue' : (180, 153, 187)
                },
            'darkmatter': {
                'grey':  (100, 100, 100),
                'green': (113, 172, 223),
                'white': (60, 117, 188),
                'red': (255, 50, 50),
                'black': (19, 25, 30),
                'blue' : (105, 114, 124)
                }
            }

def getTheme(theme):
    return themesDict.get(theme)