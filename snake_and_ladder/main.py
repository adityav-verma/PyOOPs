from app.game import Game

if __name__ == '__main__':
    g = Game()
    g.add_player('Player1')
    g.add_player('Player2')
    g.add_player('Player3')
    g.add_player('Player4')
    g.add_snake(10, 5)
    g.add_snake(95, 30)
    g.add_snake(30, 6)
    g.add_ladder(4, 12)
    g.start_game()
    g.reset()
