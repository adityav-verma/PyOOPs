from app.game import Game

if __name__ == '__main__':
    g = Game()
    g.add_player('Aditya')
    g.add_player('Sneha')
    g.add_snake(10, 5)
    g.add_snake(95, 30)
    g.add_ladder(4, 12)
    g.start_game()