from vellum import (
    ChatMessagePromptBlock,
    PlainTextPromptBlock,
    PromptParameters,
    PromptSettings,
    RichTextPromptBlock,
    VariablePromptBlock,
)
from vellum.workflows.nodes.displayable import InlinePromptNode

from ..inputs import Inputs
from .search_node import SearchNode


class Prompt(InlinePromptNode):
    ml_model = "gpt-4o-mini"
    blocks = [
        ChatMessagePromptBlock(
            chat_role="SYSTEM",
            blocks=[
                RichTextPromptBlock(
                    blocks=[
                        PlainTextPromptBlock(
                            text="""\
Please answer the user\'s questions, but only use the <context> you\'re given below. If you can\'t answer their questions with the <context>, please say \"Sorry, I\'m unable to answer that.\"

<context>
\
"""
                        ),
                        VariablePromptBlock(input_variable="search_node"),
                        PlainTextPromptBlock(
                            text="""\

</context>\
"""
                        ),
                    ]
                )
            ],
        ),
        VariablePromptBlock(input_variable="chat_history"),
    ]
    prompt_inputs = {
        "chat_history": Inputs.chat_history,
        "search_node": SearchNode.Outputs.text,
    }
    parameters = PromptParameters(
        stop=[],
        temperature=0,
        max_tokens=1000,
        top_p=1,
        top_k=0,
        frequency_penalty=0,
        presence_penalty=0,
        logit_bias={},
        custom_parameters=None,
    )
    settings = PromptSettings(stream_enabled=True)
