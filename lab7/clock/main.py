import pygame 
from datetime import datetime
pygame.init()
disp = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
#current time
curr_time = datetime.now()
curr_sec = curr_time.second
curr_min = curr_time.minute
#images 
clock_image = pygame.transform.scale(pygame.image.load('./mickeyclock.jpeg'), (800, 600))
lithand_image = pygame.image.load('./lithand.png')
lithand_image = pygame.transform.scale(lithand_image, (250, 75))
lithand_rect = lithand_image.get_rect()
lithand_rect.center = (400, 300)
bighand_image = pygame.image.load('./bighand.png')
bighand_image = pygame.transform.scale(bighand_image, (200, 50))
bighand_rect = bighand_image.get_rect()
bighand_rect.center = (400, 300)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    disp.fill(0)
    disp.blit(clock_image, (0, 0))
    
    rot_bighand = pygame.transform.rotate(bighand_image, -1 * (6 * curr_min) - 160)
    rot_bighand_rect = rot_bighand.get_rect()
    rot_bighand_rect.center = bighand_rect.center
    disp.blit(rot_bighand, rot_bighand_rect)
    
    rot_lithand = pygame.transform.rotate(lithand_image, -1 * (6 * curr_sec) + 90)
    rot_lithand_rect =rot_lithand.get_rect()
    rot_lithand_rect.center = lithand_rect.center
    disp.blit(rot_lithand, rot_lithand_rect)
    curr_time = datetime.now()
    curr_sec = curr_time.second
    curr_min = curr_time.minute
    pygame.display.update()
    clock.tick(60)
