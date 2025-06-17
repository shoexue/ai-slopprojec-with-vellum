from vellum import ArrayChatMessageContent, ChatMessage, StringChatMessageContent
from vellum.workflows.sandbox import WorkflowSandboxRunner
import sys
import re

from .inputs import Inputs
from .workflow import Workflow

if __name__ != "__main__":
    raise Exception("This file is not meant to be imported")

# Get the user message from command line arguments, or use default
user_message = sys.argv[1] if len(sys.argv) > 1 else "what is a country in south America"

runner = WorkflowSandboxRunner(
    workflow=Workflow(),
    inputs=[
        Inputs(
            text="",
            question="",
            chat_history=[
                ChatMessage(
                    role="USER",
                    text=user_message,
                    content=ArrayChatMessageContent(
                        value=[
                            StringChatMessageContent(value=user_message),
                        ]
                    ),
                ),
            ],
        ),
    ],
)

# Run the workflow and capture the output
result = runner.run()

# Extract the final output from the logs
import logging
import io

# Create a string buffer to capture the logs
log_buffer = io.StringIO()
handler = logging.StreamHandler(log_buffer)
logger = logging.getLogger('vellum.workflows')
logger.addHandler(handler)

# Run the workflow again to capture logs
runner.run()

# Get the logs and extract the final output
logs = log_buffer.getvalue()
final_output_match = re.search(r'final_output: (.*?)(?:\n|$)', logs)
if final_output_match:
    print(final_output_match.group(1))
else:
    print("No response generated")
