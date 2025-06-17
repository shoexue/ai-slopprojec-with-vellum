import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { ScrollArea } from "@/components/ui/scroll-area"
import { ChatMessage } from "./ChatMessage"
import { DocumentUpload } from "./DocumentUpload"

interface Message {
  content: string
  isUser: boolean
  timestamp: Date
}

export function ChatInterface() {
  const [messages, setMessages] = useState<Message[]>([])
  const [input, setInput] = useState("")
  const [isProcessing, setIsProcessing] = useState(false)

  const handleDocumentUpload = (file: File) => {
    setMessages(prev => [
      ...prev,
      {
        content: `Document "${file.name}" uploaded successfully. You can now ask questions about it.`,
        isUser: false,
        timestamp: new Date()
      }
    ])
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!input.trim() || isProcessing) return

    const userMessage = input.trim()
    setInput("")
    setIsProcessing(true)

    // Add user message
    setMessages(prev => [...prev, {
      content: userMessage,
      isUser: true,
      timestamp: new Date()
    }])

    // Simulate bot response
    setTimeout(() => {
      setMessages(prev => [...prev, {
        content: "This is a simulated response. The actual Vellum RAG integration will be implemented later.",
        isUser: false,
        timestamp: new Date()
      }])
      setIsProcessing(false)
    }, 1000)
  }

  return (
    <div className="flex flex-col h-[600px] w-full max-w-2xl mx-auto p-4">
      <DocumentUpload onUpload={handleDocumentUpload} />
      <ScrollArea className="flex-1 p-4 rounded-lg border">
        <div className="space-y-4">
          {messages.map((message, index) => (
            <ChatMessage
              key={index}
              message={message.content}
              isUser={message.isUser}
            />
          ))}
        </div>
      </ScrollArea>
      <form onSubmit={handleSubmit} className="flex gap-2 mt-4">
        <Input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask a question about your document..."
          className="flex-1"
          disabled={isProcessing}
        />
        <Button type="submit" disabled={isProcessing}>
          {isProcessing ? 'Processing...' : 'Send'}
        </Button>
      </form>
    </div>
  )
} 