from vellum.workflows import BaseWorkflow
from vellum.workflows.state import BaseState

from .inputs import Inputs
from .nodes.current_user_message import CurrentUserMessage
from .nodes.final_output import FinalOutput
from .nodes.prompt import Prompt
from .nodes.search_node import SearchNode


class Workflow(BaseWorkflow[Inputs, BaseState]):
    graph = CurrentUserMessage >> SearchNode >> Prompt >> FinalOutput

    class Outputs(BaseWorkflow.Outputs):
        final_output = FinalOutput.Outputs.value
