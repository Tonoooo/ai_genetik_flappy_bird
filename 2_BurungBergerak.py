import pygame
import neat
import time
import os
import random # ini untuk tinggi rendah pipa

WIN_WIDTH = 500 # LEBAR
WIN_HEIGHT = 800 # TINGGI
BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("bird1.png"))),pygame.transform.scale2x(pygame.image.load(os.path.join("bird2.png"))),pygame.transform.scale2x(pygame.image.load(os.path.join("bird3.png")))]
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("pipe.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("base.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("bg.png")))

# membuat class burung
class Bird:
    IMGS = BIRD_IMGS
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.tilt = 0  # derajat untuk dimiringkan
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]

    def jump(self):
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y

    def move(self):
        self.tick_count += 1
        # menghitung perpindahan ini akan menjadi berapa pixel yang bergerak naik/turun dibingkai
        d = self.vel*self.tick_count + 1.5*self.tick_count**2 # kecepatan burung kita saat ini kita berferak keatas/bawah
        if d >= 16: # jika burung nya turun 16 piksel maka turunkan saja
            d = 16
        if d < 0 : # jika kita keatas mari kita naik sedikit dan ini hanya menyesuaikan gerakan
            d -= 2
        self.y = self.y + d
        if d < 0 or self.y < self.height + 50: # kita akan memiringkan burung keatas
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL

    def draw(self, win): # win = windows/bingkai
        self.img_count += 1
        ## ini untuk animasi mengepakkan sayap
        if self.img_count < self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count < self.ANIMATION_TIME*2:
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME*3:
            self.img = self.IMGS[2]
        elif self.img_count < self.ANIMATION_TIME*4:
            self.img = self.IMGS[1]
        elif self.img_count == self.ANIMATION_TIME*4 + 1:
            self.img = self.IMGS[0]
            self.img_count = 0
        # jadi ini adalah kita sedang memeriksa gambar apa yang harus kita tampilkan berdasarkan jumlah gambat saat ini,
        # jadi jika jumlah gambar kurang dari 5 yang merupakan ANIMATION_TIME, maka kita akan menampilkan burung bg1.
        # jika ANIMATION_TIME jika lebih besar maka ke elif berikutnya, jika kutang dari 10 maka menampilkan gambar
        # butung bg2, dan terus begitu

        ## sekarang ketika burung miring 90 derajat kebawah kita tidak ingin mengepakkan sayap burung,
        # dan kita akan mengubah gambarnya
        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME*2

        ## sekarang kita perlu memutarnya gambarnya
        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_image.get_rect(center=self.img.get_rect(topleft = (self.x, self.y)).center)
        win.blit(rotated_image, new_rect.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)    

## ini akan menggambarkan latarblkg dan burung
def draw_window(win,bird):
    win.blit(BG_IMG , (0,0)) # bilt itu seperti menggambarkan, (0,0) = posisi gambarnya
    bird.draw(win)
    pygame.display.update()

## ini akan menjadi main function, ini akan menjalankan loop utama
def main():
    bird = Bird(200,200)
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()

    run = True
    # ini akan melacak setiap kali sesuatu terjadi seperti mengklik mouse, / sesuatu
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # jadi ketika mengklik X dipojok kanan atas bingkai pygame, maka kita akan berhenti
                pygame.quit()
                run = False
        bird.move()
        draw_window(win,bird)
    pygame.quit()
    quit()
main()