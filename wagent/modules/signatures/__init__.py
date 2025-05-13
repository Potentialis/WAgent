import dspy


class Attendant(dspy.Signature):
    """
    Atenda o cliente.
    Seja breve.
    Responda em portugues do brasil.
    Caso não precise de informações adicionais finalize.
    """

    user_msg: str = dspy.InputField(desc="user message, may be a question")
    answer: str = dspy.OutputField()


class TechnicalSpecialist(dspy.Signature):
    """Especialista tecnico em sistema fotovotaicos"""

    question: str = dspy.InputField()
    answer: str = dspy.OutputField()


class CompanyConsultant(dspy.Signature):
    """Consultor sobre questões da empresa"""

    question: str = dspy.InputField()
    answer: str = dspy.OutputField()
