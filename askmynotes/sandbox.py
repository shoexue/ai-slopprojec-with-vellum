from vellum import ArrayChatMessageContent, ChatMessage, StringChatMessageContent
from vellum.workflows.sandbox import WorkflowSandboxRunner

from .inputs import Inputs
from .workflow import Workflow

if __name__ != "__main__":
    raise Exception("This file is not meant to be imported")


runner = WorkflowSandboxRunner(
    workflow=Workflow(),
    inputs=[
        Inputs(
            text="",
            question="",
            chat_history=[
                ChatMessage(
                    role="USER",
                    text="what is a country in south America",
                    content=ArrayChatMessageContent(
                        value=[
                            StringChatMessageContent(value="what is a country in south America"),
                        ]
                    ),
                ),
            ],
        ),
    ],
)

runner.run()
