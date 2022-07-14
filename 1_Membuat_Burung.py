import pygame
import neat
import time
import os
import random # ini untuk tinggi rendah pipa

# mengatur tinggi rendahnya jendela/screen/bingkai
WIN_WIDTH = 600 # LEBAR
WIN_HEIGHT = 800 # TINGGI

# Memuat gambar burung,  ukuran gambarnya jadi 2x lipat, kita pake list karna ada 3 gambar burung
BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join( "bird1.png"))),pygame.transform.scale2x(pygame.image.load(os.path.join( "bird2.png"))),pygame.transform.scale2x(pygame.image.load(os.path.join( "bird3.png")))]
# memuat gambat pipa
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join( "pipe.png")))
# memuat gambar base/ bawah
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join( "base.png")))
# memuat gambat latar belakang
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join( "bg.png")))

# membuat class burung
class Bird:
    IMGS = BIRD_IMGS # gambar bung
    MAX_ROTATION = 25 # maximal rotasi
    ROT_VEL = 20 # rotasi kecepatan
    ANIMATION_TIME = 5 # ini berapa lama kita akan menampilkan setiap animasi burung dan dengan mengubah dgn yng lebih besar/kecil

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.tilt = 0  # derajat untuk dimiringkan
        self.tick_count = 0
        self.vel = 0 # kecepatan
        self.height = self.y # tinggi
        self.img_count = 0
        self.img = self.IMGS[0] # gambar burung pertama

    def jump(self):
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y

