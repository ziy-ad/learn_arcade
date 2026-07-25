"""
Platformer Game

python -m arcade.examples.platform_tutorial.01_open_window
"""
import arcade

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300


class GameView(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, "zee's window",  resizable=True)
        self.background_color = arcade.csscolor.WHITE
        self.player_texture = arcade.load_texture("sprite.jpeg")

        self.spirte1 = arcade.Sprite(self.player_texture)
        self.spirte1.center_x = 64
        self.spirte1.center_y = 128


    def setup(self):
        """"modified later"""
        pass


    def on_draw(self):
        self.clear()
        arcade.draw_sprite(self.spirte1)

    def on_resize(self, width, height):
        print(self.width, self.height)
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