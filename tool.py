from pydantic import BaseModel
from typing import List

# ----- Mock data -----
mock_user_documents = {
    "paul123": [
        {"id": "deck1", "title": "HSK 2 Vocabulary Deck"},
        {"id": "note1", "title": "Past Tense Grammar Notes"},
        {"id": "read1", "title": "The Little Prince (Chinese-English Bilingual)"}
    ],
    "emmanuel": [
        {"id": "deck2", "title": "HSK 4 Sentence Patterns"},
        {"id": "note2", "title": "Modal Particles Study Notes"},
        {"id": "read2", "title": "Journey to the West (Simplified)"}
    ]
}
# ----- Pydantic models -----
class UserRequest(BaseModel):
    user_id: str

class Document(BaseModel):
    id: str
    title: str

class DocumentList(BaseModel):
    documents: List[Document]

# ----- Tool functions -----
def get_user_documents_logic(user_id: str) -> List[Document]:
    user_docs = mock_user_documents.get(user_id, [])
    return user_docs