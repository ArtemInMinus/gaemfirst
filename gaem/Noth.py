import pgzrun, random, pygame, time

HEIGHT = 650
WIDTH = 1000

FPS = 60

background = Actor("background", (WIDTH/2, HEIGHT/2))
player = Actor("player", (WIDTH/2, HEIGHT/2))
dummy = Actor("player", (player.x - 400, player.y))
dummy1 = Actor("player", (2130, 1965))
sound1 = pygame.mixer.Sound('punch.mp3')
preshift = 0
punch = 0

old_x = 0
old_y = 0
debug_pos = 0

def draw():
    global pressshift
    background.draw()
    player.draw()
    dummy.draw()
    dummy1.draw()
    if preshift == 1:
        screen.draw.text("Ударь - shift", center=(player.x, player.y - 70), color = 'black', fontsize = 35)
    if punch == 1:
        screen.draw.text("-20", center=(dummy.x, dummy.y - 70), color = 'red', fontsize = 25)
    screen.draw.text(str(debug_pos), center=(WIDTH - 100, HEIGHT - 50), color = 'white', fontsize = 35)
def camera(a):
    if a == "right":
        background.x -= 5
        #dummy.x -= 1
    if a == "left":
        background.x += 5
        #dummy.x -= 1
    if a == "up":
        background.y += 5
        #dummy.x -= 1
    if a == "down":
        background.y -= 5
        #dummy.x -= 1
def update(dt):
    global old_x, old_y, debug_pos
    if keyboard.right:
        camera("right")
    elif keyboard.left:
        camera("left")
    if keyboard.up:
        camera("up")
    elif keyboard.down:
        camera("down")
        
    dummy.y = background.y
    dummy.x = background.x - 400
    

def on_key_down(key):
    global preshift, punch, debug_pos
    if keyboard.q:
        debug_pos = (background.x - player.x), (background.y - player.y)
    preshift = 0
    punch = 0
    dummy.image = "player"
    if player.colliderect(dummy):
        dummy.image = "dummybeat"
        preshift = 1
        if keyboard.rshift:
            sound1.play()
            punch = 1
pgzrun.go()