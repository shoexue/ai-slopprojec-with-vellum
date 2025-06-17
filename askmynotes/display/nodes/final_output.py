from uuid import UUID

from vellum_ee.workflows.display.editor import NodeDisplayData, NodeDisplayPosition
from vellum_ee.workflows.display.nodes import BaseFinalOutputNodeDisplay
from vellum_ee.workflows.display.nodes.types import NodeOutputDisplay

from ...nodes.final_output import FinalOutput


class FinalOutputDisplay(BaseFinalOutputNodeDisplay[FinalOutput]):
    label = "Final Output"
    node_id = UUID("ba20c617-1c5e-4021-bd51-67c273db6f13")
    target_handle_id = UUID("efcae9d8-e5f8-48b0-b415-b6ade753a642")
    output_name = "final-output"
    output_display = {
        FinalOutput.Outputs.value: NodeOutputDisplay(id=UUID("dd14d6a4-fda7-47ff-83d7-53b688370295"), name="value")
    }
    display_data = NodeDisplayData(
        position=NodeDisplayPosition(x=3602.4354778708803, y=208.3790955631399), width=522, height=416
    )
