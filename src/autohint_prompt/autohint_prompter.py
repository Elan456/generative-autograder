"""
Contains scripts for converting a list of autohint elements into a 
useful prompt for the LLM model.
"""

import enum
from typing import List, Dict


def hint_elements_to_prompt(hint_element_dicts: List[Dict]):
    hint_elements = [HintElement.from_dict(hint_element_dict) for hint_element_dict in hint_element_dicts]
    prompt = "Your job is to generate a hint that will help a student with their programming assignment."
    prompt += "Below are elements that you can pull from to help you generate a hint:\n"

    for i, hint_element in enumerate(hint_elements):
        prompt += f"\n# Element {i + 1}\n"
        prompt += f"## Content\n {hint_element.content}\n"
        prompt += f"## Source\n {hint_element.source.name}\n"
        prompt += f"## Context\n {hint_element.context}\n"
        prompt += f"## Relevance\n {hint_element.relevance}\n"

    prompt += "\nProvide a useful hint that won't give away the answer. The hint should be relevant to the student's current problem."

    return prompt
