from typing import Any, Dict, List, Optional

from phi.document.base import Document
from phi.vectordb.base import VectorDb
from phi.embedder import Embedder
from phi.utils.log import logger

class VespaDB(VectorDb):
    def __init__(self, name: str):
        self.name = name

    def create(self) -> None:
        pass

    def doc_exists(self, document: Document) -> bool:
        pass

    def name_exists(self, name: str) -> bool:
        pass

    def id_exists(self, id: str) -> bool:
        pass

    def insert(self, documents: List[Document], filters: Optional[Dict[str, Any]] = None) -> None:
        pass

    def upsert(self, documents: List[Document], filters: Optional[Dict[str, Any]] = None) -> None:
        pass

    def search(self, query: str, limit: int = 5, filters: Optional[Dict[str, Any]] = None) -> List[Document]:
        pass

    def drop(self) -> None:
        pass

    def exists(self) -> bool:
        pass

    def delete(self) -> bool:
        pass
