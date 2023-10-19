import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class Note:
    memo: str
    tags: list[str] = field(default_factory=list)
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    creation_time: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def match(self, to_filter: str):
        """
        Check if the target string exists in the memo or tags.

        Args:
            to_filter (str): The string to check for.

        Returns:
            bool: True if the to_filter string exists in the memo or tags, False otherwise.

        Examples:
            >>> note = Note("This is a memo", tags=["important"])
            >>> note.match("important")
            True
            >>> note.match("memo")
            True
            >>> note.match("Python")
            False
        """
        return to_filter in self.memo or to_filter in self.tags


@dataclass
class NoteBook:
    notes: dict = field(default_factory=dict)

    def get_notes(self) -> dict:
        return self.notes

    def new_note(self, memo: str, tags: list = []) -> uuid.UUID:
        """
        Create a new note and add it to the notebook.

        Args:
            memo (str): The memo text.
            tags (list): A list of tags (optional).

        Returns:
            int: The ID of the newly created note.

        Examples:
            >>> notebook = NoteBook()
            >>> note_id = notebook.new_note("Sample memo", ["tag1", "tag2"])
            >>> isinstance(note_id, uuid.UUID)
            True
        """
        note = Note(memo, tags)
        self.notes[note.id] = note
        return note.id

    def modify_note(self, note_id: uuid.UUID, memo: str) -> Note:
        """
        Modify an existing note in the notebook.

        Args:
            note_id (str): The ID of the note to be modified.
            memo (str): The new memo text.

        Returns:
            Note: The modified note.

        Examples:
            >>> notebook = NoteBook()
            >>> note_id = notebook.new_note("Sample memo", ["tag1", "tag2"])
            >>> modified_note = notebook.modify_note(note_id, "Updated memo")
            >>> modified_note.memo
            'Updated memo'
        """
        self.notes[note_id].memo = memo
        return self.notes[note_id]

    def modify_tags(self, note_id: uuid.UUID, tags: list) -> Note:
        """
        Modify an existing note in the notebook.

        Args:
            note_id (str): The ID of the note to be modified.
            tags (list): The new list of tags.

        Returns:
            Note: The modified note.

        Examples:
            >>> notebook = NoteBook()
            >>> note_id = notebook.new_note("Sample memo", ["tag1", "tag2"])
            >>> modified_note = notebook.modify_tags(note_id, ["newtag"])
            >>> modified_note.tags
            ['newtag']
        """
        self.notes[note_id].tags = tags
        return self.notes[note_id]

    def search(self, to_fileter: str) -> list:
        """
        Search for notes in the notebook that match a target string.

        Args:
            to_filter (str): The string to check for in notes.

        Returns:
            List[Note]: A list of notes that match the target string.

        Examples:
            >>> notebook = NoteBook()
            >>> n1 = notebook.new_note("Python is great", ["programming"])
            >>> n2 = notebook.new_note("Sample note", ["example"])
            >>> result = notebook.search("great")
            >>> len(result)
            1
        """
        return [note for note in self.notes.values() if note.match(to_fileter)]
