from typing import List, Optional

from vellum import ChatMessage
from vellum.workflows.inputs import BaseInputs


class Inputs(BaseInputs):
    text: str
    question: Optional[str]
    chat_history: Optional[List[ChatMessage]]
