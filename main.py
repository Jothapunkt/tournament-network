from gamesim import GameSim
from network import Network
from player import RemotePlayer

game = GameSim()
r_player = RemotePlayer()
r_player.x = 200

game.players.append(r_player)

while(game.has_survivors):
	game.tick()


print("0,0")
print(game.collides_at_position(0,0))

print("10,25")
print(game.collides_at_position(10,25))

print("237,140")
print(game.collides_at_position(237,140))

print("1000,1000") #true
print(game.collides_at_position(1000,1000))

print("400,520") #false
print(game.collides_at_position(400,520))

print("300,520") #true
print(game.collides_at_position(300,520))

