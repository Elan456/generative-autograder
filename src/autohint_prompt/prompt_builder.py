from typing import List
from .hint_element import HintElement, HintSource


class PromptBuilder:
    def __init__(self):
        pass

    def get_prompt(self, hint_elements: List[HintElement]):
        raise NotImplementedError("Subclasses should implement this method.")