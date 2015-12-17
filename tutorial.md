# A Basic PyGame Tutorial

### What is pygame?
PyGame is a python wrapper for the SDL library. SDL is a cross-platform library for accessing computer multimedia hardware components (sound, video, input, etc). SDL is an extremely powerful tool for building all kinds of things, but it's written in C, and C is hard, so we use PyGame.

### Who this tutorial is for.
I'll assume a basic understanding of python syntax, file structure, and OOP but nothing else. I'll go over basic game logic, drawing to the screen, collision detection, and loading outside files into our game.

### Installing PyGame
Go to the pygame download page (http://www.pygame.org/download.shtml), and find the proper binary package for your operating system and version of python. I'm using Python3 but if you are on 2.7 everything will still work the same.

## Importing and initializing pygame.
As with all python programs we begin by importing the modules we want to use. In this case we will be importing PyGame itself and pygame.locals (which we will use later for some of the constants). The last line initializes all the pygame modules, it must be called before you do anything else with pygame. Create a new .py file and input the following code:

```python
import pygame
from pygame.locals import *

pygame.init()
```

## Creating a screen object.
First things first: we need something to draw on, so we will create a "screen" which will be our overall canvas. In order to create a screen to display on we call the set_mode method of pygame.display. We pass set_mode a tuple with the width and height of the window we want. We want our screen to be 800x600 in this case. Here is what our code should look like now:

```python
import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800,600))
```

If you run this now you'll see our window pop up briefly and then immediately disappear as the program exits. Not very impressive is it? In the next section we will introduce our main game loop to ensure that our program only exits when we give it the correct input.

## The main game loop.
The main game loop is where all the action happens. It runs continuously during gameplay, updating the game state, rendering the screen, and collecting input. When we create our loop we need to make sure that we have a way to get out of the loop and exit the application. To that end we will introduce some basic user input at the same time. All user input (and some other events we will get into later) go into the pygame event queue, you can access the queue by calling 'pygame.event.get()'. Get will return a list of all the events in the queue, which we will loop through and respond according to the type of event. For now all we care about are KEYDOWN and QUIT events.

```python
# Variable to keep our main loop running
running = True

# Our main loop!
while running:
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event, KEYDOWN is a constant defined in pygame.locals, which we imported earlier
        if event.type == KEYDOWN:
            # If the Esc key has been pressed set running to false to exit the main loop
            if event.key == K_ESCAPE:
                running = False
        # Check for QUIT event, if QUIT, set running to false
        elif event.type == QUIT:
            running = False
```

Add these lines to our previous code and run it. You should see an empty window. It wont go away until you press the esc key or trigger a QUIT event by closing the window.


## Rects and Surfaces
Surfaces and Rects are basic building blocks in pygame. Think of surfaces as a blank sheet of paper that you can draw whatever you want onto. Our screen object is also a Surface. They can hold images as well. Rects are a representation of a rectangular area that your surface encompasses.

Let's create a basic surface that's 50 pixels by 50 pixels, then let's fill in the surface with a color. We'll use white because the default window background is black and we want it to be nice and visible. We will then call the 'get_rect' method on our surface to get the rectagular area and x,y coordinates of our surface.

```python
# Create the surface and pass in a tuple with it's length and width
surf = pygame.Surface((50,50))
# Give the surface a color to differentiate it from the background
surf.fill((255,255,255))
rect = surf.get_rect()
```

## Blit and Flip
Just creating our surface isn't actually enough to see it on the screen. To do that we need to blit the surface onto another surface. Blit is just a technical way to say draw. You can only blit from one surface object to another, but remember, our screen is just another surface object. Here's how we'll draw our 'surf' to the screen:

```python
# This line says "Draw surf onto screen at coordinates x:400, y:300"
screen.blit(surf, (400,300))
pygame.display.flip()
```

Blit takes two arguments: the surface to draw and the location to draw it at on the source surface. Here we use the exact center of the screen, but when you run the code you'll notice our surf does not end up centered on the screen. This is because blit will draw surf starting at the top left position.
Notice the call to pygame.display.flip() after our blit. Flip will update the entire screen with everything that has been drawn since the last flip. Without a call to flip, nothing will show. Now let's see what everything looks like together:

## Sprites
What are sprites? In programming terms a sprite is a 2d representation of something on the screen. Essentially, a sprite is a picture. Pygame provides a basic class called Sprite, which is meant to be extended and used to hold one or several graphical representations of an object that you want to display on the screen. We will extend the sprite class so that we can use it's built in methods. We'll call this new object 'Player', Player will extend Sprite, and have only two properties for now: surf and rect. We will also give surf a color (white in this case) just like the previous surface example except that now the surface belongs to the player.

```python
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75,25))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()
```

Let's put it all together!

```python
# import the pygame module
import pygame

# import pygame.locals for easier access to key coordinates
from pygame.locals import *

# Define our player object and call super to give it all the properties and methods of pygame.sprite.Sprite
# The surface we draw on the screen is now a property of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75,25))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()

# initialize pygame
pygame.init()

# create the screen object
# here we pass it a size of 800x600
screen = pygame.display.set_mode((800,600))

# instantiate our player, right now he's just a rectangle
player = Player()


# Variable to keep our main loop running
running = True

# Our main loop!
while running:
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event, KEYDOWN is a constant defined in pygame.locals, which we imported earlier
        if event.type == KEYDOWN:
            # If the Esc key has been pressed set running to false to exit the main loop
            if event.key == K_ESCAPE:
                running = False
        # Check for QUIT event, if QUIT, set running to false
        elif event.type == QUIT:
            running = False

    # Draw the player to the screen
    screen.blit(player.surf, (400,300))
    # Update the display
    pygame.display.flip()
```

Go ahead and run this code. You'll see a white rectangle at roughly the middle of the screen. What do you think would happen if you changed 'screen.blit(player.surf,(400,300))' to 'screen.blit(player.surf, player.rect)'? Now try printing player.rect to the console. The first two attributes of the rect are x,y coordinates of the top left corner of the rect. When you pass blit a rect, it will use those coordinates to draw the surface. We will use this later to make our player move!


## User Input
Here is where the fun starts. Let's make our player controllable. We discussed earlier getting our keydown event with pygame.event.get(), which pulls the latest event off the top of the event stack. Pygame has another event method called pygame.event.get_pressed. Get_pressed returns a dictionary with all the keydown events in the queue. We will put this in our main loop so we get the keys every frame.

```python
pressed_keys = pygame.event.get_pressed()
```

What we will do now is write a method that will take that dictionary and define the behavior of the sprite based off the keys that are pressed. Here's what it might look like:

```python
def update(self, pressed_keys):
    if pressed_keys[K_UP]:
        self.rect.move_ip(0,-5)
    if pressed_keys[K_DOWN]:
        self.rect.move_ip(0,5)
    if pressed_keys[K_LEFT]:
        self.rect.move_ip(-5,0)
    if pressed_keys[K_RIGHT]:
        self.rect.move_ip(5, 0)
```
K_UP, K_DOWN, K_LEFT, and K_RIGHT correspond to the arrow keys on the keyboard. So we check that key, and if it's set to true we move our rect in the relevant direction. Rects have two built-in methods for moving, here we use 'move in place', because we want to move the existing rect without making a copy. (Maybe add more about destructive methods?).

Add the above method to our Player class, and put the get_pressed call in the main loop. Our code should now look like this:

```python
import pygame

from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75,25))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5,0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

pygame.init()

screen = pygame.display.set_mode((800,600))

player = Player()


running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    pressed_keys = pygame.event.get_pressed()

    player.update(pressed_keys)

    screen.blit(player.surf, (400,300))
    pygame.display.flip()
```

Now you should be able to move your rectangle around the screen with the arrow keys. You may notice though, that you can move off the screen, which is something we probably don't want. So lets add a bit of logic to the update method that tests if the rectangle's coordinates have moved beyond our 800 by 600 boundary and if so, move it back to the edge.

```python
def update(self, pressed_keys):
    if pressed_keys[K_UP]:
        self.rect.move_ip(0,-5)
    if pressed_keys[K_DOWN]:
        self.rect.move_ip(0,5)
    if pressed_keys[K_LEFT]:
        self.rect.move_ip(-5,0)
    if pressed_keys[K_RIGHT]:
        self.rect.move_ip(5, 0)

    #Keep player on the screen
    if self.rect.left < 0:
        self.rect.left = 0
    elif self.rect.right > 800:
        self.rect.right = 800
    if self.rect.top <= 0:
        self.rect.top = 0
    elif self.rect.bottom >= 600:
        self.rect.bottom = 600
```

Here instead of using a move method we just alter the corresponding coordinates for top, bottom, left, or right.

Now lets add some enemies!

First lets create a new sprite class called 'Enemy'. We will follow the same formula we used for the player class.

```python
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20,10))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(center=(820, random.randint(0,600)))
        self.speed = random.randint(5,20)

    def update(self):
        self.rect.move_ip(-self.speed,0)
        if self.rect.right < 0:
            self.kill()
```

There are a couple differences here that we should talk about. First off when we call get_rect on our surface we are setting the center property x coordinate to 820, and our y coordinate to a random number generated by random.randint.

Random is a python library that we will import at the beginning of our file in the complete code (import random). Why the random number? Simple: we want our incoming enemies to start past the right side of the screen (820), at a random place (0-600). We also use random to set a speed property for the enemies. This way we will have some enemies that are fast, and some that are slow.

Our update method for the enemies takes no arguments (we don't care about input for enemies) and simply moves the enemy toward the left side of the screen at a rate of speed. And the last if statement in the update method test to see if the enemy has gone past the left side of the screen with the right side of it's rectangle (so that they don't just disappear as soon as they touch the side of the screen). When they pass the side of the screen we call sprites built in kill method to delete them from their sprite group thereby preventing them from being rendered. Kill does not release the memory taken by the enemy, and relies on you no longer having a reference to it so the python garbage collector will take care of it.

## Groups!
Another super useful object that pygame provides are sprite groups. They are exactly what they sound like: groups of sprites. So why do we use sprite groups instead of an array for example? Sprite groups have several methods built into them that will help us later with collisions and updating. Lets make a group right now that will hold all the sprites in our game. After we create it we will add the player to the group since that's our only sprite so far. We can create another group for enemies as well. When we call a sprite's kill method, the sprite will be removed from all groups that it is a part of.

```python
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
```

Now that we have this all_sprites group, lets change how we are rendering our objects so that we render all objects in this group.

```python
for entity in all_sprites:
    screen.blit(entity.surf, entity.rect)
```

Now anything we put into all_sprites will be rendered.

## Custom events
Now we have a sprite group for our enemies but no actual enemies. So how do we get some enemies on the screen? We could just create a bunch of them at the beginning but then our game wouldn't last more than a few seconds. So we will create a custom event that will fire off every few seconds and trigger the creation of a new enemy. We listen for this event in the same way that we listed for key presses or quit events. Creating a custom event is as easy as naming it:

```python
ADDENEMY = pygame.USEREVENT+1
```

That easy! Now we have an event called ADDENEMY that we can listen for in our main loop. The only gotcha to keep in mind here is that we need our custom event to have a unique value that is greater than the value of USEREVENT. That's why we set our new event to equal USEREVENT+1. One small note for those that are curious about about these events. They are at their core just integer constants. USEREVENT has a numeric value and any custom event we create needs to be an integer value that is greater than USEREVENT (because all the values less than USEREVENT are already taken by builtins).

Now that we've defined our event we need to insert it into the event queue. Since we need to keep creating them over the course of the game we will set a timer. To do this we use pygame's time object.

```python
pygame.time.set_timer(ADDENEMY, 250)
```

This tells pygame to fire our ADDENEMY event every 250 milliseconds, or every quarter second. This goes outside of our game loop, but will still fire throughout the entire game. Now let's add some code to listen for our event. Keep in mind set_timer is exclusively used for inserting events into the pygame event queue - it doesn't do anything else.

```python
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif(event.type == ADDENEMY):
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
```

Now we are listening for our ADDENEMY event, and when it fires, we create a new instance of the Enemy class. Then we add that instance to the enemies sprite group (which we will later use to test for collision) and to the all_sprites group (so that it gets rendered along with everything else).

## Collision
This is why you will love pygame! Writing collision code is hard, but pygame has a LOT of collision detection methods some of which you can find [here](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.collide_rect). For this tutorial we will be using [spritecollideany](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.spritecollideany). Spritecollideany takes a sprite object and a sprite group and tests if the sprite object intersects with any of the sprites in the sprite group. So we will take our player sprite and our enemies sprite group and test if our player has been hit by an enemy. Here's what it looks like in code:

```python
if pygame.sprite.spritecollideany(player, enemies):
    player.kill()
```

We test if our player sprite object collides with any sprites in the enemies sprite group, and if it does, we call the kill method on the player sprite. Because we are only rendering sprites in the all_sprites group, and the kill method removes a sprite from all its groups, our player will no longer be rendered, thus 'killing' it. Lets put it all together.

```python
# import the pygame module
import pygame

# import random for random numbers!
import random

# import pygame.locals for easier access to key coordinates
from pygame.locals import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75,25))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5,0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        #Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 600:
            self.rect.bottom = 600

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20,10))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(center=(random.randint(820,900), random.randint(0,600)))
        self.speed = random.randint(5,20)

    def update(self):
        self.rect.move_ip(-self.speed,0)
        if self.rect.right < 0:
            self.kill()



# initialize pygame
pygame.init()

# create the screen object
# here we pass it a size of 800x600
screen = pygame.display.set_mode((800,600))

# Create a custom event for adding a new enemy.
ADDENEMY = pygame.USEREVENT+1
pygame.time.set_timer(ADDENEMY, 250)

# create our 'player', right now he's just a rectangle
player = Player()

background = pygame.Surface(screen.get_size())
background.fill((0,0,0))
# player.surf.fill((255,255,255))

enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif(event.type == ADDENEMY):
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
    screen.blit(background, (0,0))
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    enemies.update()
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()

    pygame.display.flip()
```

## Next Steps
Now we have a game, but kind of an ugly game. So next we will replace all the boring white rectangles with cool images that will make the game feel like an actual game.

## Let's Add Some Images
So in the previous code examples we used a surface object filled with a color to represent everything in our game. While this is a good way to get a handle on what a surface is and how they work, it makes an ugly game. So we're going to add some pictures for the enemies and the player. I like to draw my own images so I made a little jet for the player, and some missiles for the enemies. You're welcome to use my art, draw your own, or download some [free game art assets](http://www.gameart2d.com/) to use.

## Altering Our Object Constructors
Our current player constructor looks like this:

```python
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75,25))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()
```

Our new constructor will look like this:

```python
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load('jet.png').convert()
        self.image.set_colorkey((255,255,255), RLEACCEL)
        self.rect = self.image.get_rect()
```

We want to replace our surface object with an image. We will use pygame.image.load by passing it a string of a path to a file. Load will actually return a surface object. We then call convert on that surface object to create a copy that will draw more quickly on the screen.

Next we call the set_colorkey method on our image. Set_colorkey sets the color in the image that pygame will render as transparent. In this case I chose white, because that's the background of my jet image. RLEACCEL is a optional parameter that will help pygame render faster on non-accelerated displays.

Lastly, we get our rect object in the same way as before, by calling get_rect on our image. Remember, image is still a surface object, it just now has a picture painted on it.

Let's do the same thing with the enemy constructor:

```python
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.image.load('missile.png').convert()
        self.image.set_colorkey((255,255,255), RLEACCEL)
        self.rect = self.image.get_rect(center=(random.randint(820,900), random.randint(0,600)))
        self.speed = random.randint(5,20)
```
