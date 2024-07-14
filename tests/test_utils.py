import pytest
from src.utils.replay_buffer import ReplayBuffer
from src.utils.game_environment import OomiGame, Card

def test_replay_buffer():
    buffer = ReplayBuffer(capacity=100)
    for i in range(150):
        buffer.add(i)
    assert len(buffer) == 100
    sample = buffer.sample(10)
    assert len(sample) == 10
    assert all(isinstance(item, int) for item in sample)

def test_oomi_game():
    game = OomiGame()
    assert len(game.deck) == 32
    assert len(game.hands) == 4
    assert all(len(hand) == 8 for hand in game.hands)
    
    game.choose_trump('Hearts')
    assert game.trump_suit == 'Hearts'
    
    assert not game.is_game_over()
    assert game.get_winner() == 'tie'