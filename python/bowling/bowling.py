class Game:
    def __init__(self, frame_line) -> None:
        self._frames = self.create_frames(frame_line)
        
    def create_frames(self, frame_line):
        frames_dict = {}
        frames = frame_line.split("|")
        for i, val in enumerate(frames):
            if val != "":
                frame = Frame(frames[i])
                frames_dict[i+1] = frame
        # {key: value for (key, value) in frames}
        return frames_dict
    
    def get_frame(self, frame_num):
        return self._frames[frame_num]

class Frame:
    def __init__(self, pins_down) -> None:
        # refactor this to be a method
        first_pin_string = list(pins_down)[0]
        second_pin_string = list(pins_down)[1]
        
        if first_pin_string == '-':
            first_pin_string = 0
        if second_pin_string == '-':
            second_pin_string = 0

        self._first_pin = int(first_pin_string)
        self._second_pin = int(second_pin_string)
        
    # def calculate_pins_only_score(self):
    #     first_pin, second_pin = list(self._pins_down)
    #     if first_pin == '/' or second_pin == '/':
    #         return 10
    #     return int(first_pin) + int(second_pin)