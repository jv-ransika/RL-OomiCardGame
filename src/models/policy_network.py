import torch
import torch.nn as nn
import torch.nn.functional as F

class PolicyNetwork(nn.Module):
    def __init__(self, input_dim, hidden_dim, num_cards):
        super(PolicyNetwork, self).__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, hidden_dim)
        self.fc3 = nn.Linear(hidden_dim, num_cards)
        self.dropout = nn.Dropout(0.5)

    def forward(self, game_state, valid_actions):
        x = F.relu(self.fc1(game_state))
        x = self.dropout(x)
        x = F.relu(self.fc2(x))
        x = self.dropout(x)
        logits = self.fc3(x)
        logits = logits.masked_fill(~valid_actions, float('-inf'))
        return F.softmax(logits, dim=-1)