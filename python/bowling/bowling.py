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
    
    def calculate_additional_score(self, current_frame):
        additional_score = 0
        if current_frame == 10 and (self._frames[current_frame]._first_ball == "X" or self._frames[current_frame]._second_ball == "/"):
            additional_score = self._frames[current_frame+1]._frame_score
        elif self._frames[current_frame]._first_ball == "X":
            if self._frames[current_frame+1]._first_ball == 'X':
                additional_score = 10 + self._frames[current_frame+2]._first_ball_num
            else:
                additional_score = self._frames[current_frame+1]._frame_score
        elif self._frames[current_frame]._second_ball == "/":
            additional_score = self._frames[current_frame+1]._first_ball_num
        
        return additional_score
    
    def calculate_score(self):
        score = 0
        frame = 1

        while frame <= 10:
            additional_score = self.calculate_additional_score(frame)
            
            score += self._frames[frame]._frame_score + additional_score
            frame+=1
            
        return score

class Frame:
    def __init__(self, pins_down) -> None:
        self.set_balls(pins_down)
        self.set_balls_num()
        self.set_frame_score()
        
    def set_frame_score(self):
        if not hasattr(self, '_second_ball'):
            self._frame_score = 10 if self._first_ball == 'X' else int(self._first_ball)
        elif self._second_ball == '/':
            self._frame_score = 10
        else:
            if self._first_ball == '-':
                first_pin = 0
            elif self._first_ball == 'X':
                first_pin = 10
            else:
                first_pin = int(self._first_ball)
                
            if self._second_ball == '-':
                second_pin = 0
            elif self._second_ball == 'X':
                second_pin = 10
            else:
                second_pin = int(self._second_ball)

            self._frame_score = first_pin + second_pin
        
    def set_balls(self, pins):
        if len(pins) == 2:
            self._first_ball = list(pins)[0]
            self._second_ball = list(pins)[1]
        else:
            self._first_ball = list(pins)[0]
            
    def set_balls_num(self):
        match self._first_ball:
                case "X":
                    self._first_ball_num = 10
                case "-":
                    self._first_ball_num = 0
                case _:
                    self._first_ball_num = int(self._first_ball)
                    
        if hasattr(self, '_second_ball'):
            match self._second_ball:
                    case "/":
                        self._second_ball_num = 10 - self._first_ball_num
                    case "-":
                        self._second_ball_num = 0
                    case "X":
                        self._second_ball_num = 10
                    case _:
                        self._second_ball_num = int(self._second_ball)
        
        