import { Card } from "@/components/ui/card"

interface ChatMessageProps {
  message: string
  isUser: boolean
}

export function ChatMessage({ message, isUser }: ChatMessageProps) {
  return (
    <div className={`flex ${isUser ? 'justify-end' : 'justify-start'} mb-4`}>
      <Card className={`max-w-[80%] p-4 ${isUser ? 'bg-primary text-primary-foreground' : 'bg-muted'}`}>
        <p className="text-sm">{message}</p>
      </Card>
    </div>
  )
} 