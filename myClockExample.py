import pygame


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()

size = [700, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
done = False
clock = pygame.time.Clock()

font = pygame.font.Font(None, 25)

frame_count = 0
frame_rate = 60
start_time = 10


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(WHITE)
    total_seconds = frame_count // frame_rate
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)
    text = font.render(output_string, True, BLACK)
    screen.blit(text, [250, 250])
    total_seconds = start_time - (frame_count // frame_rate)
    if total_seconds < 0:
        total_seconds = 0
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    output_string = "Time left: {0:02}:{1:02}".format(minutes, seconds)
    text = font.render(output_string, True, BLACK)
    screen.blit(text, [250, 280])
    frame_count += 1
    clock.tick(frame_rate)
    pygame.display.flip()

pygame.quit()
