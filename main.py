#!/usr/bin/env python
#__*__ coding: utf-8 __*__

import pygame,sys,time,random
from pygame.locals import *
import Astar

redColour = pygame.Color(255,0,0)
blackColour = pygame.Color(0,0,0)
whiteColour = pygame.Color(255,255,255)
greenColour = pygame.Color(0,255,0)
greyColour = pygame.Color(200,200,200)

def main():
	pygame.init()
	playSurface = pygame.display.set_mode((640,480))
	fpsClock = pygame.time.Clock()
	pygame.display.set_caption('Snake HEGSNS')

	block_width = 20
	tabu_table = [[10, idx] for idx in range(0,15)] + [[20, idx] for idx in range(10,24)]
	snakePosition = [2, 2]
	snakeSegments = [[2,2],[1,2],[0,2]]
	raspberryPosition = [31,22]

	a_starobj = Astar.Astar(tabu_table + snakeSegments)
	while True:
		# A_star search
		a_starobj.__init__(tabu_table + snakeSegments)
		a_starobj.A_star_search(snakePosition, raspberryPosition)
		route = a_starobj.recall_route(snakePosition, raspberryPosition)
		a_starobj.clear_history()

		for loc_idx in range(1, len(route)):
			snakePosition = [x for x in route[loc_idx]]
			# 增加蛇的长度
			snakeSegments.insert(0,list(snakePosition))
			if loc_idx < len(route) - 1:
				snakeSegments.pop()
			# 刷新pygame显示层
			playSurface.fill(whiteColour)
			for position in route[loc_idx:]:
				pygame.draw.rect(playSurface, greyColour, Rect(position[0] * block_width, position[1] * block_width, block_width, block_width))
			for position in snakeSegments:
				pygame.draw.rect(playSurface,greenColour,Rect(position[0]*block_width,position[1]*block_width,block_width,block_width))
			for position in tabu_table:
				pygame.draw.rect(playSurface, blackColour, Rect(position[0]*block_width, position[1]*block_width, block_width, block_width))
			pygame.draw.rect(playSurface,redColour,Rect(raspberryPosition[0]*block_width, raspberryPosition[1]*block_width,block_width,block_width))
			pygame.display.flip()
			fpsClock.tick(5)

		while True:
			x = random.randrange(1, 32)
			y = random.randrange(1, 24)
			tabu_table_tmp = tabu_table + snakeSegments
			if [x, y] not in tabu_table_tmp:
				break
		raspberryPosition = [int(x), int(y)]

		for event in pygame.event.get():
			if event.type == QUIT:
				exit()

	return


if __name__ == "__main__":
	main()