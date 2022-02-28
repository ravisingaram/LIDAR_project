from PPlan import env,sensors
#introducing the sensors and env files to main program
import pygame

environment = env.buildEnvironment((600, 1200))
#building environments using the arguments
environment.originalMap = environment.map.copy()
laser = sensors.LaserSensor(200,environment.originalMap,uncertainity=(0.5,0.01))
environment.map.fill((0,0,0))
environment.infomap = environment.map.copy()
running = True #boolean value
while running:  #check for events
    sensorON=False
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #if event type is related to red exit button
            running = False  #it has to be terminated
        if pygame.mouse.get_focused():
            sensorON=True
        elif not pygame.mouse.get_focused():
            sensorON=False
    if sensorON:
        position = pygame.mouse.get_pos()
        laser.position=position
        sensor_data = laser.sense_obstacles()
        environment.dataStorage(sensor_data)
        environment.show_sensorData()
    environment.map.blit(environment.infomap,(0,0))
    pygame.display.update()









