## Intro
1. Outline of tutorial.
1. What is pygame.
1. Installing pygame.

## Creating and Drawing to the screen
1. Creating the screen
```
// initialize pygame
pygame.init()
// create screen
screen = pygame.display.set_mode(size)
```

1. blit()
```
// draws an entity to the screen at x,y coordinates
screen.blit(entity, (x,y))
```

1. flip()
 - You won't see the objects you've 'blitted' until you update the screen using flip.
```
//updates the screen
pygame.display.flip()
```

## Surfaces, Sprites, and Rects
### How they all fit together
1. Rect
```
// Used to represent rectangles
pygame.Rect(left, top, width, height)
```

1. Surfaces
```
// Surfaces in pygame are use to represent an image
// Loading an image into the game will return you a Surface object.
surface = pygame.image.load('path to image')
```

1. Sprites
  -Pygame has a built in base class to represent 'sprites'
  -You can think of it as a related group of Rects and Surfaces
  -Pygame sprites have several built in methods to use or overwrite.
    -The most useful ones here

## User Input
1. Another thing that pygame makes simple.

## Collision
1. PyGame makes detecting collisions ridiculously simple
1. Both the sprite class and the rect class have several methods for detecting collisions, we will use the most basic: colliderect.
