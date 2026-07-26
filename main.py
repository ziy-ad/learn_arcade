"""
Platformer Game

python -m arcade.examples.platform_tutorial.01_open_window
"""
import arcade
import random

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300


class GameView(arcade.Window):
    def __init__(self):
            super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, "zee's window", resizable=True)
            self.background_color = arcade.csscolor.WHITE
            self.player_texture = arcade.load_texture("sprite.jpeg")
    
            self.sprite_list = arcade.SpriteList()
    
            self.sprites = [self.sprite_list.append(arcade.Sprite(self.player_texture)) for _ in range(10)]
    
            for sprite in self.sprite_list:
                sprite.center_x = random.randint(1, 400)
                sprite.center_y = random.randint(1, 300)
                print(sprite.center_x, sprite.center_y)


    def setup(self):
        """"modified later"""
        pass


    def on_draw(self):
        self.clear()
        self.sprite_list.draw()

    def on_resize(self, width, height):
        return super().on_resize(width, height)



def main():
    """Main function"""
    window = GameView()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit(1)