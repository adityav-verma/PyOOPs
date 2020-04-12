from app.game import Game

if __name__ == '__main__':
    file = open('./input.txt')

    size = int(file.readline())
    g = Game(size)

    snakes = file.readline()
    for index in range(int(snakes)):
        snake = file.readline()
        snake = [int(pos) for pos in snake.split(' ')]
        g.add_snake(snake[0], snake[1])

    ladders = file.readline()
    for index in range(int(ladders)):
        ladder = file.readline()
        ladder = [int(pos) for pos in ladder.split(' ')]
        g.add_ladder(ladder[0], ladder[1])

    players = file.readline()
    for index in range(int(players)):
        player = file.readline()
        g.add_player(player)

    g.start_game()
    g.reset()
