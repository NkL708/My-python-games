
def create_2d_arr(weight, height):
    return [[0 for x in range(weight)] for y in range(height)];


class Board:
    objects = create_2d_arr(weight, height)
    
    
    def update(time_interval):
        snake.move()
        time.sleep(time_interval)
