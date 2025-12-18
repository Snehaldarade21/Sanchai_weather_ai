import { useState } from 'react'

export default function App() {
  const [input, setInput] = useState('')
  const [reply, setReply] = useState('')

  const send = async () => {
    const r = await fetch('http://localhost:8000/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: input })
    })
    const d = await r.json()
    setReply(d.response)
  }

  return (
    <div style={{ padding: 40 }}>
      <h2>Weather AI</h2>
      <input value={input} onChange={e => setInput(e.target.value)} />
      <button onClick={send}>Send</button>
      <p>{reply}</p>
    </div>
  )
}
