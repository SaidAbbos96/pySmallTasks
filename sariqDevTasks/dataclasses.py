from dataclasses import dataclass


@dataclass(frozen=True)
class Question:
    text: str = "def val"
    is_true: bool = False
    explanation: int = 2
