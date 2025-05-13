import dspy
from datetime import datetime


def calutator(question: str):
    """Use somente quando precisar fazer algum calculo"""

    program = dspy.ProgramOfThought("question -> answer")
    return program(question=question).answer


def get_time():
    """Use somente para saber a data e hora atual"""

    return datetime.now()
