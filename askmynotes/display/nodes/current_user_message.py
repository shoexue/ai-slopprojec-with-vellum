from uuid import UUID

from vellum_ee.workflows.display.editor import NodeDisplayData, NodeDisplayPosition
from vellum_ee.workflows.display.nodes import BaseTemplatingNodeDisplay
from vellum_ee.workflows.display.nodes.types import NodeOutputDisplay, PortDisplayOverrides

from ...nodes.current_user_message import CurrentUserMessage


class CurrentUserMessageDisplay(BaseTemplatingNodeDisplay[CurrentUserMessage]):
    label = "current-user-message"
    node_id = UUID("0db337b0-3ac6-4fb7-9bcf-ee019eb94fe8")
    target_handle_id = UUID("23782b6d-0ba5-4f50-be8e-b974466d1326")
    node_input_ids_by_name = {
        "template": UUID("a0e04029-0cd6-4fd6-9b3d-b5899dbf5c6e"),
        "inputs.chat_history": UUID("0838ddd7-86c7-4247-a88e-e707f1b17dc1"),
    }
    output_display = {
        CurrentUserMessage.Outputs.result: NodeOutputDisplay(
            id=UUID("3a28282e-2219-44dd-bbe9-9ca0da5a10ea"), name="result"
        )
    }
    port_displays = {
        CurrentUserMessage.Ports.default: PortDisplayOverrides(id=UUID("f664b71f-0d75-4bd7-90bf-d7867b2b963d"))
    }
    display_data = NodeDisplayData(
        position=NodeDisplayPosition(x=1730.1514931740614, y=229.77889358468428), width=554, height=368
    )
