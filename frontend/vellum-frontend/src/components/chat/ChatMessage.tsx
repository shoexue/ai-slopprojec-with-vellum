import { Card } from "@/components/ui/card"

interface ChatMessageProps {
  message: string
  isUser: boolean
}

export function ChatMessage({ message, isUser }: ChatMessageProps) {
  return (
    <div className={`flex ${isUser ? 'justify-end' : 'justify-start'}`}>
      <div
        className={`max-w-[80%] rounded-lg p-3 ${
          isUser
            ? 'bg-pink-500 text-white'
            : 'bg-pink-100 text-pink-900'
        }`}
      >
        {message}
      </div>
    </div>
  )
} 