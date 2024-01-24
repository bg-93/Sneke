import pdb
import math
import pygame, sys, random
from pygame.math import Vector2

#pdb.set_trace()
#1301
pygame.init()
cell_size = 13
cell_number = 60
SNEKE_COLOR = (132,113,79)
SNAKE_COLOR = (49,35,30)

length = cell_number*cell_size

screen = pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size))
clock = pygame.time.Clock()
score_font = pygame.font.Font( 'Fonts/Pixeltype.ttf' , 50)


global green_grey
global viridian
global green
global purple
global white
white = (255, 251, 254)
purple = (124, 119, 185)
green = (176, 254, 118)
viridian = (71, 137, 120)
green_grey = (46, 92, 107)
green_light = (160, 222, 133)
global DEFBGCOL 
global MAINMENUCOL 
MAINMENUCOL = green
DEFBGCOL= viridian



#-----------------------------------------------------------------MAIN MENU-----------------------------------------------------------------------#
def main_menu():
	class TEXT:
		def __init__(self):
			font = pygame.font.Font('Fonts/Pixeltype.ttf', 80)

			self.mainmenu = pygame.transform.scale(pygame.image.load('images/welcome_banner.png'),(0.7*67.39*cell_size,7*cell_size))
			self.mainmenu_Rect = self.mainmenu.get_rect()
			self.mainmenu_Rect.center = (cell_size*cell_number//2,cell_size*cell_number//3)
			


			self.enterToCont = pygame.transform.scale(pygame.image.load('images/continue_button.png'),(0.3*56.4*cell_size,3*cell_size))
			self.enterToCont_Rect = self.enterToCont.get_rect()
			self.enterToCont_Rect.center = ( cell_size*cell_number// 2,cell_size*cell_number// 1.5 )
			

			self.pressO = pygame.transform.scale(pygame.image.load('images/rules_button.png'),(0.5*30.0935*cell_size,5*cell_size))
			self.pressO_Rect = self.pressO.get_rect()
			self.pressO_Rect.center = ( cell_size*cell_number// 2,cell_size*cell_number//2  )


		def draw_text(self):
			screen.blit(self.enterToCont, self.enterToCont_Rect)
			screen.blit(self.pressO, self.pressO_Rect)
			screen.blit(self.mainmenu, self.mainmenu_Rect)

	class MAIN:
		def __init__(self):
			self.text = TEXT()

		def draw_elements(self):
			self.text.draw_text()

#		def detect_click(self):
#			mouse_pos = pygame.mouse.get_pos()
#			if self.text.enterToCont_Rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]: 
#				self.enterToCont_Button = True
#			if self.text.pressO_Rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
#				self.pressO_Button = True
	while True:
		#home screen
		main_menu = MAIN()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()



			mouse_pos = pygame.mouse.get_pos()
			if main_menu.text.enterToCont_Rect.collidepoint(mouse_pos):
				if event.type == pygame.MOUSEBUTTONUP:
					options_screen()
			if main_menu.text.pressO_Rect.collidepoint(mouse_pos):
				if event.type == pygame.MOUSEBUTTONUP:
					rule_screen()


			if event.type == pygame.KEYDOWN :
				if event.key == pygame.K_RETURN:# if we press the "enter key" from here then the options will run
					options_screen()
				if event.key == pygame.K_o:
					rule_screen()
		
		screen.fill(green_grey)

		for y in range(cell_number):
		    for x in range(cell_number):
		        rect = pygame.Rect(x*cell_size, y*cell_size,cell_size,cell_size)
		        pygame.draw.rect(screen, (0,0,0), rect,1)

		main_menu.draw_elements()
		pygame.display.update()
		clock.tick(60)
#-----------------------------------------------------------------------OPTIONS SCREEN-------------------------------------------------------------------------#
def options_screen():
	class TEXT:
		def __init__(self):
			font =pygame.font.Font( 'Fonts/Pixeltype.ttf' , 80)

			self.options = pygame.transform.scale(pygame.image.load('images/options_banner.png'),(0.6*41.85*cell_size,6*cell_size))
			self.options_Rect = self.options.get_rect()
			self.options_Rect.center = ( cell_size*cell_number// 2,cell_size*cell_number// 10 )


			self.enterToCont = font.render('PRESS ENTER TO PLAY', True, viridian)
			self.enterToCont_Rect = self.enterToCont.get_rect()
			self.enterToCont_Rect.center = ( cell_size*cell_number// 1.6,cell_size*cell_number-4*cell_size )


			self.goBack = pygame.transform.scale(pygame.image.load('images/back_2_button.png'),(0.3*29.6*cell_size,3*cell_size))
			self.goBack_Rect = self.goBack.get_rect()
			self.goBack_Rect.center = ( 5*cell_size+2*cell_size,cell_size*cell_number-5*cell_size )

# and now we will begin the buttons

			self.human = pygame.transform.scale(pygame.image.load('images/human_symbol.png'),(0.6*10.9*cell_size,6*cell_size))
			self.human_Rect = self.human.get_rect()
			self.human_Rect.center = (length/3+30*cell_size,length/5+3*cell_size)

			self.human1 = pygame.transform.scale(pygame.image.load('images/human_symbol.png'),(0.6*10.9*cell_size,6*cell_size))
			self.human1_Rect = self.human1.get_rect()
			self.human1_Rect.center = (length/3+26*cell_size,length/5+3*cell_size)

			self.humanFlag = False



			self.humanSingle = pygame.transform.scale(pygame.image.load('images/human_symbol.png'),(0.6*10.6*cell_size,6*cell_size))
			self.humanSingle_Rect = self.humanSingle.get_rect()
			self.humanSingle_Rect.center = (length/5+26*cell_size, length/5+3*cell_size)
			self.humanSingleFlag = False



			self.timed = pygame.transform.scale(pygame.image.load('images/timed.png'),(0.6*6.55*cell_size,6*cell_size))
			self.timed_Rect = self.timed.get_rect()
			self.timed_Rect.center = (length/3+30*cell_size,length/2.6+3*cell_size)
			self.timedFlag = False



			self.suddenDeath = pygame.transform.scale(pygame.image.load('images/sudden_death.png'),(6*cell_size,6*cell_size))
			self.suddenDeath_Rect = self.suddenDeath.get_rect()
			self.suddenDeath_Rect.center = (length/5+26*cell_size,length/2.6 +3*cell_size)
			self.sdFlag = False 



			#self.obstacles = pygame.transform.scale(pygame.image.load('images/_symbol.png'),(0.3*10.9*cell_size,3*cell_size))
			#self.obstacles_Rect = self.obstacles.get_rect()

			self.gameSpeed = pygame.transform.scale(pygame.image.load('images/game_speed.png'),(0.3*92.2*cell_size,3*cell_size))
			self.gameSpeed_Rect = self.gameSpeed.get_rect()
			self.gameSpeed_Rect.center = (length/3,length/1.5)



			self.modeOpp = pygame.transform.scale(pygame.image.load('images/modeOpp.png'),(1.8*0.9*23.6*cell_size,1.8*11*cell_size))
			self.modeOpp_Rect = self.modeOpp.get_rect() 
			self.modeOpp_Rect.center = ( length/4+9*cell_size,length/3)









			self.fast = pygame.transform.scale(pygame.image.load('images/fast.png'),(0.4*23.58*cell_size,4*cell_size))
			self.fast_Rect = self.fast.get_rect()
			self.fast_Rect.center = (length/3+ 9*cell_size,length/1.5+ 5*cell_size)
			self.fastFlag = False



			self.slow = pygame.transform.scale(pygame.image.load('images/slow.png'),(0.4*26.56*cell_size,4*cell_size))
			self.slow_Rect = self.slow.get_rect()
			self.slow_Rect.center = (length/3 - 9*cell_size,length/1.5+ 5*cell_size)
			self.slowFlag = False






		
		def draw_text(self):
			screen.blit(self.enterToCont, self.enterToCont_Rect)
			screen.blit(self.goBack, self.goBack_Rect)
			screen.blit(self.options, self.options_Rect)
			screen.blit(self.human1, self.human1_Rect)
			screen.blit(self.human, self.human_Rect)
			screen.blit(self.humanSingle,self.humanSingle_Rect) 
			screen.blit(self.timed, self.timed_Rect)
			screen.blit(self.suddenDeath, self.suddenDeath_Rect)
			screen.blit(self.fast, self.fast_Rect)
			screen.blit(self.slow, self.slow_Rect)
			screen.blit(self.gameSpeed, self.gameSpeed_Rect)
			screen.blit(self.modeOpp, self.modeOpp_Rect)
			
			# now we're going to make the conditionals to draw a rectangle around the selected option
			if self.slowFlag == True:
				pygame.draw.rect(screen, (255,0,0), pygame.Rect(self.slow_Rect.x,self.slow_Rect.y, 10, 10))
			if self.fastFlag == True:
				pygame.draw.rect(screen, (255,0,0), pygame.Rect(self.fast_Rect.x,self.fast_Rect.y, 10, 10))
			if self.sdFlag == True:
				pygame.draw.rect(screen, (255,0,0), pygame.Rect(self.suddenDeath_Rect.x, self.suddenDeath_Rect.y, 10, 10))
			if self.timedFlag == True:
				pygame.draw.rect(screen, (255,0,0), pygame.Rect(self.timed_Rect.x,self.timed_Rect.y, 10, 10))
			if self.humanFlag == True:
				pygame.draw.rect(screen, (255,0,0), pygame.Rect(self.human_Rect.x,self.human_Rect.y, 10, 10))
			if self.humanSingleFlag == True:
				pygame.draw.rect(screen, (255,0,0), pygame.Rect(self.humanSingle_Rect.x,self.humanSingle_Rect.y, 10, 10))


			

	class OPTIONS:
		def __init__(self):
			self.running = True
			self.text  = TEXT()
		

		def draw_elements(self):
			self.text.draw_text()


	

	options_screen = OPTIONS()

	while options_screen.running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		#	if event.type == pygame.KEYDOWN :
		#		if event.key == pygame.K_RETURN:
		#			main_game1()
		#			game_over_screen1()


			mouse_pos = pygame.mouse.get_pos()

		#	if options_screen.text.enterToCont_Rect.collidepoint(mouse_pos):
		#		if event.type == pygame.MOUSEBUTTONUP:
		#			main_game1()
		#			game_over_screen1()


			if options_screen.text.goBack_Rect.collidepoint(mouse_pos):
				if event.type == pygame.MOUSEBUTTONUP:
					options_screen.running = False

			if options_screen.text.human_Rect.collidepoint(mouse_pos):
				if event.type == pygame.MOUSEBUTTONUP:
					options_screen.text.humanFlag = True
					options_screen.text.humanSingleFlag = False

			if options_screen.text.humanSingle_Rect.collidepoint(mouse_pos):
				if event.type == pygame.MOUSEBUTTONUP:
					options_screen.text.humanFlag = False
					options_screen.text.humanSingleFlag = True

			if options_screen.text.suddenDeath_Rect.collidepoint(mouse_pos):
				if event.type == pygame.MOUSEBUTTONUP:
					options_screen.text.sdFlag = True
					options_screen.text.timedFlag = False

			if options_screen.text.timed_Rect.collidepoint(mouse_pos):
				if event.type == pygame.MOUSEBUTTONUP:
					options_screen.text.sdFlag = False
					options_screen.text.timedFlag = True

			if options_screen.text.fast_Rect.collidepoint(mouse_pos):
				if event.type == pygame.MOUSEBUTTONUP:
					options_screen.text.fastFlag = True
					options_screen.text.slowFlag = False

			if options_screen.text.slow_Rect.collidepoint(mouse_pos):
				if event.type == pygame.MOUSEBUTTONUP:
					options_screen.text.fastFlag = False
					options_screen.text.slowFlag = True
			

			if event.type == pygame.KEYDOWN :
				if event.key == pygame.K_RETURN:

					if options_screen.text.humanFlag:

						if options_screen.text.fastFlag and options_screen.text.sdFlag:
							main_game1()
							game_over_screen1()


						if options_screen.text.fastFlag and options_screen.text.timedFlag:
							main_game3()
							game_over_screen3()
							

						if options_screen.text.slowFlag and options_screen.text.sdFlag:
							main_game2()
							game_over_screen2()

						if options_screen.text.slowFlag and options_screen.text.timedFlag:
							main_game4()
							game_over_screen4()
							
					
					if options_screen.text.humanSingleFlag :
						main_game5()
						game_over_screen5()

					


		screen.fill(green_grey)
		

		options_screen.draw_elements()
		pygame.display.update()
		clock.tick(60)

#-----------------------SUDDEN DEATH-------------------------------------------------MAIN GAME 1 1 1 1 1 1 1 1 1 1 1 1 1 1 ---------------------------------------------------------------------------#

def main_game1():
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
				pygame.draw.rect(screen,white, block_rect)
				#snake_block = pygame.transform.scale(pygame.image.load('images/snake_body.png'),(cell_size,cell_size))
				#snake_block_rect = snake_block.get_rect()
				#snake_block_rect.center = (x_pos,y_pos)
				#screen.blit(snake_block, snake_block_rect)\
			head_rect = pygame.Rect(int(self.body[0].x*cell_size),int(self.body[0].y*cell_size),cell_size,cell_size)
			pygame.draw.rect(screen,green_light, head_rect)

			

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
				head_rect = pygame.Rect(int(self.body[0].x*cell_size),int(self.body[0].y*cell_size),cell_size,cell_size)
				pygame.draw.rect(screen,purple, head_rect)

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




	class FRUIT:
		def __init__(self):
			 self.randomize()

		def draw_fruit(self):
			#fruit = pygame.transform.scale(pygame.image.load('images/apple.png'),(cell_size,cell_size))
			#fruit_rect = fruit.get_rect()
			#fruit_rect.center = (cell_size*self.x, cell_size*self.y)
			#screen.blit(fruit, fruit_rect)

			pygame.draw.rect(screen,(255,0,0),pygame.Rect(cell_size*self.x,cell_size*self.y , cell_size, cell_size))
		def randomize(self):
			self.x = random.randint(0,cell_number-1)
			self.y = random.randint(0, cell_number-1)
			self.pos = Vector2(self.x, self.y)
	
	class FRUIT1:
		def __init__(self):
			 self.randomize()

		def draw_fruit1(self):
			#fruit1 = pygame.transform.scale(pygame.image.load('images/apple.png'),(cell_size,cell_size))
			#fruit1_rect = fruit1.get_rect()
			#fruit1_rect.center = (cell_size*self.x, cell_size*self.y)
			#screen.blit(fruit1, fruit1_rect)
			pygame.draw.rect(screen,(255,0,0),pygame.Rect(cell_size*self.x,cell_size*self.y , cell_size, cell_size))

		def randomize(self):
			self.x = random.randint(0,cell_number-1)
			self.y = random.randint(0, cell_number-1)
			self.pos = Vector2(self.x, self.y)


	class SCOREBOARD:
		def __init__(self,score1 ,score2 ):
			self.score1 = score1
			self.score2 = score2

			font = pygame.font.Font('Fonts/Pixeltype.ttf', 32)
			self.score1_text = font.render(f'snake {self.score1}', True, white)
			self.score1_Rect = self.score1_text.get_rect()
			self.score1_Rect.center = ( cell_size*cell_number// 5,cell_size*cell_number// 20 )

			self.score2_text = font.render(f'sneke {self.score2}', True, (163,68,115))
			self.score2_Rect = self.score2_text.get_rect()
			self.score2_Rect.center = ( cell_size*cell_number// 1.3,cell_size*cell_number// 20)
		def draw_elements(self):
			screen.blit(self.score1_text, self.score1_Rect)
			screen.blit(self.score2_text, self.score2_Rect)		


	class MAIN:
			def __init__(self):# you have to chuck in the difficulty settings and time duration settings in here too in later stages
				self.snake = SNAKE()
				self.fruit = FRUIT()
				self.fruit1 = FRUIT1()
				self.sneke = SNEKE()
				self.running = True # this is to determine whether or not the game state is active/running
				self.snake_half = False
				self.sneke_half = False
				self.snake_score = 0
				self.sneke_score = 0
			def update(self):
				self.snake.move_snake()
				self.sneke.move_sneke()
				self.check_collision()
				self.check_fail()
			def draw_elements(self):
				self.fruit.draw_fruit()
				self.fruit1.draw_fruit1()
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

				if self.fruit1.pos == self.snake.body[0]:
					# add another block to the snake
					self.snake.add_block()
					# change fruit position
					self.fruit1.randomize()
					#add 1 to the snake score
					self.snake_score += 1


				if self.fruit1.pos == self.sneke.body[0]:
					# add another block to the snake
					self.sneke.add_block()
					# change fruit position
					self.fruit1.randomize()
					# add 1 to the snake score
					self.sneke_score += 1


			def check_fail(self):
				#check is snake is ouside of screen 
				if not 0 <= self.snake.body[0].x < cell_number or not 0<= self.snake.body[0].y <cell_number:
					self.snake_half = True
					self.sneke_half = False
					self.game_over()
					
				#check is sneke is outside of screen
				if not 0 <= self.sneke.body[0].x < cell_number or not 0<= self.sneke.body[0].y <cell_number:
					self.snake_half = False
					self.sneke_half = True
					self.game_over()
				# check if snake hits itself
				for block in self.snake.body[1:]:
					if self.snake.body[0] == block:
						self.snake_half = True
						self.sneke_half = False
						self.game_over()
				# check if sneke hits itself:
				for block in self.sneke.body[1:]:
					if self.sneke.body[0] == block:
						self.snake_half = False
						self.sneke_half = True
						self.game_over()
				#check if snake hits sneke 
				for block in self.sneke.body[1:]:
					if self.snake.body[0] == block:
						self.snake_half = True
						self.sneke_half = False
						self.game_over()
				#check if sneke hits snake on body
				for block in self.snake.body[1:]:
					if self.sneke.body[0] == block:
						self.snake_half = False
						self.sneke_half = True
						self.game_over()


			def game_over(self):
				self.running = False # this is to define whether or not the game is running


	main_game = MAIN()
	SCREENUPDATE = pygame.USEREVENT # this is for the clocking of the snake movement.
	#SCREEN_UPDATE is us defining an event
	pygame.time.set_timer(SCREENUPDATE,60)
	main_game.running = True


	start_time = int(pygame.time.get_ticks()/1000)
	
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
					main_game.running = False

					
		
		
		
		global snake_score
		global sneke_score
		snake_score = main_game.snake_score
		sneke_score = main_game.sneke_score
		scoreboard = SCOREBOARD(snake_score,sneke_score)

		global snake_loss
		global sneke_loss
		sneke_loss = main_game.sneke_half
		snake_loss = main_game.snake_half
		


		screen.fill(green_grey)
		for y in range(cell_number):
		    for x in range(cell_number):
		        rect = pygame.Rect(x*cell_size, y*cell_size,cell_size,cell_size)
		        pygame.draw.rect(screen, (0,0,0), rect,1)

		main_game.draw_elements()	
		scoreboard.draw_elements()

		global current_time

		current_time = int(pygame.time.get_ticks()/1000)  - start_time
		time_surf = score_font.render(f'{current_time}', False, (64,64,64))
		time_rect = time_surf.get_rect(center = (400, 50))
		screen.blit(time_surf,time_rect)


		pygame.display.update()
		clock.tick(60)

#-----------------------------SUDDEN DEATH--------------------------------------------GAME OVER SCREEN 1 1 1 1 1 1 1 1 1 1---------------------------------------------------------------------#

def game_over_screen1():
	class TEXT:
		def __init__(self):
			font = pygame.font.Font('Fonts/Pixeltype.ttf', 75)
			global sneke_score
			global snake_score
			global snake_loss
			global sneke_loss

			if sneke_loss:
				sneke_score = math.ceil(sneke_score/1.14)
			if snake_loss: 
				snake_score = math.ceil(snake_score/1.14)


			if sneke_score > snake_score:
				sneke_loss = False
				snake_loss = True

			if sneke_score < snake_score:
				sneke_loss = True
				snake_loss = False
		
			self.goBack = pygame.transform.scale(pygame.image.load('images/back_button.png'),(0.3*29.6*cell_size,3*cell_size))
			self.goBack_Rect = self.goBack.get_rect()
			self.goBack_Rect.center = ( 5*cell_size+2*cell_size,cell_size*cell_number-5*cell_size )



			self.gameoverBackground =  pygame.transform.scale(pygame.image.load('images/gameover_screen.png'),(cell_number*cell_size,cell_number*cell_size))
			self.gameoverBackground_Rect = self.gameoverBackground.get_rect()

			self.SNAKE_score = font.render(f'{snake_score} points', True, green)
			self.SNAKE_score_Rect = self.SNAKE_score.get_rect()
			self.SNAKE_score_Rect.center = ( cell_size*cell_number// 2 - 2*cell_size,cell_size*cell_number// 3.5+12*cell_size )

			self.SNEKE_score = font.render(f'{sneke_score} points', True, green)
			self.SNEKE_score_Rect = self.SNEKE_score.get_rect()
			self.SNEKE_score_Rect.center = ( cell_size*cell_number// 2- 2*cell_size,cell_size*cell_number// 2.5+10*cell_size )

			self.winnerSnake = font.render(f'SNAKE',True, green_light)
			self.winnerSnake_Rect = self.winnerSnake.get_rect()
			self.winnerSnake_Rect.center = (length//2,length//4)

			self.winnerSneke = font.render(f'SNEKE',True, green_light)
			self.winnerSneke_Rect = self.winnerSneke.get_rect()
			self.winnerSneke_Rect.center = (length//2,length//4)

			self.draw = font.render(f'NO ONE (its a draw)',True, green_light)
			self.draw_Rect = self.draw.get_rect()
			self.draw_Rect.center = (length//2,length//4)

			self.duration = font.render(f'{current_time} seconds', True, green_light)
			self.duration_Rect = self.duration.get_rect()
			self.duration_Rect.center = (length//2 + 10*cell_size, length//2 +12*cell_size)
	
		def draw_text(self):
		
			screen.blit(self.gameoverBackground, self.gameoverBackground_Rect)
			screen.blit(self.SNAKE_score, self.SNAKE_score_Rect)
			screen.blit(self.SNEKE_score, self.SNEKE_score_Rect)
			screen.blit(self.goBack, self.goBack_Rect)
			screen.blit(self.duration, self.duration_Rect)
		
			if snake_score == sneke_score:
				screen.blit(self.draw,self.draw_Rect)
			else:	
				if sneke_loss:
					screen.blit(self.winnerSnake,self.winnerSnake_Rect)

				if snake_loss:
					screen.blit(self.winnerSneke, self.winnerSneke_Rect)

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


			if game_over.text.goBack_Rect.collidepoint(mouse_pos):
				if event.type == pygame.MOUSEBUTTONUP:
					game_over.running = False
						
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					game_over.running = False

		screen.fill(green_grey)
		for y in range(cell_number):
		    for x in range(cell_number):
		        rect = pygame.Rect(x*cell_size, y*cell_size,cell_size,cell_size)
		        pygame.draw.rect(screen, (0,0,0), rect,1)

		game_over.draw_elements()
		pygame.display.update()
		clock.tick(60)




#----------------------SUDDEN DEATH---------------------------------------------MAIN GAME  2 2 2 2 2 2 2 2 2 2 2------------------------------------------------

def main_game2():
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
				pygame.draw.rect(screen,white, block_rect)
				#snake_block = pygame.transform.scale(pygame.image.load('images/snake_body.png'),(cell_size,cell_size))
				#snake_block_rect = snake_block.get_rect()
				#snake_block_rect.center = (x_pos,y_pos)
				#screen.blit(snake_block, snake_block_rect)\
			head_rect = pygame.Rect(int(self.body[0].x*cell_size),int(self.body[0].y*cell_size),cell_size,cell_size)
			pygame.draw.rect(screen,green_light, head_rect)

			

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
				head_rect = pygame.Rect(int(self.body[0].x*cell_size),int(self.body[0].y*cell_size),cell_size,cell_size)
				pygame.draw.rect(screen,purple, head_rect)

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
			#fruit = pygame.transform.scale(pygame.image.load('images/apple.png'),(cell_size,cell_size))
			#fruit_rect = fruit.get_rect()
			#fruit_rect.center = (cell_size*self.x, cell_size*self.y)
			#screen.blit(fruit, fruit_rect)
			pygame.draw.rect(screen,(255,0,0),pygame.Rect(cell_size*self.x,cell_size*self.y , cell_size, cell_size))

		def randomize(self):
			self.x = random.randint(0,cell_number-1)
			self.y = random.randint(0, cell_number-1)
			self.pos = Vector2(self.x, self.y)
	
	class FRUIT1:
		def __init__(self):
			 self.randomize()

		def draw_fruit1(self):
			#fruit1 = pygame.transform.scale(pygame.image.load('images/apple.png'),(cell_size,cell_size))
			#fruit1_rect = fruit1.get_rect()
			#fruit1_rect.center = (cell_size*self.x, cell_size*self.y)
			#screen.blit(fruit1, fruit1_rect)
			pygame.draw.rect(screen,(255,0,0),pygame.Rect(cell_size*self.x,cell_size*self.y , cell_size, cell_size))


		def randomize(self):
			self.x = random.randint(0,cell_number-1)
			self.y = random.randint(0, cell_number-1)
			self.pos = Vector2(self.x, self.y)


	class SCOREBOARD:
		def __init__(self,score1 ,score2 ):
			self.score1 = score1
			self.score2 = score2

			font = pygame.font.Font('Fonts/Pixeltype.ttf', 32)
			self.score1_text = font.render(f'snake {self.score1}', True, white)
			self.score1_Rect = self.score1_text.get_rect()
			self.score1_Rect.center = ( cell_size*cell_number// 5,cell_size*cell_number// 20 )

			self.score2_text = font.render(f'sneke {self.score2}', True, (163,68,115))
			self.score2_Rect = self.score2_text.get_rect()
			self.score2_Rect.center = ( cell_size*cell_number// 1.3,cell_size*cell_number// 20)
		def draw_elements(self):
			screen.blit(self.score1_text, self.score1_Rect)
			screen.blit(self.score2_text, self.score2_Rect)		


	class MAIN:
			def __init__(self):# you have to chuck in the difficulty settings and time duration settings in here too in later stages
				self.snake = SNAKE()
				self.fruit = FRUIT()
				self.fruit1 = FRUIT1()
				self.sneke = SNEKE()
				self.running = True # this is to determine whether or not the game state is active/running
				self.snake_half = False
				self.sneke_half = False
				self.snake_score = 0
				self.sneke_score = 0
			def update(self):
				self.snake.move_snake()
				self.sneke.move_sneke()
				self.check_collision()
				self.check_fail()
			def draw_elements(self):
				self.fruit.draw_fruit()
				self.fruit1.draw_fruit1()
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

				if self.fruit1.pos == self.snake.body[0]:
					# add another block to the snake
					self.snake.add_block()
					# change fruit position
					self.fruit1.randomize()
					#add 1 to the snake score
					self.snake_score += 1


				if self.fruit1.pos == self.sneke.body[0]:
					# add another block to the snake
					self.sneke.add_block()
					# change fruit position
					self.fruit1.randomize()
					# add 1 to the snake score
					self.sneke_score += 1


			def check_fail(self):
				#check is snake is ouside of screen 
				if not 0 <= self.snake.body[0].x < cell_number or not 0<= self.snake.body[0].y <cell_number:
					self.snake_half = False
					self.sneke_half = True
					self.game_over()
					
				#check is sneke is outside of screen
				if not 0 <= self.sneke.body[0].x < cell_number or not 0<= self.sneke.body[0].y <cell_number:
					self.snake_half = True
					self.sneke_half = False
					self.game_over()
				# check if snake hits itself
				for block in self.snake.body[1:]:
					if self.snake.body[0] == block:
						self.snake_half = False
						self.sneke_half = True
						self.game_over()
				# check if sneke hits itself:
				for block in self.sneke.body[1:]:
					if self.sneke.body[0] == block:
						self.snake_half = True
						self.sneke_half = False
						self.game_over()
				#check if snake hits sneke 
				for block in self.sneke.body[1:]:
					if self.snake.body[0] == block:
						self.snake_half = False
						self.sneke_half = True
						self.game_over()
				#check if sneke hits snake on body
				for block in self.snake.body[1:]:
					if self.sneke.body[0] == block:
						self.snake_half = True
						self.sneke_half = False
						self.game_over()


			def game_over(self):
				self.running = False # this is to define whether or not the game is running
				#breakpoint()

	main_game = MAIN()
	SCREENUPDATE = pygame.USEREVENT # this is for the clocking of the snake movement.
	#SCREEN_UPDATE is us defining an event
	pygame.time.set_timer(SCREENUPDATE,80)
	main_game.running = True


	start_time = int(pygame.time.get_ticks()/1000)
	
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
					main_game.running = False

					
		
		
		
		global snake_score
		global sneke_score
		snake_score = main_game.snake_score
		sneke_score = main_game.sneke_score
		scoreboard = SCOREBOARD(snake_score,sneke_score)

		global snake_loss
		global sneke_loss
		sneke_loss = main_game.sneke_half
		snake_loss = main_game.snake_half
		


		screen.fill(green_grey)
		for y in range(cell_number):
		    for x in range(cell_number):
		        rect = pygame.Rect(x*cell_size, y*cell_size,cell_size,cell_size)
		        pygame.draw.rect(screen, (0,0,0), rect,1)

		main_game.draw_elements()	
		scoreboard.draw_elements()

		global current_time

		current_time = int(pygame.time.get_ticks()/1000)  - start_time
		time_surf = score_font.render(f'{current_time}', False, white)
		time_rect = time_surf.get_rect(center = (400, 50))
		screen.blit(time_surf,time_rect)


		pygame.display.update()
		clock.tick(60)

#--------------------------SUDDEN DEATH--------------------------------------------GAMEOVER 2 2 22 2 2 2 2 2 2 2 2----------------------------------------------

def game_over_screen2():
	class TEXT:
		def __init__(self):
			font = pygame.font.Font('Fonts/Pixeltype.ttf', 75)
			global sneke_score
			global snake_score
			global snake_loss
			global sneke_loss

			if sneke_loss:
				sneke_score = math.ceil(sneke_score/1.14)
			if snake_loss: 
				snake_score = math.ceil(snake_score/1.14)


			if sneke_score > snake_score:
				sneke_loss = False
				snake_loss = True

			if sneke_score < snake_score:
				sneke_loss = True
				snake_loss = False
		
			self.goBack = pygame.transform.scale(pygame.image.load('images/back_button.png'),(0.3*29.6*cell_size,3*cell_size))
			self.goBack_Rect = self.goBack.get_rect()
			self.goBack_Rect.center = ( 5*cell_size+2*cell_size,cell_size*cell_number-5*cell_size )



			self.gameoverBackground =  pygame.transform.scale(pygame.image.load('images/gameover_screen.png'),(cell_number*cell_size,cell_number*cell_size))
			self.gameoverBackground_Rect = self.gameoverBackground.get_rect()

			self.SNAKE_score = font.render(f'{snake_score} points', True, green)
			self.SNAKE_score_Rect = self.SNAKE_score.get_rect()
			self.SNAKE_score_Rect.center = ( cell_size*cell_number// 2 - 2*cell_size,cell_size*cell_number// 3.5+12*cell_size )

			self.SNEKE_score = font.render(f'{sneke_score} points', True, green)
			self.SNEKE_score_Rect = self.SNEKE_score.get_rect()
			self.SNEKE_score_Rect.center = ( cell_size*cell_number// 2- 2*cell_size,cell_size*cell_number// 2.5+10*cell_size )

			self.winnerSnake = font.render(f'SNAKE',True, green_light)
			self.winnerSnake_Rect = self.winnerSnake.get_rect()
			self.winnerSnake_Rect.center = (length//2,length//4)

			self.winnerSneke = font.render(f'SNEKE',True, green_light)
			self.winnerSneke_Rect = self.winnerSneke.get_rect()
			self.winnerSneke_Rect.center = (length//2,length//4)

			self.draw = font.render(f'NO ONE (its a draw)',True, green_light)
			self.draw_Rect = self.draw.get_rect()
			self.draw_Rect.center = (length//2,length//4)

			self.duration = font.render(f'{current_time} seconds', True, green_light)
			self.duration_Rect = self.duration.get_rect()
			self.duration_Rect.center = (length//2 + 10*cell_size, length//2 +12*cell_size)
	
		def draw_text(self):
		
			screen.blit(self.gameoverBackground, self.gameoverBackground_Rect)
			screen.blit(self.SNAKE_score, self.SNAKE_score_Rect)
			screen.blit(self.SNEKE_score, self.SNEKE_score_Rect)
			screen.blit(self.goBack, self.goBack_Rect)
			screen.blit(self.duration, self.duration_Rect)
		
			if snake_score == sneke_score:
				screen.blit(self.draw,self.draw_Rect)
			else:	
				if sneke_loss:
					screen.blit(self.winnerSnake,self.winnerSnake_Rect)

				if snake_loss:
					screen.blit(self.winnerSneke, self.winnerSneke_Rect)

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


			if game_over.text.goBack_Rect.collidepoint(mouse_pos):
				if event.type == pygame.MOUSEBUTTONUP:
					game_over.running = False
						
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					game_over.running = False

		screen.fill(green_grey)
		for y in range(cell_number):
		    for x in range(cell_number):
		        rect = pygame.Rect(x*cell_size, y*cell_size,cell_size,cell_size)
		        pygame.draw.rect(screen, (0,0,0), rect,1)

		game_over.draw_elements()
		pygame.display.update()
		clock.tick(60)





#-------------------------TIMED---------SLOW---------------------------------MAIN GAME  3 3 3 3 3 3 3 3 3 3 33------------------------------------------------

def main_game3():
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
				pygame.draw.rect(screen,white, block_rect)
				#snake_block = pygame.transform.scale(pygame.image.load('images/snake_body.png'),(cell_size,cell_size))
				#snake_block_rect = snake_block.get_rect()
				#snake_block_rect.center = (x_pos,y_pos)
				#screen.blit(snake_block, snake_block_rect)\
			head_rect = pygame.Rect(int(self.body[0].x*cell_size),int(self.body[0].y*cell_size),cell_size,cell_size)
			pygame.draw.rect(screen,green, head_rect)

			

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
				head_rect = pygame.Rect(int(self.body[0].x*cell_size),int(self.body[0].y*cell_size),cell_size,cell_size)
				pygame.draw.rect(screen,purple, head_rect)

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




	class FRUIT:
		def __init__(self):
			 self.randomize()

		def draw_fruit(self):
			#fruit = pygame.transform.scale(pygame.image.load('images/apple.png'),(cell_size,cell_size))
			#fruit_rect = fruit.get_rect()
			#fruit_rect.center = (cell_size*self.x, cell_size*self.y)
			#screen.blit(fruit, fruit_rect)

			pygame.draw.rect(screen,(255,0,0),pygame.Rect(cell_size*self.x,cell_size*self.y , cell_size, cell_size))
		def randomize(self):
			self.x = random.randint(0,cell_number-1)
			self.y = random.randint(0, cell_number-1)
			self.pos = Vector2(self.x, self.y)
	
	class FRUIT1:
		def __init__(self):
			 self.randomize()

		def draw_fruit1(self):
			#fruit1 = pygame.transform.scale(pygame.image.load('images/apple.png'),(cell_size,cell_size))
			#fruit1_rect = fruit1.get_rect()
			#fruit1_rect.center = (cell_size*self.x, cell_size*self.y)
			#screen.blit(fruit1, fruit1_rect)
			pygame.draw.rect(screen,(255,0,0),pygame.Rect(cell_size*self.x,cell_size*self.y , cell_size, cell_size))

		def randomize(self):
			self.x = random.randint(0,cell_number-1)
			self.y = random.randint(0, cell_number-1)
			self.pos = Vector2(self.x, self.y)


	class SCOREBOARD:
		def __init__(self,score1 ,score2 ):
			self.score1 = score1
			self.score2 = score2

			font = pygame.font.Font('Fonts/Pixeltype.ttf', 32)
			self.score1_text = font.render(f'snake {self.score1}', True, white)
			self.score1_Rect = self.score1_text.get_rect()
			self.score1_Rect.center = ( cell_size*cell_number// 5,cell_size*cell_number// 20 )

			self.score2_text = font.render(f'sneke {self.score2}', True, (163,68,115))
			self.score2_Rect = self.score2_text.get_rect()
			self.score2_Rect.center = ( cell_size*cell_number// 1.3,cell_size*cell_number// 20)
		def draw_elements(self):
			screen.blit(self.score1_text, self.score1_Rect)
			screen.blit(self.score2_text, self.score2_Rect)		


	class MAIN:
			def __init__(self):# you have to chuck in the difficulty settings and time duration settings in here too in later stages
				self.snake = SNAKE()
				self.fruit = FRUIT()
				self.fruit1 = FRUIT1()
				self.sneke = SNEKE()
				self.running = True # this is to determine whether or not the game state is active/running
				self.snake_half = False
				self.sneke_half = False
				self.snake_score = 0
				self.sneke_score = 0
			def update(self):
				self.snake.move_snake()
				self.sneke.move_sneke()
				self.check_collision()
				self.check_fail()
			def draw_elements(self):
				self.fruit.draw_fruit()
				self.fruit1.draw_fruit1()
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

				if self.fruit1.pos == self.snake.body[0]:
					# add another block to the snake
					self.snake.add_block()
					# change fruit position
					self.fruit1.randomize()
					#add 1 to the snake score
					self.snake_score += 1


				if self.fruit1.pos == self.sneke.body[0]:
					# add another block to the snake
					self.sneke.add_block()
					# change fruit position
					self.fruit1.randomize()
					# add 1 to the snake score
					self.sneke_score += 1


			def check_fail(self):
				#check is snake is ouside of screen 
				if not 0 <= self.snake.body[0].x < cell_number or not 0<= self.snake.body[0].y <cell_number:
					self.snake_half = True
					#self.sneke_half = False
					#self.snake.body = [Vector2(5,10),Vector2(4,10),Vector2(3 ,10)]
					self.snake_score = math.ceil(self.snake_score/1.15)

					
				#check is sneke is outside of screen
				if not 0 <= self.sneke.body[0].x < cell_number or not 0<= self.sneke.body[0].y <cell_number:
					#self.snake_half = False
					self.sneke_half = True
					#self.sneke.body = [Vector2(5,10),Vector2(4,10),Vector2(3 ,10)]
					self.sneke_score = math.ceil(self.sneke_score/1.15)

				# check if snake hits itself
				for block in self.snake.body[1:]:
					if self.snake.body[0] == block:
						self.snake_half = True
						#self.sneke_half = False
						#self.sneke.body = [Vector2(5,15),Vector2(4,15),Vector2(3 ,15)]
						self.snake_score = math.ceil(self.snake_score/1.15)

				# check if sneke hits itself:
				for block in self.sneke.body[1:]:
					if self.sneke.body[0] == block:
						self.snake_half = False
						#self.sneke_half = True
						#self.sneke.body = [Vector2(5,15),Vector2(4,15),Vector2(3 ,15)]
						self.sneke_score = math.ceil(self.sneke_score/1.15)


				#check if snake hits sneke 
				for block in self.sneke.body[1:]:
					if self.snake.body[0] == block:
						self.snake_half = True
						#self.sneke_half = False
						#self.snake.body = [Vector2(5,10),Vector2(4,10),Vector2(3 ,10)]
						self.snake_score = math.ceil(self.snake_score/1.15)
				#check if sneke hits snake on body
				for block in self.snake.body[1:]:
					if self.sneke.body[0] == block:
						self.snake_half = False
						#self.sneke_half = True
						#self.sneke.body = [Vector2(5,15),Vector2(4,15),Vector2(3 ,15)]
						self.sneke_score = math.ceil(self.snake_score/1.15)

				if self.snake_half == True:
					self.snake.body = [Vector2(5,10),Vector2(4,10),Vector2(3 ,10)]

				if self.sneke_half == True:
					self.sneke.body = [Vector2(5,15),Vector2(4,15),Vector2(3 ,15)]





			def game_over(self):
				self.running = False # this is to define whether or not the game is running


	main_game = MAIN()
	SCREENUPDATE = pygame.USEREVENT # this is for the clocking of the snake movement.
	#SCREEN_UPDATE is us defining an event
	pygame.time.set_timer(SCREENUPDATE,50)
	main_game.running = True


	start_time = int(pygame.time.get_ticks()/1000)
	
	while main_game.running:

		global current_time
		current_time = int(pygame.time.get_ticks()/1000)  - start_time
		time_surf = score_font.render(f'{current_time}', False, white)
		time_rect = time_surf.get_rect(center = (400, 50))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == SCREENUPDATE:
				main_game.update()

			if current_time == 120:
				main_game.running = False

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
					main_game.running = False

					
		
		
		
		global snake_score
		global sneke_score
		snake_score = main_game.snake_score
		sneke_score = main_game.sneke_score
		scoreboard = SCOREBOARD(snake_score,sneke_score)

		global snake_loss
		global sneke_loss
		sneke_loss = main_game.sneke_half
		snake_loss = main_game.snake_half
		


		screen.fill(green_grey)
		for y in range(cell_number):
		    for x in range(cell_number):
		        rect = pygame.Rect(x*cell_size, y*cell_size,cell_size,cell_size)
		        pygame.draw.rect(screen, (0,0,0), rect,1)

		main_game.draw_elements()	
		scoreboard.draw_elements()

		

		
		screen.blit(time_surf,time_rect)


		pygame.display.update()
		clock.tick(60)


	






#--------------------------TIMED--------------------------------------------GAMEOVER 3 3 3 3 3 3 3 3 3 3 3 3----------------------------------------------
def game_over_screen3():
	class TEXT:
		def __init__(self):
			font = pygame.font.Font('Fonts/Pixeltype.ttf', 75)
			global sneke_score
			global snake_score
			global snake_loss
			global sneke_loss

		#	if sneke_loss:
		#		sneke_score = math.ceil(sneke_score/2)
		#	if snake_loss: 
		#		snake_score = math.ceil(snake_score/2)


			if sneke_score > snake_score:
				sneke_loss = False
				snake_loss = True

			if sneke_score < snake_score:
				sneke_loss = True
				snake_loss = False
		
			self.goBack = pygame.transform.scale(pygame.image.load('images/back_button.png'),(0.3*29.6*cell_size,3*cell_size))
			self.goBack_Rect = self.goBack.get_rect()
			self.goBack_Rect.center = ( 5*cell_size+2*cell_size,cell_size*cell_number-5*cell_size )



			self.gameoverBackground =  pygame.transform.scale(pygame.image.load('images/gameover_screen.png'),(cell_number*cell_size,cell_number*cell_size))
			self.gameoverBackground_Rect = self.gameoverBackground.get_rect()

			self.SNAKE_score = font.render(f'{snake_score} points', True, green)
			self.SNAKE_score_Rect = self.SNAKE_score.get_rect()
			self.SNAKE_score_Rect.center = ( cell_size*cell_number// 2 - 2*cell_size,cell_size*cell_number// 3.5+12*cell_size )

			self.SNEKE_score = font.render(f'{sneke_score} points', True, green)
			self.SNEKE_score_Rect = self.SNEKE_score.get_rect()
			self.SNEKE_score_Rect.center = ( cell_size*cell_number// 2- 2*cell_size,cell_size*cell_number// 2.5+10*cell_size )

			self.winnerSnake = font.render(f'SNAKE',True, green_light)
			self.winnerSnake_Rect = self.winnerSnake.get_rect()
			self.winnerSnake_Rect.center = (length//2,length//4)

			self.winnerSneke = font.render(f'SNEKE',True, green_light)
			self.winnerSneke_Rect = self.winnerSneke.get_rect()
			self.winnerSneke_Rect.center = (length//2,length//4)

			self.draw = font.render(f'NO ONE (its a draw)',True, green_light)
			self.draw_Rect = self.draw.get_rect()
			self.draw_Rect.center = (length//2,length//4)

			self.duration = font.render(f'{current_time} seconds', True, green_light)
			self.duration_Rect = self.duration.get_rect()
			self.duration_Rect.center = (length//2 + 10*cell_size, length//2 +12*cell_size)
	
		def draw_text(self):
		
			screen.blit(self.gameoverBackground, self.gameoverBackground_Rect)
			screen.blit(self.SNAKE_score, self.SNAKE_score_Rect)
			screen.blit(self.SNEKE_score, self.SNEKE_score_Rect)
			screen.blit(self.goBack, self.goBack_Rect)
			screen.blit(self.duration, self.duration_Rect)
		
			if snake_score == sneke_score:
				screen.blit(self.draw,self.draw_Rect)
			else:	
				if sneke_loss:
					screen.blit(self.winnerSnake,self.winnerSnake_Rect)

				if snake_loss:
					screen.blit(self.winnerSneke, self.winnerSneke_Rect)

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


			if game_over.text.goBack_Rect.collidepoint(mouse_pos):
				if event.type == pygame.MOUSEBUTTONUP:
					game_over.running = False
						
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					game_over.running = False

		screen.fill(green_grey)
		for y in range(cell_number):
		    for x in range(cell_number):
		        rect = pygame.Rect(x*cell_size, y*cell_size,cell_size,cell_size)
		        pygame.draw.rect(screen, (0,0,0), rect,1)

		game_over.draw_elements()
		pygame.display.update()
		clock.tick(60)






















#--------------------------TIMED-----------------------------------------MAIN GAME  4 4 4 4 4 44  4 4 4 4------------------------------------------------
def main_game4():
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
				pygame.draw.rect(screen,white, block_rect)
				#snake_block = pygame.transform.scale(pygame.image.load('images/snake_body.png'),(cell_size,cell_size))
				#snake_block_rect = snake_block.get_rect()
				#snake_block_rect.center = (x_pos,y_pos)
				#screen.blit(snake_block, snake_block_rect)\
			head_rect = pygame.Rect(int(self.body[0].x*cell_size),int(self.body[0].y*cell_size),cell_size,cell_size)
			pygame.draw.rect(screen,green, head_rect)

			

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
				head_rect = pygame.Rect(int(self.body[0].x*cell_size),int(self.body[0].y*cell_size),cell_size,cell_size)
				pygame.draw.rect(screen,purple, head_rect)

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
			#fruit = pygame.transform.scale(pygame.image.load('images/apple.png'),(cell_size,cell_size))
			#fruit_rect = fruit.get_rect()
			#fruit_rect.center = (cell_size*self.x, cell_size*self.y)
			#screen.blit(fruit, fruit_rect)

			pygame.draw.rect(screen,(255,0,0),pygame.Rect(cell_size*self.x,cell_size*self.y , cell_size, cell_size))
		def randomize(self):
			self.x = random.randint(0,cell_number-1)
			self.y = random.randint(0, cell_number-1)
			self.pos = Vector2(self.x, self.y)
	
	class FRUIT1:
		def __init__(self):
			 self.randomize()

		def draw_fruit1(self):
			#fruit1 = pygame.transform.scale(pygame.image.load('images/apple.png'),(cell_size,cell_size))
			#fruit1_rect = fruit1.get_rect()
			#fruit1_rect.center = (cell_size*self.x, cell_size*self.y)
			#screen.blit(fruit1, fruit1_rect)
			pygame.draw.rect(screen,(255,0,0),pygame.Rect(cell_size*self.x,cell_size*self.y , cell_size, cell_size))

		def randomize(self):
			self.x = random.randint(0,cell_number-1)
			self.y = random.randint(0, cell_number-1)
			self.pos = Vector2(self.x, self.y)


	class SCOREBOARD:
		def __init__(self,score1 ,score2 ):
			self.score1 = score1
			self.score2 = score2

			font = pygame.font.Font('Fonts/Pixeltype.ttf', 32)
			self.score1_text = font.render(f'snake {self.score1}', True, white)
			self.score1_Rect = self.score1_text.get_rect()
			self.score1_Rect.center = ( cell_size*cell_number// 5,cell_size*cell_number// 20 )

			self.score2_text = font.render(f'sneke {self.score2}', True, (163,68,115))
			self.score2_Rect = self.score2_text.get_rect()
			self.score2_Rect.center = ( cell_size*cell_number// 1.3,cell_size*cell_number// 20)
		def draw_elements(self):
			screen.blit(self.score1_text, self.score1_Rect)
			screen.blit(self.score2_text, self.score2_Rect)		


	class MAIN:
			def __init__(self):# you have to chuck in the difficulty settings and time duration settings in here too in later stages
				self.snake = SNAKE()
				self.fruit = FRUIT()
				self.fruit1 = FRUIT1()
				self.sneke = SNEKE()
				self.running = True # this is to determine whether or not the game state is active/running
				self.snake_half = False
				self.sneke_half = False
				self.snake_score = 0
				self.sneke_score = 0
			def update(self):
				self.snake.move_snake()
				self.sneke.move_sneke()
				self.check_collision()
				self.check_fail()
			def draw_elements(self):
				self.fruit.draw_fruit()
				self.fruit1.draw_fruit1()
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

				if self.fruit1.pos == self.snake.body[0]:
					# add another block to the snake
					self.snake.add_block()
					# change fruit position
					self.fruit1.randomize()
					#add 1 to the snake score
					self.snake_score += 1


				if self.fruit1.pos == self.sneke.body[0]:
					# add another block to the snake
					self.sneke.add_block()
					# change fruit position
					self.fruit1.randomize()
					# add 1 to the snake score
					self.sneke_score += 1


			def check_fail(self):
				#check is snake is ouside of screen 
				if not 0 <= self.snake.body[0].x < cell_number or not 0<= self.snake.body[0].y <cell_number:
					self.snake_half = True
					self.sneke_half = False
					self.snake.body = [Vector2(5,10),Vector2(4,10),Vector2(3 ,10)]
					self.snake_score = math.ceil(self.snake_score/1.15)

					
				#check is sneke is outside of screen
				if not 0 <= self.sneke.body[0].x < cell_number or not 0<= self.sneke.body[0].y <cell_number:
					self.snake_half = False
					self.sneke_half = True
					self.sneke.body = [Vector2(5,10),Vector2(4,10),Vector2(3 ,10)]
					self.sneke_score = math.ceil(self.sneke_score/1.15)

				# check if snake hits itself
				for block in self.snake.body[1:]:
					if self.snake.body[0] == block:
						self.snake_half = True
						self.sneke_half = False
						self.sneke.body = [Vector2(5,15),Vector2(4,15),Vector2(3 ,15)]
						self.snake_score = math.ceil(self.snake_score/1.15)

				# check if sneke hits itself:
				for block in self.sneke.body[1:]:
					if self.sneke.body[0] == block:
						self.snake_half = False
						self.sneke_half = True
						self.sneke.body = [Vector2(5,15),Vector2(4,15),Vector2(3 ,15)]
						self.sneke_score = math.ceil(self.sneke_score/1.15)


				#check if snake hits sneke 
				for block in self.sneke.body[1:]:
					if self.snake.body[0] == block:
						self.snake_half = True
						self.sneke_half = False
						self.snake.body = [Vector2(5,10),Vector2(4,10),Vector2(3 ,10)]
						self.snake_score = math.ceil(self.snake_score/1.15)
				#check if sneke hits snake on body
				for block in self.snake.body[1:]:
					if self.sneke.body[0] == block:
						self.snake_half = False
						self.sneke_half = True
						self.sneke.body = [Vector2(5,15),Vector2(4,15),Vector2(3 ,15)]
						self.sneke_score = math.ceil(self.snake_score/1.15)



			def game_over(self):
				self.running = False # this is to define whether or not the game is running


	main_game = MAIN()
	SCREENUPDATE = pygame.USEREVENT # this is for the clocking of the snake movement.
	#SCREEN_UPDATE is us defining an event
	pygame.time.set_timer(SCREENUPDATE,70)
	main_game.running = True


	start_time = int(pygame.time.get_ticks()/1000)
	
	while main_game.running:

		global current_time
		current_time = int(pygame.time.get_ticks()/1000)  - start_time
		time_surf = score_font.render(f'{current_time}', False, white)
		time_rect = time_surf.get_rect(center = (400, 50))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == SCREENUPDATE:
				main_game.update()

			if current_time == 120:
				main_game.running = False

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
					main_game.running = False

					
		
		
		
		global snake_score
		global sneke_score
		snake_score = main_game.snake_score
		sneke_score = main_game.sneke_score
		scoreboard = SCOREBOARD(snake_score,sneke_score)

		global snake_loss
		global sneke_loss
		sneke_loss = main_game.sneke_half
		snake_loss = main_game.snake_half
		


		screen.fill(green_grey)
		for y in range(cell_number):
		    for x in range(cell_number):
		        rect = pygame.Rect(x*cell_size, y*cell_size,cell_size,cell_size)
		        pygame.draw.rect(screen, (0,0,0), rect,1)

		main_game.draw_elements()	
		scoreboard.draw_elements()

		

		
		screen.blit(time_surf,time_rect)


		pygame.display.update()
		clock.tick(60)


	




#---------------------------TIMED-------------------------------------------GAMEOVER 4 4 4 4 4 4 4 4 4 44 ----------------------------------------------
def game_over_screen4():
	class TEXT:
		def __init__(self):
			font = pygame.font.Font('Fonts/Pixeltype.ttf', 75)
			global sneke_score
			global snake_score
			global snake_loss
			global sneke_loss

			'''if sneke_loss:
				sneke_score = math.ceil(sneke_score/2)
			if snake_loss: 
				snake_score = math.ceil(snake_score/2)
			'''

			if sneke_score > snake_score:
				sneke_loss = False
				snake_loss = True

			if sneke_score < snake_score:
				sneke_loss = True
				snake_loss = False
		
			self.goBack = pygame.transform.scale(pygame.image.load('images/back_button.png'),(0.3*29.6*cell_size,3*cell_size))
			self.goBack_Rect = self.goBack.get_rect()
			self.goBack_Rect.center = ( 5*cell_size+2*cell_size,cell_size*cell_number-5*cell_size )



			self.gameoverBackground =  pygame.transform.scale(pygame.image.load('images/gameover_screen.png'),(cell_number*cell_size,cell_number*cell_size))
			self.gameoverBackground_Rect = self.gameoverBackground.get_rect()

			self.SNAKE_score = font.render(f'{snake_score} points', True, green)
			self.SNAKE_score_Rect = self.SNAKE_score.get_rect()
			self.SNAKE_score_Rect.center = ( cell_size*cell_number// 2 - 2*cell_size,cell_size*cell_number// 3.5+12*cell_size )

			self.SNEKE_score = font.render(f'{sneke_score} points', True, green)
			self.SNEKE_score_Rect = self.SNEKE_score.get_rect()
			self.SNEKE_score_Rect.center = ( cell_size*cell_number// 2- 2*cell_size,cell_size*cell_number// 2.5+10*cell_size )

			self.winnerSnake = font.render(f'SNAKE',True, green_light)
			self.winnerSnake_Rect = self.winnerSnake.get_rect()
			self.winnerSnake_Rect.center = (length//2,length//4)

			self.winnerSneke = font.render(f'SNEKE',True, green_light)
			self.winnerSneke_Rect = self.winnerSneke.get_rect()
			self.winnerSneke_Rect.center = (length//2,length//4)

			self.draw = font.render(f'NO ONE (its a draw)',True, green_light)
			self.draw_Rect = self.draw.get_rect()
			self.draw_Rect.center = (length//2,length//4)

			self.duration = font.render(f'{current_time} seconds', True, green_light)
			self.duration_Rect = self.duration.get_rect()
			self.duration_Rect.center = (length//2 + 10*cell_size, length//2 +12*cell_size)
	
		def draw_text(self):
		
			screen.blit(self.gameoverBackground, self.gameoverBackground_Rect)
			screen.blit(self.SNAKE_score, self.SNAKE_score_Rect)
			screen.blit(self.SNEKE_score, self.SNEKE_score_Rect)
			screen.blit(self.goBack, self.goBack_Rect)
			screen.blit(self.duration, self.duration_Rect)
		
			if snake_score == sneke_score:
				screen.blit(self.draw,self.draw_Rect)
			else:	
				if sneke_loss:
					screen.blit(self.winnerSnake,self.winnerSnake_Rect)

				if snake_loss:
					screen.blit(self.winnerSneke, self.winnerSneke_Rect)

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


			if game_over.text.goBack_Rect.collidepoint(mouse_pos):
				if event.type == pygame.MOUSEBUTTONUP:
					game_over.running = False
						
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					game_over.running = False

		screen.fill(green_grey)
		for y in range(cell_number):
		    for x in range(cell_number):
		        rect = pygame.Rect(x*cell_size, y*cell_size,cell_size,cell_size)
		        pygame.draw.rect(screen, (0,0,0), rect,1)

		game_over.draw_elements()
		pygame.display.update()
		clock.tick(60)

#----------------------------------------------------------------------------SINGLE PLAYER classic---------------------------------------------------------------------#

def main_game5():
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
				pygame.draw.rect(screen,white, block_rect)
				#snake_block = pygame.transform.scale(pygame.image.load('images/snake_body.png'),(cell_size,cell_size))
				#snake_block_rect = snake_block.get_rect()
				#snake_block_rect.center = (x_pos,y_pos)
				#screen.blit(snake_block, snake_block_rect)\
			head_rect = pygame.Rect(int(self.body[0].x*cell_size),int(self.body[0].y*cell_size),cell_size,cell_size)
			pygame.draw.rect(screen,green, head_rect)

			

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



	class FRUIT:
		def __init__(self):
			 self.randomize()

		def draw_fruit(self):
			#fruit = pygame.transform.scale(pygame.image.load('images/apple.png'),(cell_size,cell_size))
			#fruit_rect = fruit.get_rect()
			#fruit_rect.center = (cell_size*self.x, cell_size*self.y)
			#screen.blit(fruit, fruit_rect)

			pygame.draw.rect(screen,(255,0,0),pygame.Rect(cell_size*self.x,cell_size*self.y , cell_size, cell_size))
		def randomize(self):
			self.x = random.randint(0,cell_number-1)
			self.y = random.randint(0, cell_number-1)
			self.pos = Vector2(self.x, self.y)
	
	class FRUIT1:
		def __init__(self):
			 self.randomize()

		def draw_fruit1(self):
			#fruit1 = pygame.transform.scale(pygame.image.load('images/apple.png'),(cell_size,cell_size))
			#fruit1_rect = fruit1.get_rect()
			#fruit1_rect.center = (cell_size*self.x, cell_size*self.y)
			#screen.blit(fruit1, fruit1_rect)
			pygame.draw.rect(screen,(255,0,0),pygame.Rect(cell_size*self.x,cell_size*self.y , cell_size, cell_size))

		def randomize(self):
			self.x = random.randint(0,cell_number-1)
			self.y = random.randint(0, cell_number-1)
			self.pos = Vector2(self.x, self.y)


	class SCOREBOARD:
		def __init__(self,score1 ):
			self.score1 = score1
	

			font = pygame.font.Font('Fonts/Pixeltype.ttf', 32)
			self.score1_text = font.render(f'snake {self.score1}', True, white)
			self.score1_Rect = self.score1_text.get_rect()
			self.score1_Rect.center = ( cell_size*cell_number// 5,cell_size*cell_number// 20 )

	
		def draw_elements(self):
			screen.blit(self.score1_text, self.score1_Rect)
			


	class MAIN:
			def __init__(self):# you have to chuck in the difficulty settings and time duration settings in here too in later stages
				self.snake = SNAKE()
				self.fruit = FRUIT()
				self.fruit1 = FRUIT1()

				self.running = True # this is to determine whether or not the game state is active/running
				self.snake_half = False
				self.sneke_half = False
				self.snake_score = 0
				self.sneke_score = 0
			def update(self):
				self.snake.move_snake()

				self.check_collision()
				self.check_fail()
			def draw_elements(self):
				self.fruit.draw_fruit()
				self.fruit1.draw_fruit1()
				self.snake.draw_snake()

			def check_collision(self):
				if self.fruit.pos == self.snake.body[0]:
					# add another block to the snake
					self.snake.add_block()
					# change fruit position
					self.fruit.randomize()
					#add 1 to the snake score
					self.snake_score += 1


			

				if self.fruit1.pos == self.snake.body[0]:
					# add another block to the snake
					self.snake.add_block()
					# change fruit position
					self.fruit1.randomize()
					#add 1 to the snake score
					self.snake_score += 1



			def check_fail(self):
				#check is snake is ouside of screen 
				if not 0 <= self.snake.body[0].x < cell_number or not 0<= self.snake.body[0].y <cell_number:
					self.snake_half = True
			

				# check if snake hits itself
				for block in self.snake.body[1:]:
					if self.snake.body[0] == block:
						self.snake_half = True





			def game_over(self):
				self.running = False # this is to define whether or not the game is running


	main_game = MAIN()
	SCREENUPDATE = pygame.USEREVENT # this is for the clocking of the snake movement.
	#SCREEN_UPDATE is us defining an event
	pygame.time.set_timer(SCREENUPDATE,70)
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

				if event.key == pygame.K_ESCAPE: # so it continues with the main loop
					main_game.running = False

			if main_game.snake_half:
				main_game.running = False
					
		
		
		global snake_score
		snake_score = main_game.snake_score
		scoreboard = SCOREBOARD(snake_score)
		


		screen.fill(green_grey)
		for y in range(cell_number):
		    for x in range(cell_number):
		        rect = pygame.Rect(x*cell_size, y*cell_size,cell_size,cell_size)
		        pygame.draw.rect(screen, (0,0,0), rect,1)

		main_game.draw_elements()	
		scoreboard.draw_elements()

		

		


		pygame.display.update()
		clock.tick(60)


#----------------------------------------------------------------------------GAME OVER SCREEN 5---------------------------------------------------------------------#
def game_over_screen5():
	class TEXT:
		def __init__(self):
			font = pygame.font.Font('Fonts/Pixeltype.ttf', 120)



			self.goBack = pygame.transform.scale(pygame.image.load('images/back_2_button.png'),(0.3*29.6*cell_size,3*cell_size))
			self.goBack_Rect = self.goBack.get_rect()
			self.goBack_Rect.center = ( 6*cell_size,cell_size*cell_number-3*cell_size )


			self.score = pygame.transform.scale(pygame.image.load('images/your_score.png'),(length,length))
			self.score_Rect = self.score.get_rect()


			self.SNAKE_score = font.render(f'{snake_score}', True, green)
			self.SNAKE_score_Rect = self.SNAKE_score.get_rect()
			self.SNAKE_score_Rect.center = ( length//2,length//2 )
		






		def draw_text(self):
			screen.blit(self.score, self.score_Rect)
			screen.blit(self.SNAKE_score,self.SNAKE_score_Rect)
			screen.blit(self.goBack,self.goBack_Rect)
		
			


	class RULES:
		def __init__(self):
			self.running = True
			self.text = TEXT()
		def draw_elements(self):
			self.text.draw_text()

	rules = RULES()
	while rules.running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			mouse_pos = pygame.mouse.get_pos()
			if rules.text.goBack_Rect.collidepoint(mouse_pos):
				if event.type == pygame.MOUSEBUTTONUP:
					rules.running = False


			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					rules.running = False

		screen.fill(green_grey)
		for y in range(cell_number):
		    for x in range(cell_number):
		        rect = pygame.Rect(x*cell_size, y*cell_size,cell_size,cell_size)
		        pygame.draw.rect(screen, (0,0,0), rect,1)

		rules.draw_elements()
		pygame.display.update()
		clock.tick(60)




















#----------------------------------------------------------------------------RULE SCREEN---------------------------------------------------------------------#
def rule_screen():
	class TEXT:
		def __init__(self):
			font = pygame.font.Font('Fonts/Pixeltype.ttf', 32)



			self.goBack = pygame.transform.scale(pygame.image.load('images/back_2_button.png'),(0.3*29.6*cell_size,3*cell_size))
			self.goBack_Rect = self.goBack.get_rect()
			self.goBack_Rect.center = ( 6*cell_size,cell_size*cell_number-3*cell_size )


			self.more = pygame.transform.scale(pygame.image.load('images/more_button.png'),(0.3*29.6*cell_size,3*cell_size))
			self.more_Rect = self.more.get_rect()
			self.more_Rect.center = ( 18*cell_size,cell_size*cell_number-3*cell_size )



			self.rules = pygame.transform.scale(pygame.image.load('images/rules_page.png'),(cell_size*cell_number,cell_size*cell_number))
			self.rules_Rect = self.rules.get_rect()



		def draw_text(self):
			screen.blit(self.rules, self.rules_Rect)
			screen.blit(self.goBack,self.goBack_Rect)
			screen.blit(self.more, self.more_Rect)


	class RULES:
		def __init__(self):
			self.running = True
			self.text = TEXT()
		def draw_elements(self):
			self.text.draw_text()

	rules = RULES()
	while rules.running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			mouse_pos = pygame.mouse.get_pos()
			if rules.text.goBack_Rect.collidepoint(mouse_pos):
				if event.type == pygame.MOUSEBUTTONUP:
					rules.running = False

			if rules.text.more_Rect.collidepoint(mouse_pos):
				if event.type == pygame.MOUSEBUTTONUP:
					rule_screen1()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					rules.running = False

		screen.fill(green_grey)
		for y in range(cell_number):
		    for x in range(cell_number):
		        rect = pygame.Rect(x*cell_size, y*cell_size,cell_size,cell_size)
		        pygame.draw.rect(screen, (0,0,0), rect,1)

		rules.draw_elements()
		pygame.display.update()
		clock.tick(60)

def rule_screen1():
	class TEXT:
		def __init__(self):
			font = pygame.font.Font('Fonts/Pixeltype.ttf', 32)



			self.goBack = pygame.transform.scale(pygame.image.load('images/back_2_button.png'),(0.3*29.6*cell_size,3*cell_size))
			self.goBack_Rect = self.goBack.get_rect()
			self.goBack_Rect.center = ( 6*cell_size,3*cell_size )






			self.rules = pygame.transform.scale(pygame.image.load('images/rule_page_2.png'),(cell_size*cell_number,cell_size*cell_number))
			self.rules_Rect = self.rules.get_rect()



		def draw_text(self):
			screen.blit(self.rules, self.rules_Rect)
			screen.blit(self.goBack,self.goBack_Rect)
			pygame.draw.rect(screen, (54,119,122), pygame.Rect(0, length - 16*cell_size - 2, 350, 130))


	class RULES:
		def __init__(self):
			self.running = True
			self.text = TEXT()
		def draw_elements(self):
			self.text.draw_text()

	rules = RULES()
	while rules.running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			mouse_pos = pygame.mouse.get_pos()
			if rules.text.goBack_Rect.collidepoint(mouse_pos):
				if event.type == pygame.MOUSEBUTTONUP:
					rules.running = False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					rules.running = False

		screen.fill(green_grey)
		for y in range(cell_number):
		    for x in range(cell_number):
		        rect = pygame.Rect(x*cell_size, y*cell_size,cell_size,cell_size)
		        pygame.draw.rect(screen, (0,0,0), rect,1)

		rules.draw_elements()
		pygame.display.update()
		clock.tick(60)




main_menu()
