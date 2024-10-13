from pathlib import Path
from typing import List, Union, IO, Any
from phi.document.base import Document
from phi.document.reader.base import Reader
from phi.utils.log import logger


class TextReader(Reader):
    """Reader for Text files"""

    def read(self, path_or_content: Union[Path, IO, str]) -> List[Document]:
        if not path_or_content:
            raise ValueError("No path or content provided")

        try:
            if isinstance(path_or_content, str):
                file_name = "text_content"
                file_contents = path_or_content
            elif isinstance(path_or_content, IO):
                temp_path = Path("temp_file.txt")
                temp_path.write_bytes(path_or_content.read())
                path_or_content = temp_path
                file_name = path_or_content.name.split("/")[-1].split(".")[0].replace("/", "_").replace(" ", "_")
                file_contents = path_or_content.read_text()
            else:
                logger.info(f"Reading: {path_or_content}")
                file_name = path_or_content.name.split("/")[-1].split(".")[0].replace("/", "_").replace(" ", "_")
                file_contents = path_or_content.read_text()

            logger.info(f"Processing: {file_name}")
            
            documents = [
                Document(
                    name=file_name,
                    id=file_name,
                    content=file_contents,
                )
            ]
            if self.chunk:
                chunked_documents = []
                for document in documents:
                    chunked_documents.extend(self.chunk_document(document))
                return chunked_documents
            return documents
        except Exception as e:
            logger.error(f"Error reading: {path_or_content}: {e}")
        return []
