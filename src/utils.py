import re
import json
from typing import List, Any, Optional

def extract_json_from_response(text: str) -> Optional[dict]:
    """Extract JSON from LLM output (even if accompanied by text)"""
    # Protect against None
    if text is None:
        return None
    
    # Find the first { and last }
    start = text.find('{')
    end = text.rfind('}')
    if start != -1 and end != -1:
        try:
            return json.loads(text[start:end+1])
        except json.JSONDecodeError:
            pass
    return None

def split_sentences(text: str) -> List[str]:
    """Split text into sentences using periods, question marks, and exclamation marks"""
    # Protect against None
    if text is None:
        return []
    
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    # Remove empty sentences
    return [s.strip() for s in sentences if s.strip()]

def clean_statement_numbering(text: str) -> str:
    """Remove numbering like '1.', '2)' from the beginning of a sentence"""
    # Protect against None
    if text is None:
        return ""
    
    return re.sub(r'^\s*\d+[\.\)]\s*', '', text.strip())