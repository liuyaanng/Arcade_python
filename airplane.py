#!/usr/bin/env python
# -*- coding: utf-8 -*-


import arcade 
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Aacade Space Shooter"
SCALING = 1.0

class SpaceShooter(arcade.Window):

    """Docstring for SpaceShooter. """

    def __init__(self):
        """Initialize the game.
        """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.paused = False
        #Set the empty sprite lists
        self.enemies_list = arcade.SpriteList()
        self.clouds_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()

    def setup(self):
        """Get the game ready to play
        :returns: TODO

        """
        
        # Set the background color
        arcade.set_background_color(arcade.color.SKY_BLUE)

        # Set up the player
        self.player = arcade.Sprite("images/ship.bmp", SCALING)
        self.player.center_y = self.height / 2
        self.player.left = 10
        self.all_sprites.append(self.player)

        # Spawn a new enemy every 0.25 seconds
        arcade.schedule(self.add_enemy, 0.25)

        # Spawn a new cloud every second 
        arcade.schedule(self.add_cloud, 1.0)

    def add_enemy(self, delta_time: float):
        """Adds a new enemy to the screen.

        :delta_time: delta_time {float} -- How much time has passed since the last call.

        """
        
        # Create the new enemy sprite
        enemy = FlyingSprite("images/alien.bmp", SCALING)

        # Set its position to a random height aed off screen right
        enemy.left = random.randint(self.width, self.width + 80)
        enemy.top = random.randint(10, self.height - 10)

        # Set its speed to a random speed heading left
        enemy.velocity = (random.randint(-20, -5), 0)

        # Add it to the enemies list
        self.enemies_list.append(enemy)
        self.all_sprites.append(enemy)
        
    def add_cloud(self, delta_time: float):

    # First, create the new cloud sprite
        cloud = FlyingSprite("images/ship.bmp", SCALING)

    # Set its position to a random height and off screen right
        cloud.left = random.randint(self.width, self.width + 80)
        cloud.top = random.randint(10, self.height - 10)

    # Set its speed to a random speed heading left
        cloud.velocity = (random.randint(-5, -2), 0)

    # Add it to the enemies list
        self.clouds_list.append(cloud)
        self.all_sprites.append(cloud)
    
    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.Q:
        # Quit immediately
            arcade.close_window()

        if symbol == arcade.key.P:
            self.paused = not self.paused

        if symbol == arcade.key.I or symbol == arcade.key.UP:
            self.player.change_y = 50

        if symbol == arcade.key.K or symbol == arcade.key.DOWN:
            self.player.change_y = -50

        if symbol == arcade.key.J or symbol == arcade.key.LEFT:
            self.player.change_x = -50

        if symbol == arcade.key.L or symbol == arcade.key.RIGHT:
            self.player.change_x = 50

    def on_key_release(self, symbol: int, modifiers: int):
        if (
            symbol == arcade.key.I
            or symbol == arcade.key.K
            or symbol == arcade.key.UP
            or symbol == arcade.key.DOWN
        ):
            self.player.change_y = 0

        if (
        symbol == arcade.key.J
            or symbol == arcade.key.L
            or symbol == arcade.key.LEFT
            or symbol == arcade.key.RIGHT
        ):
            self.player.change_x = 0

                
    def on_update(self, delta_time: float):

    # If paused, don't update anything

    # Update everything
        if self.paused:
            return
        #self.setup()
        #for enemy in self.enemies_list:
           # enemy.update()
        if self.player.collides_with_list(self.enemies_list): 
            arcade.close_window()
        #self.all_sprites.update()
        for sprite in self.all_sprites: 
            sprite.center_x = int( sprite.center_x + 10 * sprite.change_x * delta_time ) 
            sprite.center_y = int( sprite.center_y + 10 * sprite.change_y * delta_time )
        # Keep the player on screen
        if self.player.top > self.height:
            self.player.top = self.height
        if self.player.right > self.width:
            self.player.right = self.width
        if self.player.bottom < 0:
            self.player.bottom = 0
        if self.player.left < 0:
            self.player.left = 0
    def on_draw(self):
        """Draw all game objects
        :returns: TODO

        """
        arcade.start_render()
        self.all_sprites.draw()


class FlyingSprite(arcade.Sprite):

    """Base class for all Flying sprites.
    Flying sprites innclude enemies and clouds
"""

    def update(self):
        """Update the position of the sprite
When it moves off screen to the left, remove it 
"""
        
        # Move the sprite
        super().update()

        # Remove if off the screen 

        if self.right < 0:
            self.remove_from_sprite_lists()
        



if __name__ == "__main__":
    app = SpaceShooter()
    app.setup()
    arcade.run()
