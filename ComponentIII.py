#Game Cell
#The Diamond
#Kanvir Singh, Gurpreet Singh, Rene Juarez San Migu
#Knight has to go and retrive the King's diamond from the devil.

from gamelib import*#import game library

#objects and initial settings
game = Game (800,600,"The Diamond")
bk = Image("castle.png",game)
bk.resizeTo(game.width, game.height)
knight = Image("knight.png",game)
King_Arthur = Image("king_arthur.png" ,game)


#Level 1 - game loop

while not game.over:
    game.processInput()
    #game.scrollBackground("left",2)
    bk.draw()
    knight.draw()
    game.update(30)

game.over = False
#Level 2 - game loop
while not game.over:
    game.processInput()
    #game.scrollBackground("left",2)
    bk.draw()
    knight.draw()
    game.update(30)

game.quit()

