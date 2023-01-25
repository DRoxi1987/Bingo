from home_layer import HomeLayer
from game_layer import GameLayer


class StateManager:
    def __init__(self, surface):
        self.state = "home"
        self.game_layer = GameLayer()
        self.home_layer = HomeLayer()
        self.surface = surface

    def state_manager(self):
        if self.state == "home":
            self.home_layer.create_layer(self.surface)
            temp = self.home_layer.check_events_home()
            if temp == "game":
                self.state = "game"

        elif self.state == "game":
            self.game_layer.create_layer(self.surface)
            temp = self.game_layer.check_events_game()
            if temp == "home":
                self.game_layer.get_all()
                self.state = "home"
