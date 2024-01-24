
# this version will consist of the timed version

import pygame, sys, random
import os 
from pygame.math import Vector2


pygame.init()

font_folder = os.path.join(os.path.dirname(__file__), 'fonts')
font_path = os.path.join(font_folder, 'Pixeltype.ttf')
pygame.font.init()


cell_size = 13
cell_number = 60
SNEKE_COLOR = (132,113,79)
SNAKE_COLOR = (49,35,30)

screen = pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size))
length = cell_number*cell_size
clock = pygame.time.Clock()

white = (255, 251, 254)
purple = (124, 119, 185)
green = (176, 254, 118)
viridian = (71, 137, 120)
green_grey = (46, 92, 107)
global start_time
start_time = 0



def main_game():

	def returnTime():
		time_font = pygame.font.Font( 'Fonts/Pixeltype.ttf' , 60)
		current_time = int(pygame.time.get_ticks()/1000) - start_time
		time_surf = time_font.render(f'Score: {current_time}', False, green)
		time_rect = time_surf.get_rect(center = (length/2,length/2 ))
		screen.blit(time_surf,time_rect)
		if main_game.running == False:
			current_time = start_time


	class SNAKE:
		def __init__(self):
			self.body = [Vector2(5,10),Vector2(4,10),Vector2(3 ,10)]
			self.direction = Vector2(1,0)
			self.new_block = False
		def draw_snake(self):
			
			
			for block in self.body:
				x_pos = int(block.x*cell_size)
				y_pos = int(block.y*cell_size)
				block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
				pygame.draw.rect(screen,green, block_rect)
				#snake_block = pygame.transform.scale(pygame.image.load('images/snake_body.png'),(cell_size,cell_size))
				#snake_block_rect = snake_block.get_rect()
				#snake_block_rect.center = (x_pos,y_pos)
				#screen.blit(snake_block, snake_block_rect)\
			head_rect = pygame.Rect(int(self.body[0].x*cell_size),int(self.body[0].y*cell_size),cell_size,cell_size)
			pygame.draw.rect(screen,white, head_rect)

			

		def move_snake(self):
			if self.new_block == True:
				body_copy = self.body[:]
				body_copy.insert(0,body_copy[0] + self.direction)
				self.body = body_copy[:] 
				self.new_block = False
			else:
				body_copy = self.body[:-1]
				body_copy.insert(0,body_copy[0] + self.direction)
				self.body = body_copy[:] 
		def add_block(self):
			self.new_block = True
			print("newblock added to snake player")


	class SNEKE:
		def __init__(self):
			self.body = [Vector2(5,15),Vector2(4,15),Vector2(3 ,15)]
			self.direction = Vector2(1,0)
			self.new_block = False

		def draw_sneke(self):
			for block in self.body:
				x_pos = int(block.x*cell_size)
				y_pos = int(block.y*cell_size)
				block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
				pygame.draw.rect(screen,white, block_rect)
				#sneke_block_rect = sneke_block.get_rect()
				#sneke_block_rect.center = (x_pos,y_pos)
				#screen.blit(sneke_block, sneke_block_rect)
		def move_sneke(self):
			if self.new_block == True:
				body_copy = self.body[:]
				body_copy.insert(0,body_copy[0] + self.direction)
				self.body = body_copy[:] 
				self.new_block = False
			else:
				body_copy = self.body[:-1]
				body_copy.insert(0,body_copy[0] + self.direction)
				self.body = body_copy[:] 
		def add_block(self):
			self.new_block = True
			print("new block added to the sneke player")



	class FRUIT:
		def __init__(self):
			 self.randomize()

		def draw_fruit(self):
			fruit = pygame.transform.scale(pygame.image.load('images/apple.png'),(cell_size,cell_size))
			fruit_rect = fruit.get_rect()
			fruit_rect.center = (cell_size*self.x, cell_size*self.y)
			screen.blit(fruit, fruit_rect)
		def randomize(self):
			self.x = random.randint(0,cell_number-1)
			self.y = random.randint(0, cell_number-1)
			self.pos = Vector2(self.x, self.y)
	class SCOREBOARD:
		def __init__(self,score1 ,score2 ):
			self.score1 = score1
			self.score2 = score2

			font = pygame.font.Font('Fonts/Pixeltype.ttf', 32)
			self.score1_text = font.render(f'snake: {self.score1}', True, SNAKE_COLOR)
			self.score1_Rect = self.score1_text.get_rect()
			self.score1_Rect.center = ( cell_size*cell_number// 5,cell_size*cell_number// 20 )

			self.score2_text = font.render(f'sneke: {self.score2}', True, SNEKE_COLOR)
			self.score2_Rect = self.score2_text.get_rect()
			self.score2_Rect.center = ( cell_size*cell_number// 1.3,cell_size*cell_number// 20)
		def draw_elements(self):
			screen.blit(self.score1_text, self.score1_Rect)
			screen.blit(self.score2_text, self.score2_Rect)		


	class MAIN:
			def __init__(self):# you have to chuck in the difficulty settings and time duration settings in here too in later stages
				self.snake = SNAKE()
				self.fruit = FRUIT()
				self.sneke = SNEKE()
				self.running = True # this is to determine whether or not the game state is active/running
				self.snake_winner = False
				self.sneke_winner = False
				self.snake_score = 0
				self.sneke_score = 0
			def update(self):
				self.snake.move_snake()
				self.sneke.move_sneke()
				self.check_collision()
				self.check_fail()
			def draw_elements(self):
				self.fruit.draw_fruit()
				self.snake.draw_snake()
				self.sneke.draw_sneke()



			def check_collision(self):
				if self.fruit.pos == self.snake.body[0]:
					# add another block to the snake
					self.snake.add_block()
					# change fruit position
					self.fruit.randomize()
					#add 1 to the snake score
					self.snake_score += 1


				if self.fruit.pos == self.sneke.body[0]:
					# add another block to the snake
					self.sneke.add_block()
					# change fruit position
					self.fruit.randomize()
					# add 1 to the snake score
					self.sneke_score += 1

			def check_fail(self):
				#check is snake is ouside of screen 
				if not 0 <= self.snake.body[0].x < cell_number or not 0<= self.snake.body[0].y <cell_number:
					self.snake_winner = False
					self.sneke_winner = True
					self.game_over()
					
				#check is sneke is outside of screen
				if not 0 <= self.sneke.body[0].x < cell_number or not 0<= self.sneke.body[0].y <cell_number:
					self.snake_winner = True
					self.sneke_winner = False
					self.game_over()
				# check if snake hits itself
				for block in self.snake.body[1:]:
					if self.snake.body[0] == block:
						self.snake_winner = False
						self.sneke_winner = True
						self.game_over()
				# check if sneke hits itself:
				for block in self.sneke.body[1:]:
					if self.sneke.body[0] == block:
						self.snake_winner = True
						self.sneke_winner = False
						self.game_over()
				#check if snake hits sneke 
				for block in self.sneke.body[1:]:
					if self.snake.body[0] == block:
						self.snake_winner = False
						self.sneke_winner = True
						self.game_over()
				#check if sneke hits snake on body
				for block in self.snake.body[1:]:
					if self.sneke.body[0] == block:
						self.snake_winner = True
						self.sneke_winner = False
						self.game_over()


			def game_over(self):
				self.running = False # this is to define whether or not the game is running
				#breakpoint()
				game_over_screen()

	main_game = MAIN()
	SCREENUPDATE = pygame.USEREVENT # this is for the clocking of the snake movement.
	#SCREEN_UPDATE is us defining an event
	pygame.time.set_timer(SCREENUPDATE,60)
	main_game.running = True

	while main_game.running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == SCREENUPDATE:
				main_game.update()
			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_UP and main_game.snake.direction.y !=1:
					main_game.snake.direction = Vector2(0,-1)
				if event.key == pygame.K_DOWN and main_game.snake.direction.y != -1:
					main_game.snake.direction = Vector2(0,1)
				if event.key == pygame.K_LEFT and main_game.snake.direction.x != 1:
					main_game.snake.direction = Vector2(-1,0)
				if event.key == pygame.K_RIGHT and main_game.snake.direction.x != -1:
					main_game.snake.direction = Vector2(1,0)

				if event.key == pygame.K_w and main_game.sneke.direction.y !=1:
					main_game.sneke.direction = Vector2(0,-1)
				if event.key == pygame.K_s and main_game.sneke.direction.y != -1:
					main_game.sneke.direction = Vector2(0,1)
				if event.key == pygame.K_a and main_game.sneke.direction.x != 1:
					main_game.sneke.direction = Vector2(-1,0)
				if event.key == pygame.K_d and main_game.sneke.direction.x != -1:
					main_game.sneke.direction = Vector2(1,0)
				if event.key == pygame.K_ESCAPE: # so it continues with the main loop
					main_game.game_over()
					
		
		global snake_score
		global sneke_score
		snake_score = main_game.snake_score
		sneke_score = main_game.sneke_score
		scoreboard = SCOREBOARD(snake_score,sneke_score)
		
		
		screen.fill(green_grey)
		main_game.draw_elements()	
		scoreboard.draw_elements()
		returnTime()
		pygame.display.update()
		clock.tick(60)
#-------------------------------------------------------------------------GAME OVER SCREEN---------------------------------------------------------------------#
def game_over_screen():
	class TEXT:
		def __init__(self):
			font = pygame.font.Font('Fonts/Pixeltype.ttf', 32)

			self.SNAKE_score = font.render(f'{snake_score} ', True, green)
			self.SNAKE_score_Rect = self.SNAKE_score.get_rect()
			self.SNAKE_score_Rect.center = ( cell_size*cell_number//2 - 3*cell_size, cell_size*cell_number//2 - cell_size)



			self.gameoverBackground =  pygame.transform.scale(pygame.image.load('images/gameover_screen.png'),(cell_number*cell_size,cell_number*cell_size))
			self.gameoverBackground_Rect = self.gameoverBackground.get_rect()


			self.SNEKE_score = font.render(f'SNEKE SCORE:{sneke_score} ', True, SNEKE_COLOR)
			self.SNEKE_score_Rect = self.SNEKE_score.get_rect()
			self.SNEKE_score_Rect.center = ( cell_size*cell_number// 2,cell_size*cell_number// 4 )

			self.enterToCont = font.render('PRESS ENTER TO CONTINUE ', True, '#005C5B')
			self.enterToCont_Rect = self.enterToCont.get_rect()
			self.enterToCont_Rect.center = ( cell_size*cell_number// 2,cell_size*cell_number// 8 )

			



	
		def draw_text(self):
			screen.blit(self.gameoverBackground, self.gameoverBackground_Rect)
			screen.blit(self.SNAKE_score, self.SNAKE_score_Rect)
			screen.blit(self.SNEKE_score, self.SNEKE_score_Rect)
			screen.blit(self.enterToCont, self.enterToCont_Rect)
			
	class GAME_OVER:
		def __init__(self):
			self.running = True
			self.text = TEXT()
		def draw_elements(self):
			self.text.draw_text()

	game_over = GAME_OVER()
	while game_over.running:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			mouse_pos = pygame.mouse.get_pos()
			if game_over.text.enterToCont_Rect.collidepoint(mouse_pos):
				if event.type == pygame.MOUSEBUTTONUP:
					main_game()
						
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					main_game()

		screen.fill(green_grey)
		game_over.draw_elements()
		pygame.display.update()
		clock.tick(60)


main_game()
