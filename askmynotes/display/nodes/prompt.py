from uuid import UUID

from vellum_ee.workflows.display.editor import NodeDisplayData, NodeDisplayPosition
from vellum_ee.workflows.display.nodes import BaseInlinePromptNodeDisplay
from vellum_ee.workflows.display.nodes.types import NodeOutputDisplay, PortDisplayOverrides

from ...nodes.prompt import Prompt


class PromptDisplay(BaseInlinePromptNodeDisplay[Prompt]):
    label = "Prompt"
    node_id = UUID("aec8da04-da98-401e-94c8-b9d785594363")
    output_id = UUID("b177d04d-43d6-43fb-a5f3-c761e10578bb")
    array_output_id = UUID("d2a690e2-5288-4641-8fca-636f458308d6")
    target_handle_id = UUID("d519e73a-0a11-4ca0-b12f-8dd8b06342b0")
    node_input_ids_by_name = {
        "prompt_inputs.chat_history": UUID("4ed1faaa-0927-4895-b584-a747b101f0b7"),
        "prompt_inputs.search_node": UUID("449fa252-4aad-4f72-8cb4-b287c7d9c631"),
    }
    attribute_ids_by_name = {"ml_model": UUID("908be058-c6ba-494e-9dce-c797cf9f5111")}
    output_display = {
        Prompt.Outputs.text: NodeOutputDisplay(id=UUID("b177d04d-43d6-43fb-a5f3-c761e10578bb"), name="text"),
        Prompt.Outputs.results: NodeOutputDisplay(id=UUID("d2a690e2-5288-4641-8fca-636f458308d6"), name="results"),
        Prompt.Outputs.json: NodeOutputDisplay(id=UUID("acfb4eea-25de-49bd-8dcc-6efbad41fcd2"), name="json"),
    }
    port_displays = {Prompt.Ports.default: PortDisplayOverrides(id=UUID("3c874419-a293-4c40-92b1-4d63c356e881"))}
    display_data = NodeDisplayData(
        position=NodeDisplayPosition(x=2845.7389718430027, y=586.1526670938263), width=554, height=442
    )
