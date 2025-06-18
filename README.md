This project was made with the help of vellum-ai. This web app was built to help students study and get answers to questions based on notes, while ensuring accuracy. This means if there is any question outside of the scope of the documents provided, it will not hallucinate and refuse to answer. This was made with Flask, React, and Vellum. 

**HOW I USED VELLUM**

A vellum workflow based on a RAG chatbot was created. The search node, prompt node, etc was used. The CLI tool was used to easily pull all the code for this workflow. 
The workflow ensured that responses were based on the context of the document provided. 
The POST api/upload-documents was used to upload and process documents on Vellum AI, and this was already integrated into the workflow. 

Essentially all the backend processing was handlelled by Vellum and the rest was to wrapper around it. 



Here is a video demo 

https://github.com/user-attachments/assets/e277e8b3-63e3-4aef-bbe8-8bae528f643f
