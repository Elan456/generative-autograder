from typing import List
from .prompt_builder import PromptBuilder
from .hint_element import *


class StringDifferencePB(PromptBuilder):
    def __init__(self):
        super().__init__()
    
    def get_prompt(self, hint_elements: List[HintElement]):
        pass 
