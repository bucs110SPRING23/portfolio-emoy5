import pygame

def threenp1(n):
        count = 0
        while n > 1.0:
            count += 1
            if n % 2 == 0:
                n = int(n / 2)
            else:
                n = int(3 * n + 1)
        return count #returns number of iterations
    
def threenp1range(upper_limit):
    threenplus1_iters_dict = {}
    for i in range(2, upper_limit+1):
        count = threenp1(i)
        threenplus1_iters_dict[i] = count #should be numbers 2-20: iterations of those numbers                  
    return threenplus1_iters_dict #returns the dictionary

def graph_coordinates(threenplus1_iters_dict):
    pygame.draw.lines()
    
    font = pygame.font.Font(None, 30)
    msg = font.render(msg, True, "black")
    display.blit(msg, (10, 10))

def main():
    pygame.init()
    upper_limit = 20
    threenp1range(upper_limit)
    print(threenp1range(upper_limit))
    #graph_coordinates(range)
main()