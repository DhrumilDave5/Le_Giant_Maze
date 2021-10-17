import pygame
import Game_Files.Settings as Settings


class Player:

    def __init__(self, spawn_mu, colour, maze,
                 up_key, down_key, right_key, left_key):

        mus = Settings.mu_size_pv

        self.rect = pygame.Rect(0, 0, Settings.p_size, Settings.p_size)
        self.rect.x += (spawn_mu[0] * mus) + (((mus - Settings.p_size) // 2) // Settings.lq) * Settings.lq
        self.rect.y += (spawn_mu[1] * mus) + (((mus - Settings.p_size) // 2) // Settings.lq) * Settings.lq

        self.maze = maze
        self.vel = Settings.p_vel
        self.won = False

        self.x_tlmu = self.rect.topleft[0] // mus
        self.y_tlmu = self.rect.topleft[1] // mus
        self.x_trmu = (self.rect.topright[0] - self.vel) // mus
        self.y_trmu = self.rect.topright[1] // mus
        self.x_blmu = self.rect.bottomleft[0] // mus
        self.y_blmu = (self.rect.bottomleft[1] - self.vel) // mus
        self.x_brmu = (self.rect.bottomright[0] - self.vel) // mus
        self.y_brmu = (self.rect.bottomright[1] - self.vel) // mus
        self.x_cmu = self.rect.centerx // mus
        self.y_cmu = self.rect.centery // mus

        self.colour = colour
        self.up_key = up_key
        self.down_key = down_key
        self.right_key = right_key
        self.left_key = left_key

    def update_mu_stuff(self):

        mus = Settings.mu_size_pv

        self.x_tlmu = self.rect.topleft[0] // mus
        self.y_tlmu = self.rect.topleft[1] // mus
        self.x_trmu = (self.rect.topright[0] - self.vel) // mus
        self.y_trmu = self.rect.topright[1] // mus
        self.x_blmu = self.rect.bottomleft[0] // mus
        self.y_blmu = (self.rect.bottomleft[1] - self.vel) // mus
        self.x_brmu = (self.rect.bottomright[0] - self.vel) // mus
        self.y_brmu = (self.rect.bottomright[1] - self.vel) // mus
        self.x_cmu = self.rect.centerx // mus
        self.y_cmu = self.rect.centery // mus

    def move_up(self):
        self.rect.y -= self.vel
        self.update_mu_stuff()

    def move_down(self):
        self.rect.y += self.vel
        self.update_mu_stuff()

    def move_right(self):
        self.rect.x += self.vel
        self.update_mu_stuff()

    def move_left(self):
        self.rect.x -= self.vel
        self.update_mu_stuff()

    def collide_up(self):
        if self.maze.map[self.y_tlmu][self.x_tlmu] == Settings.filled_mu_digit or \
                self.maze.map[self.y_trmu][self.x_trmu] == Settings.filled_mu_digit:
            self.move_down()

    def collide_down(self):
        if self.maze.map[self.y_blmu][self.x_blmu] == Settings.filled_mu_digit or \
                self.maze.map[self.y_brmu][self.x_brmu] == Settings.filled_mu_digit:
            self.move_up()

    def collide_right(self):
        if self.maze.map[self.y_trmu][self.x_trmu] == Settings.filled_mu_digit or \
                self.maze.map[self.y_brmu][self.x_brmu] == Settings.filled_mu_digit:
            self.move_left()

    def collide_left(self):
        if self.maze.map[self.y_tlmu][self.x_tlmu] == Settings.filled_mu_digit or \
                self.maze.map[self.y_blmu][self.x_blmu] == Settings.filled_mu_digit:
            self.move_right()

    def movement(self, key_list):

        def check_win():
            if not self.won:
                if self.maze.map[self.y_tlmu][self.x_tlmu] == Settings.win_area_mu_digit:
                    self.won = True
                    self.maze.map[27][80] = Settings.filled_mu_digit

        self.update_mu_stuff()

        if key_list[self.up_key]:
            self.move_up(), self.collide_up()

        if key_list[self.down_key]:
            self.move_down(), self.collide_down()

        if key_list[self.right_key]:
            self.move_right(), self.collide_right()

        if key_list[self.left_key]:
            self.move_left(), self.collide_left()

        check_win()
