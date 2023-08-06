

```python 
width, height = config["resolution"]["width"], config["resolution"]["height"]
clock = pygame.time.Clock()
win = pygame.display.set_mode((width, height))
screen = win
display = win
pygame.display.set_caption("Game Engine", config['version'])

```

- width: The width of the game window, extracted from the configuration file.
- height: The height of the game window, extracted from the configuration file.
- clock: A Pygame Clock object to manage the frame rate.
- win: The game window surface.
- screen: An alias for the game window surface (just another reference to win).
- display: Another alias for the game window surface (just another reference to win).
- pygame.display.set_caption: Sets the window caption to "Game Engine" with the version from the configuration file.
## Static Variables

```python 
black = (0, 0, 0)
white = (255, 255, 255)
grey = (100, 100, 100)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
sky_blue = (135, 206, 250)
light_blue = (155, 155, 255)

```
These variables represent RGB color codes.

## Fonts and Letters

```python 
fontSize = 25
font = pygame.font.Font(None, fontSize)
Letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

```

- fontSize: The font size for rendering text.
- font: A Pygame font object created with a default font and the specified font size.
- Letters: A list containing uppercase English letters.
## Images Loading

```python 
assetList = [["box"]]
assetList2 = [["floor"],["grass"],["hole"],["dirt"]]
allAssets = []
userAssets = []

```

These variables store the names of different assets to be loaded later.

## Loading All Assets

```python 
for i in range(len(assetList)):
    allAssets.append(pygame.image.load(
        f'{path}//data//assets//programImages//{assetList[i][0]}.png'))

```
This loop loads images from the `data/assets/programImages` directory and appends them to the allAssets list.

```python
for i in range(len(assetList2)):
    userAssets.append(pygame.image.load(
        f'{path}//data//assets//userPacks//{assetList2[i][0]}.png'))

```

This loop loads images from the `data/assets/userPacks` directory and appends them to the userAssets list.