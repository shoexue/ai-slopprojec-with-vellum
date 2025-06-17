import { ChatInterface } from "@/components/chat/ChatInterface"

function App() {
  return (
    <div className="min-h-screen bg-background p-4">
      <div className="container mx-auto">
        <h1 className="text-2xl font-bold text-center mb-8">Vellum RAG Chat</h1>
        <ChatInterface />
      </div>
    </div>
  )
}

export default App