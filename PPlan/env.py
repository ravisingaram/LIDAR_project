import math
import pygame
class buildEnvironment:
    def __init__(self, MapDimensions):
        pygame.init()  # intialize the pygame
        self.pointCloud=[]  # Declare a list to store our point cloud map 2d points in 2d space
        self.externalMap=pygame.image.load('floor_image.png')  # upload our floor plan by calling image load function
        self.maph, self.mapw = MapDimensions  # introducing map dimensions height and width
        self.MapWindowName = 'RRT path planning'
        pygame.display.set_caption(self.MapWindowName)
        self.map = pygame.display.set_mode((self.mapw, self.maph))  # specifying the width and height to the actual window(main map was empty)
        self.map.blit(self.externalMap, (0, 0))

        # Giving the Colours to the map
        self.black = (0, 0, 0)
        self.grey = (70, 70, 70)
        self.blue = (0, 0, 255)
        self.green = (0, 255, 0)
        self.red = (255, 0, 0)
        self.white = (255, 255, 255)

    def AD2pos(selfself, distance,angle,robotposition):
        x = distance * math.cos(angle)+robotposition[0]
        y = -distance * math.sin(angle) +robotposition[0]
        return (int(x),int(y))

    def dataStorage(self,data):
        print(len(self.pointCloud))
        for element in data:
            point=self.AD2pos(element[0],element[1],element[2])
            if point not in self.pointCloud:
                self.pointCloud.append(point)

    def show_sensorData(self):
        self.infomap=self.map.copy()
        for point in self.pointCloud:
            self.infomap.set_at((int(point[0]),int(point[1])),(255,0,0))


