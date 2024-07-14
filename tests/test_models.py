import torch
import pytest
from src.models.card_game_state import CardGameState
from src.models.policy_network import PolicyNetwork

def test_card_game_state():
    model = CardGameState(4, 8, 64)
    trump_suit = torch.tensor([0])
    hand = torch.randint(0, 32, (1, 8))
    desk = torch.randint(0, 32, (1, 4))
    played = torch.randint(0, 32, (1, 20))
    
    output = model(trump_suit, hand, desk, played)
    assert output.shape == (1, 64)

def test_policy_network():
    model = PolicyNetwork(64, 64, 32)
    game_state = torch.randn(1, 64)
    valid_actions = torch.randint(0, 2, (1, 32)).bool()
    
    output = model(game_state, valid_actions)
    assert output.shape == (1, 32)
    assert torch.isclose(output.sum(), torch.tensor(1.0))