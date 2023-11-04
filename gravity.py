#!/usr/bin/env python
import pygame
import math
import time

pygame.init()
size=(1024,768)
screen=pygame.display.set_mode(size)
background = pygame.Surface(screen.get_size())
pygame.display.set_caption("PyGravity")
pygame.key.set_repeat(10, 30)

#print pygame.font.get_fonts()
#Define Colors
black	= (0,0,0)
white	= (255,255,255)
green	= (0,255,0)
red	= (255,0,0)
grey	= (128,128,128)
blue	= (0,0,255)
yellow	= (255,255,0)
violet	= (255,0,255)
darkblue = (0,0,33)
G	= 6.67*10**(-11)
done=False

clock=pygame.time.Clock()
try:
	joystick = pygame.joystick.Joystick(0)
	joystick.init()
except:
	pass

def winscreen(winner):
	wonfont = pygame.font.Font(None,35)
#	wonfont.set_bold()
	text = winner + " has won"
	playerwon = wonfont.render(text,True,red)
	background.blit(playerwon, (size[0]/2-50,size[1]/2))
def makeworld(level):
	if level ==1:
		list_of_planets = [Planet([600,400],50),Planet([200,400],80),Planet([400,250],100)]
		player = canon("player",[50,100],40)
		player2 = canon("player2",[700,200],40)
		list_of_players = player,player2
	elif level == 2:
		list_of_planets = [Star([size[0]/2,size[1]/2],100),]
		player = canon("player",[50,100],40)
		player2 = canon("player2",[700,200],40)
		list_of_players = player,player2
	return list_of_planets,list_of_players
class canon(pygame.sprite.Sprite):
	def __init__(self,id,position,basesize):
		pygame.sprite.Sprite.__init__(self)
		self.id = id
		self.image = pygame.Surface([10,10])
		self.dead=0
		self.image.fill(red)
		self.angle=0.0*math.pi
		if position[0] > size[0]/2:
			self.angle=1*math.pi
		self.v0 = 20
		self.locfcenterpol = self.angle
		self.locfcenter = pol2kart(self.angle,basesize/2)
		self.position = position[0]+self.locfcenter[0],position[1]+self.locfcenter[1]
		self.rect = self.image.get_rect()
		self.player = self
		self.rect.center = self.position
		self.list_of_bullets = list()
		self.base = Planet(position,basesize)
		list_of_players_planets.append(self.base)
	def turnleft(self):
		self.angle += 0.0125*math.pi
	def turnright(self):
		self.angle -= 0.0125*math.pi
	def faster(self):
		if self.v0<25:
			self.v0 *= 1.025
	def slower(self):
		self.v0 /= 1.025
	def moveleft(self):
		self.locfcenterpol += 0.05*math.pi
		self.angle += 0.05*math.pi
	def moveright(self):
		self.locfcenterpol -= 0.05*math.pi
		self.angle -= 0.05*math.pi
	def update(self):
		self.locfcenter = pol2kart(self.locfcenterpol,self.base.radius)
		self.position = self.base.position[0]+self.locfcenter[0], self.base.position[1]+self.locfcenter[1]
		self.rect.center = self.position
		self.drawcanon()
		self.drawpreview ( )
	def drawcanon(self):
		self.rohr = pygame.Surface([100,100])
		self.dx, self.dy = pol2kart(self.angle,20)
		self.rohrrect = pygame.draw.line(self.rohr,red,[50,50],[self.dx+50,self.dy+50])
		self.rohr.set_colorkey((0,0,0))
		self.rohr.convert_alpha()
		background.blit(self.rohr,[self.position[0]-50,self.position[1]-50])
	def drawpreview ( self ):
		self.snapshot = pygame.Surface ( [3, 3] )
		self.snapshot.fill ( (96, 96, 96) )
		pos, v = self.position , pol2kart ( self.angle, self.v0 )
		for i in range ( 25 ):
			pos, v = gravity ( pos, v, mass = 1, delta_t = 1 )
			background.blit ( self.snapshot, pos )
	def kill(self):
		self.remove(players)
		self.dead=1
	def shoot(self):
		if self.dead == 0:
			bullets.add ( Bullet ( self.player, self.position, self.angle, self.v0 ) )

def drawenvironment():
	background.fill(darkblue)

def pol2kart(angle,v):
	x = v * math.cos(angle)
	y = -v * math.sin(angle)
	return x,y

def gravity ( pos = [0, 0], speed = [0, 0], mass = 1, delta_t = 1 ):
	pos = (pos[0] + speed[0] * delta_t, pos[1] + speed[1] * delta_t)
	f = [0,0]
	for m in list_of_masses:
		dist = math.sqrt ( ( m[0] - pos[0] )**2 + ( m[1] - pos[1] )**2 )
		f[0] += m[2] * mass * G * ( m[0] - pos[0] ) / dist**3
		f[1] += m[2] * mass * G * ( m[1] - pos[1] ) / dist**3
	speed = (speed[0] + delta_t * f[0] / mass, speed[1] + delta_t * f[1] / mass)
	return pos, speed

