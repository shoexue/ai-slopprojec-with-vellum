from uuid import UUID

from vellum_ee.workflows.display.base import (
    EdgeDisplay,
    EntrypointDisplay,
    WorkflowInputsDisplay,
    WorkflowMetaDisplay,
    WorkflowOutputDisplay,
)
from vellum_ee.workflows.display.editor import NodeDisplayData, NodeDisplayPosition
from vellum_ee.workflows.display.vellum import WorkflowDisplayData, WorkflowDisplayDataViewport
from vellum_ee.workflows.display.workflows import BaseWorkflowDisplay

from ..inputs import Inputs
from ..nodes.current_user_message import CurrentUserMessage
from ..nodes.final_output import FinalOutput
from ..nodes.prompt import Prompt
from ..nodes.search_node import SearchNode
from ..workflow import Workflow


class WorkflowDisplay(BaseWorkflowDisplay[Workflow]):
    workflow_display = WorkflowMetaDisplay(
        entrypoint_node_id=UUID("ce6dd9bf-4f7c-41b2-b69b-30d513bdb734"),
        entrypoint_node_source_handle_id=UUID("ff70a988-3a13-4a09-96a0-bd3ef4005921"),
        entrypoint_node_display=NodeDisplayData(position=NodeDisplayPosition(x=1545, y=330), width=124, height=48),
        display_data=WorkflowDisplayData(
            viewport=WorkflowDisplayDataViewport(x=-1303.8891282431443, y=-6.284935803638433, zoom=0.4850633663544947)
        ),
    )
    inputs_display = {
        Inputs.text: WorkflowInputsDisplay(id=UUID("2fe7383f-c728-488f-a158-8760ab651c3b"), name="text"),
        Inputs.question: WorkflowInputsDisplay(
            id=UUID("dce9a71d-09c4-4d50-a134-4a42b6aa1c4f"), name="question", color="lipstick"
        ),
        Inputs.chat_history: WorkflowInputsDisplay(
            id=UUID("867d4007-fb4e-4d1a-b4c8-c99303afa73c"), name="chat_history", color="navy"
        ),
    }
    entrypoint_displays = {
        CurrentUserMessage: EntrypointDisplay(
            id=UUID("ce6dd9bf-4f7c-41b2-b69b-30d513bdb734"),
            edge_display=EdgeDisplay(id=UUID("6a1a3e69-90b7-432b-9c41-af9e680dfaae")),
        )
    }
    edge_displays = {
        (CurrentUserMessage.Ports.default, SearchNode): EdgeDisplay(id=UUID("a50ef717-bed1-482a-881f-dcffa9b2e339")),
        (Prompt.Ports.default, FinalOutput): EdgeDisplay(id=UUID("68f71b6e-2eac-4822-975f-ca759cb13704")),
        (SearchNode.Ports.default, Prompt): EdgeDisplay(id=UUID("64acd93d-337a-423b-a1df-fe597fa4ea92")),
    }
    output_displays = {
        Workflow.Outputs.final_output: WorkflowOutputDisplay(
            id=UUID("dd14d6a4-fda7-47ff-83d7-53b688370295"), name="final-output"
        )
    }
