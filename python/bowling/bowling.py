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
    
    def calculate_score(self):
        score = 0
        frame = 1
        while frame <= 10:
            additional_score = 0
            if self._frames[frame]._second_ball == '/':
                additional_score = int(self._frames[frame + 1]._first_ball)
            score += self._frames[frame]._frame_score + additional_score
            frame+=1
        return score

class Frame:
    def __init__(self, pins_down) -> None:
        self.set_balls(pins_down)
        self.set_frame_score()
        
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