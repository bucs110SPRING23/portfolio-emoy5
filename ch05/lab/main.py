import pygame
pygame.init()

def threenp1(n):
    """
    This is a function that calculates the 3n+1 sequence for a range
    args: number (int)
    return: number of iterations (int)
    """
    count = 0
    while n > 1.0:
        count += 1
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = int(3 * n + 1)
    return count #returns number of iterations
    
def threenp1range(upper_limit):
    """
    This is a function that puts creates a dictionary using (value, number of iterations)
    args: upperlimit of the range (int)
    return: values and number of iterations for that value (dict)
    """
    threenplus1_iters_dict = {}
    
    for i in range(2, upper_limit+1):
        count = threenp1(i)
        threenplus1_iters_dict[i] = count #should be numbers 2-20: iterations of those numbers                  
    return threenplus1_iters_dict #returns the dictionary

def graph_coordinates(upper_limit):
    """
    This is a function that graphs values and number of iterations for those values
    args: upperlimit of the range (int)
    return: a graph?
    """
    threenplus1_iters_dict = threenp1range(upper_limit)
    coordinates = threenplus1_iters_dict.items()
    
    screen = pygame.display.set_mode()
    screen.fill("black")
    for k, v in coordinates.items():
        
    pygame.draw.lines(screen, "white", False, list(coordinates), 1)
    flipped = pygame.transform.flip(screen, False, True)
    width, height = flipped.get_size()
    transformed = pygame.transform.scale(flipped, (width * 5, height * 5))
    
    screen.blit(transformed, (0, 0))
    pygame.display.flip()
    pygame.time.wait(500)

    max_so_far = [0,0]
    for key, value in threenplus1_iters_dict.items():
        if value >= max_so_far[1]:
            max_so_far[1] = value
            max_so_far[0] = key
        else:
            max_so_far = max_so_far
         
    font = pygame.font.Font(None, 30)
    max_display = font.render("highest number of iterations for " + str(max_so_far[0]) + " is " + str(max_so_far[1]), True, "red")
    screen.blit(max_display, (width/2, height/2))
    pygame.display.flip()
    pygame.time.wait(1000)


def main():
    pygame.init()
    upper_limit = 100
    print(threenp1range(upper_limit))
    graph_coordinates(upper_limit)
main()