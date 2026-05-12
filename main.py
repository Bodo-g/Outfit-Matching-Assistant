"""Main entry point for the outfit matching assistant project."""
from src.train import train


if __name__ == "__main__":
    model = train()
    print(model)
