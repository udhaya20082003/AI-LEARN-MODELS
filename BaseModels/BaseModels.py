from pydantic import BaseModel
from typing import Optional , Union


class SummarizerIn(BaseModel):
    text: str
    max_length: Optional[int]
    min_length: Optional[int]

class AudioIn(BaseModel):
    audio: bytes 

class QuestionGenIN(BaseModel):
    transcript: str    
    types: list[int]
    chunk_size: Optional[int] = 2000
    chunk_overlap: Optional[int] = 1000


class HumanIn(BaseModel):
    question: str
    context: Optional[str]
    k: Optional[int]
    type: Optional[int]
    chat_history: Optional[list[str]]    
    do_spilting: Optional[bool]
    add_to_history: Optional[bool]
    chunk_size: Optional[int]
    chunk_overlap: Optional[int]

class LlmOut(BaseModel):
    answer: str
    chat_history: Optional[list[str]]
    

class CompareAnswers(BaseModel):
    student_answer: str
    correct_answer: str
    question: str