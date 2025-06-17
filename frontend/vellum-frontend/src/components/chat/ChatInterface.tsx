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

    try {
      const response = await fetch('http://localhost:5000/run-script', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userMessage })
      })
      
      const data = await response.json()
      
      // Check if we got a valid response
      if (data.stdout && data.stdout.trim()) {
        setMessages(prev => [...prev, {
          content: data.stdout.trim(),
          isUser: false,
          timestamp: new Date()
        }])
      } else {
        setMessages(prev => [...prev, {
          content: "I couldn't generate a response. Please try again.",
          isUser: false,
          timestamp: new Date()
        }])
      }

      if (data.stderr) {
        console.error('Script error:', data.stderr)
      }
    } catch (error) {
      console.error('Failed to run script:', error)
      setMessages(prev => [...prev, {
        content: "Failed to get response from server. Please try again.",
        isUser: false,
        timestamp: new Date()
      }])
    } finally {
      setIsProcessing(false)
    }
  }

  return (
    <div className="flex flex-col h-[600px] w-full max-w-2xl mx-auto p-4 bg-pink-50">
      <DocumentUpload onUpload={handleDocumentUpload} />
      <ScrollArea className="flex-1 p-4 rounded-lg border border-pink-200 bg-white">
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
          className="flex-1 border-pink-200 focus:border-pink-400"
          disabled={isProcessing}
        />
        <Button 
          type="submit" 
          disabled={isProcessing}
          className="bg-pink-500 hover:bg-pink-600 text-white"
        >
          {isProcessing ? 'Processing...' : 'Send'}
        </Button>
      </form>
    </div>
  )
} 