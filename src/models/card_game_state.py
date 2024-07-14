import torch
import torch.nn as nn

class CardGameState(nn.Module):
    def __init__(self, num_suits, num_ranks, hidden_dim):
        super(CardGameState, self).__init__()
        self.num_suits = num_suits
        self.num_ranks = num_ranks
        self.card_embedding = nn.Embedding(num_suits * num_ranks, hidden_dim)
        self.suit_embedding = nn.Embedding(num_suits + 1, hidden_dim)  # +1 for no trump
        self.lstm = nn.LSTM(hidden_dim, hidden_dim, batch_first=True)
        self.attention = nn.MultiheadAttention(hidden_dim, 4)
        self.combine_layer = nn.Linear(hidden_dim * 4, hidden_dim)

    def forward(self, trump_suit, hand, desk, played):
        trump_embed = self.suit_embedding(trump_suit).unsqueeze(1)
        hand_state = self._process_cards(hand)
        desk_state = self._process_cards(desk)
        played_state = self._process_cards(played)
        game_state = torch.cat([trump_embed, hand_state, desk_state, played_state], dim=1)
        return self.combine_layer(game_state.view(game_state.size(0), -1))

    def _process_cards(self, cards):
        embedded = self.card_embedding(cards)
        lstm_out, _ = self.lstm(embedded)
        attn_out, _ = self.attention(lstm_out, lstm_out, lstm_out)
        return attn_out.mean(1).unsqueeze(1)