import React, { useState, useEffect } from 'react'
import ListItem from '../components/ListItem.js'
import AddButton from '../components/AddButton.js'

const NotesListPage = () => {
    const [notes, setNotes] = useState([])

    useEffect(() => {
        getNotes()
    }, [])

    const getNotes = async () => {
        try {
            const response = await fetch('/api/notes/')
            const data = await response.json()
            setNotes(data)
        } catch (error) {
            console.error(error)
        }
    }

    return (
        <div className='notes'>
            <div className="notes-header">
                <h2 className="notes-title">
                    &#9782; Notes
                </h2>
                <p className="notes-count">{notes.length}</p>
            </div>
            <div className='notes-list'>
                {notes.map((note) => (
                    <div className='note-preview' key={note.id}>
                        <ListItem note={note} />
                    </div>
                ))}
            </div>
            <AddButton />
        </div>
    )
}

export default NotesListPage
