import pytest

from bowling import Game, Frame

def test_can_parse_both_pins():
    frame = Frame("45")
    assert frame._first_ball == "4"
    assert frame._second_ball == "5"
    assert frame._first_ball_num == 4
    assert frame._second_ball_num == 5
    
def test_creates_correct_number_of_frames():
    frame_line = '9-|9-|9-|9-|9-|9-|9-|9-|9-|9-||'
    game = Game(frame_line)
    
    assert len(game._frames) == 10
    assert game.get_frame(1)._first_ball == "9"
    assert game.get_frame(1)._second_ball == "-"

def test_can_calculate_frame_score_ints_only():
    frame_line = '42|42|42|42|42|42|42|42|42|42||'
    game = Game(frame_line)
    
    assert game.get_frame(1)._frame_score == 6
    
def test_can_calculate_frame_score_with_no_ball():
    frame_line = '9-|9-|9-|9-|9-|9-|9-|9-|9-|9-||'
    game = Game(frame_line)
    
    assert game.get_frame(1)._frame_score == 9
    
def test_can_calculate_frame_score_with_spares():
    frame_line = '9-|5/|9-|9-|9-|9-|9-|9-|9-|9-||'
    game = Game(frame_line)
    
    assert game.get_frame(2)._frame_score == 10
    
def test_can_calculate_frame_score_with_strikes():
    frame_line = '9-|X|9-|9-|9-|9-|9-|9-|9-|9-||'
    game = Game(frame_line)
    
    assert game.get_frame(2)._frame_score == 10
    
def test_can_handle_bonus_balls_at_end():
    frame_line = '5/|5/|5/|5/|5/|5/|5/|5/|5/|5/||5'
    game = Game(frame_line)
    
    assert game.get_frame(11)._frame_score == 5
    
def test_can_handle_no_bonus_balls_at_end():
    frame_line = '5/|5/|5/|5/|5/|5/|5/|5/|5/|5-||'
    game = Game(frame_line)
    with pytest.raises(Exception) as e_info:
        game.get_frame(11)._frame_score

def test_calculates_game_score_only_numbers():
    frame_line = '9-|9-|9-|9-|9-|9-|9-|9-|9-|9-||'
    game = Game(frame_line)
    
    assert game.calculate_score() == 90
    
def test_calculates_game_score_mix_numbers_and_strikes_spares():
    frame_line1 = '5/|5/|5/|5/|5/|5/|5/|5/|5/|5/||5'
    frame_line2 = 'X|7/|9-|X|-8|8/|-6|X|X|X||81'
    frame_line3 = 'X|X|X|X|X|X|X|X|X|X||XX'
    frame_line4 = 'X|7/|9-|X|-8|8/|-6|X|X|X||82'
    frame_line5 = 'X|7/|9-|X|-8|8/|-6|X|X|X||8/'
    game1 = Game(frame_line1)
    game2 = Game(frame_line2)
    game3 = Game(frame_line3)
    game4 = Game(frame_line4)
    game5 = Game(frame_line5)
    
    assert game1.calculate_score() == 150
    assert game2.calculate_score() == 167
    assert game3.calculate_score() == 300
    assert game4.calculate_score() == 168
    assert game5.calculate_score() == 168
