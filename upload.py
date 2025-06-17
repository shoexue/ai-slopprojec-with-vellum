# upload.py

import os
from vellum.client import Vellum

# Get API key from environment variable
API_KEY = os.environ.get("VELLUM_API_KEY")
if not API_KEY:
    raise ValueError("Please set the VELLUM_API_KEY environment variable")

client = Vellum(
    api_key=API_KEY
)

with open("lecture_notes.pdf", "rb") as f:
    result = client.documents.upload(
        contents=f,
        label="Human-friendly label for your document",
        add_to_index_names=["notes"],
        external_id="<your-external-id>",
        keywords=[],
    )

print("Upload complete!")