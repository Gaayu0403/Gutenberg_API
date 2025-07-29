from pydantic import BaseModel
from typing import List, Optional, Union


class AuthorOut(BaseModel):
    name: str
    birth_year: Optional[int]
    death_year: Optional[int]

    class Config:
        orm_mode = True


class SubjectOut(BaseModel):
    name: str

    class Config:
        orm_mode = True


class BookshelfOut(BaseModel):
    name: str

    class Config:
        orm_mode = True


class FormatOut(BaseModel):
    mime_type: str
    url: str

    class Config:
        orm_mode = True


class LanguageOut(BaseModel):
    code: str

    class Config:
        orm_mode = True


class BookOut(BaseModel):
    id: int
    title: str
    download_count: int
    authors: List[AuthorOut]
    subjects: List[SubjectOut]
    bookshelves: List[BookshelfOut]
    formats: List[FormatOut]
    language: Optional[LanguageOut]

    class Config:
        orm_mode = True


class BookListResponse(BaseModel):
    total: int
    books: List[BookOut]


class ValidationError(BaseModel):
    loc: List[Union[str, int]]
    msg: str
    type: str


class HTTPValidationError(BaseModel):
    detail: List[ValidationError]    
