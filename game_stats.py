class GameStats:
    """Control the statics of the game"""
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        """The states to be resetted for new game"""
        self.ship_left = self.settings.ship_limit