class Bullet(pygame.sprite.Sprite):
	def __init__(self,playername,position,angle,v0):
		#self.canonid=canonid
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([5,5])
		if playername == list_of_players[0]:
			self.color = violet
		elif playername == list_of_players[1]:
			self.color = yellow
		self.rect = pygame.draw.circle(self.image,self.color,[3,3],2)
		self.rect.center = position
		self.position = position
		self.image.set_colorkey((0,0,0))
		self.image.convert_alpha()
		self.v = list(pol2kart(angle,v0))
		self.mass = 0.1
	def update(self,masses = list()):
		self.position, self.v = gravity ( self.position, self.v, self.mass, delta_t = 1 )
		self.rect.center = self.position
		if abs(self.rect.center[0]) > 5000 or abs(self.rect.center[1]) > 5000:
			self.kill()

	def blit(self):
		background.blit(self.image, self.rect)
	def kill(self):
		self.remove(bullets)
		explosions.add(Explosion(self.position))

class Planet(pygame.sprite.Sprite):
	def __init__(self,position,size):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([size,size])
		self.rect = pygame.draw.circle(self.image,blue,[int(size/2),int(size/2)],int(size/2))
		self.rect.center = position
		self.radius=size/2
		self.position = position
		self.mass = 10**9*size**3
		self.image.set_colorkey((0,0,0))
		self.image.convert_alpha()
	def update(self):
		background.blit(self.image, self.rect)

class Star(Planet):
	def __init__(self,position,size):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([size,size])
		self.rect = pygame.draw.circle(self.image,yellow,[int(size/2),int(size/2)],int(size/2))
		self.rect.center = position
		self.radius=size/2
		self.position = position
		self.mass = 10**9*size**3*2
		self.image.set_colorkey((0,0,0))
		self.image.convert_alpha()

class Explosion(pygame.sprite.Sprite):
	def __init__(self,position):
		self.size = 30
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([self.size,self.size])
		self.image.set_colorkey((0,0,0))
		self.image.convert_alpha()
		self.rect = pygame.draw.circle(self.image,red,[self.size/2,self.size/2],self.size/2)
		self.ttl = 5
		self.position = position
		self.rect.center = self.position
	def update(self):
		self.ttl-=1
		if self.ttl == 0:
			self.kill()

###
list_of_players_planets = list()
list_of_planets,list_of_players = makeworld(1)
list_of_planets = list_of_planets + list_of_players_planets
players = pygame.sprite.Group()
for p in list_of_players:
	players.add(p)
explosions = pygame.sprite.Group()
bullets = pygame.sprite.Group()
while done == False:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done=True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				done = True
			if event.key == pygame.K_SPACE:
				list_of_players[0].shoot()
			elif event.key == pygame.K_UP:
				list_of_players[0].turnleft()
			elif event.key == pygame.K_DOWN:
				list_of_players[0].turnright()
			elif event.key == pygame.K_LEFT:
				list_of_players[0].moveleft()
			elif event.key == pygame.K_RIGHT:
				list_of_players[0].moveright()
			elif event.key == pygame.K_PLUS:
				list_of_players[0].faster ( )
			elif event.key == pygame.K_MINUS:
				list_of_players[0].slower ( )
			else: print event.key
		elif event.type == pygame.JOYHATMOTION:
			if event.value == (1,0):
				list_of_players[1].moveright()
			elif event.value == (-1,0):
				list_of_players[1].moveleft()
			elif event.value == (0,1):
				list_of_players[1].turnleft()
			elif event.value == (0,-1):
				list_of_players[1].turnright()
		elif event.type == pygame.JOYBUTTONDOWN:
			list_of_players[1].shoot()
	list_of_masses = list()
	for p in list_of_planets:
		list_of_masses.append([p.position[0],p.position[1],p.mass])
	bullets.update(list_of_masses)
	explosions.update()
	drawenvironment()
	for epl in explosions:
		pygame.sprite.spritecollide(epl, players, True, pygame.sprite.collide_circle)
	for p in list_of_planets:
		pygame.sprite.spritecollide(p, bullets, True, pygame.sprite.collide_circle)
		p.update()
	players.update()
	players.draw(background)
	bullets.draw(background)
	explosions.draw(background)
	if len(players) == 1:
		done = True
		winscreen(players.sprites()[0].id)
	screen.blit(background, (0,0))
	clock.tick(20)
	pygame.display.flip()
	if done == True:
		time.sleep(1)
