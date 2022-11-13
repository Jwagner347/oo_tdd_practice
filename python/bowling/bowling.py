class Frame:
    def __init__(self, pins_down) -> None:
        self._pins_down = pins_down
        
    def calculate_frame_score(self):
        first_pin, second_pin = list(self._pins_down)
        return int(first_pin) + int(second_pin)