from uuid import UUID

from vellum_ee.workflows.display.editor import NodeDisplayData, NodeDisplayPosition
from vellum_ee.workflows.display.nodes import BaseSearchNodeDisplay
from vellum_ee.workflows.display.nodes.types import NodeOutputDisplay, PortDisplayOverrides

from ...nodes.search_node import SearchNode


class SearchNodeDisplay(BaseSearchNodeDisplay[SearchNode]):
    label = "Search Node"
    node_id = UUID("d3e27a18-fea5-47ac-b9fb-4cc7ee5a6e10")
    target_handle_id = UUID("9f9c3fa4-e623-4b03-8901-824b0042b31b")
    node_input_ids_by_name = {
        "query": UUID("3a178d47-08b9-42d8-ae03-24ff84d99e1a"),
        "document_index_id": UUID("532581ab-eaae-4d46-a426-e88cbca9f35c"),
        "weights": UUID("f574e634-77b9-4075-acca-e4bb61059ffa"),
        "limit": UUID("f432a12b-d905-4711-868a-fdeedeabe5d1"),
        "separator": UUID("54003892-94be-4f0f-bb2a-4366e1933f9b"),
        "result_merging_enabled": UUID("958afb21-feb7-46fe-a5dd-dd83365063a7"),
        "external_id_filters": UUID("8fa9af4c-be5b-4102-b63c-69dd274f8be9"),
        "metadata_filters": UUID("df94dba6-1e3f-49d4-aae0-e7e110ab704b"),
    }
    output_display = {
        SearchNode.Outputs.results: NodeOutputDisplay(id=UUID("cf19354e-e627-4968-9d4f-0f2232748a05"), name="results"),
        SearchNode.Outputs.text: NodeOutputDisplay(id=UUID("0b9f32f0-9d16-4742-a056-816b9236b9cd"), name="text"),
    }
    port_displays = {SearchNode.Ports.default: PortDisplayOverrides(id=UUID("b68b0063-4da5-4f04-9c7a-895bd45d178a"))}
    display_data = NodeDisplayData(
        position=NodeDisplayPosition(x=2287.742619453925, y=519.2281256665957), width=554, height=672
    )
