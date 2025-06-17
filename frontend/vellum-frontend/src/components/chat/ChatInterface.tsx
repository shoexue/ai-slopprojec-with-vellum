import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { ScrollArea } from "@/components/ui/scroll-area"
import { ChatMessage } from "./ChatMessage"

interface Message {
  content: string
  isUser: boolean
}

export function ChatInterface() {
  const [messages, setMessages] = useState<Message[]>([])
  const [input, setInput] = useState("")

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    if (!input.trim()) return

    // Add user message
    setMessages(prev => [...prev, { content: input, isUser: true }])
    
    // Simulate bot response (replace with actual API call later)
    setTimeout(() => {
      setMessages(prev => [...prev, { 
        content: "This is a simulated response. The actual Vellum RAG integration will be implemented later.", 
        isUser: false 
      }])
    }, 1000)

    setInput("")
  }

  return (
    <div className="flex flex-col h-[600px] w-full max-w-2xl mx-auto p-4">
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
          placeholder="Type your message..."
          className="flex-1"
        />
        <Button type="submit">Send</Button>
      </form>
    </div>
  )
} 