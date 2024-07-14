# Oomi AI Project

This project implements an AI agent to play the Oomi card game using reinforcement learning techniques.

## Features

- Deep Q-Learning (DQN) based AI agent
- Self-play training mechanism
- Experience replay for improved learning stability
- Epsilon-greedy exploration strategy
- Policy gradient method with entropy regularization

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/oomi-ai.git
   cd oomi-ai
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the training script:
   ```
   python src/train.py
   ```

## Project Structure

- `src/`: Source code for the AI agent and game environment
- `tests/`: Unit tests
- `notebooks/`: Jupyter notebooks for analysis
- `data/`: Training statistics and other data
- `models/`: Saved model checkpoints

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
