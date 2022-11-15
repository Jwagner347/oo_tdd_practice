class Game:
    def __init__(self, frame_line) -> None:
        self._frames = self.create_frames(frame_line)
        
    def create_frames(self, frame_line):
        frames_dict = {}
        frames = frame_line.split("|")
        frames = [i for i in frames if i]

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
        self.set_balls(pins_down)
        self.set_frame_score()
        
    def transform_balls(ball1, ball2):
        if ball1 == '-':
            first_pin = 0
        if ball2 == '-':
            second_pin = 0
            
        if ball1 == 'X':
            first_pin = 10
        if ball2 == 'X':
            second_pin = 10

        return first_pin, second_pin
        
    def set_frame_score(self):
        if not hasattr(self, '_second_ball'):
            self._frame_score = 10 if self._first_ball == 'X' else int(self._first_ball)
        elif self._second_ball == '/':
            self._frame_score = 10
        else:
            first_pin = 0 if self._first_ball == '-' else int(self._first_ball)
            second_pin = 0 if self._second_ball == '-' else int(self._second_ball)

            self._frame_score = first_pin + second_pin
        
    def set_balls(self, pins):
        if len(pins) == 2:
            self._first_ball = list(pins)[0]
            self._second_ball = list(pins)[1]
        else:
            self._first_ball = list(pins)[0]