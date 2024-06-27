* * *

RL-OomiCardGame
======

RL-OomiCardGame is a Reinforcement Learning (RL) implementation for the card game Oomi, popular in Sri Lanka. This repository provides a framework for training RL agents to play Oomi using recurrent neural networks (RNNs) to handle the sequential nature of the game.

Table of Contents
-----------------

*   [Overview](#overview)
*   [Installation](#installation)
*   [Usage](#usage)
*   [Training](#training)
*   [Model Saving and Loading](#model-saving-and-loading)
*   [Contributing](#contributing)
*   [License](#license)

Overview
--------

Oomi is a card game played by four players. Each player is dealt eight cards, and the game proceeds in turns where players play one card each. The team that wins the most rounds is rewarded. This repository implements an environment for Oomi, and uses reinforcement learning techniques to train agents to play the game.

The key features include:

*   Environment setup for the Oomi card game.
*   LSTM-based policy and value networks to handle the sequential nature of the game.
*   Training loop to optimize the policy and value networks based on game rewards.
*   Saving and loading models for persistent training.

Installation
------------

To use this repository, you need to have Python installed. You can install the required dependencies using pip:

```bash
pip install torch numpy
```

Usage
-----

To get started, clone the repository and navigate into the directory:

```bash
git clone https://github.com/jv-ransika/RL-OomiCardGame.git cd RL-OomiCardGame
```

Training
--------

The `main.py` script contains the training loop for the RL agents. You can run this script to start training the agents:

```bash
python main.py
```

The training process involves:

*   Initializing the game environment.
*   Resetting the game and hidden states for each episode.
*   Running the game loop where each player takes turns to play.
*   Calculating rewards based on game outcomes.
*   Updating the policy and value networks based on the collected experiences.

Model Saving and Loading
------------------------

The models are automatically saved after each episode to ensure progress is not lost. The models are saved in the current directory as `policy_net.pth` and `value_net.pth`. These models can be loaded to resume training or for inference.

Example:

```python
# Load existing models if available, otherwise create new ones
if os.path.exists(policy_model_path):     p
  olicy_net = torch.load(policy_model_path)
else:
  policy_net = LSTMModel(input_dim, hidden_dim, output_dim)
if os.path.exists(value_model_path):
  value_net = torch.load(value_model_path)
else:
  value_net = LSTMModel(input_dim, hidden_dim, output_dim, is_value_net=True)
```

Contributing
------------

Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.

License
-------

This project is licensed under the MIT License. See the LICENSE file for details.

* * *
