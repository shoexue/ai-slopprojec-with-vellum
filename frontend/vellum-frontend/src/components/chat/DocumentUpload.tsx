import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Label } from "@/components/ui/label"
import { Card } from "@/components/ui/card"

interface DocumentUploadProps {
  onUpload: (file: File) => void
}

export function DocumentUpload({ onUpload }: DocumentUploadProps) {
  const [isUploading, setIsUploading] = useState(false)
  const [uploadedFile, setUploadedFile] = useState<File | null>(null)

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0]
    if (!file) return

    setUploadedFile(file)
    setIsUploading(true)
    
    // Simulate upload delay
    setTimeout(() => {
      onUpload(file)
      setIsUploading(false)
    }, 1000)
  }

  return (
    <Card className="p-4 mb-4">
      <div className="space-y-4">
        <div className="space-y-2">
          <Label htmlFor="document">Upload Document</Label>
          <div className="flex items-center gap-4">
            <input
              id="document"
              type="file"
              accept=".pdf,.txt,.doc,.docx"
              onChange={handleFileChange}
              className="hidden"
            />
            <Button
              onClick={() => document.getElementById('document')?.click()}
              disabled={isUploading}
            >
              {isUploading ? 'Uploading...' : 'Choose File'}
            </Button>
            {uploadedFile && (
              <span className="text-sm text-muted-foreground">
                {uploadedFile.name}
              </span>
            )}
          </div>
        </div>
      </div>
    </Card>
  )
} 