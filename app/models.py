
from sqlalchemy import Column, Integer, String, SmallInteger, Text, ForeignKey, Table
from sqlalchemy.orm import relationship
from .database import Base

# ---------------------- Association Tables ----------------------
book_languages = Table(
    "books_book_languages",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("book_id", Integer, ForeignKey("books_book.id")),
    Column("language_id", Integer, ForeignKey("books_language.id"))
)

book_subjects = Table(
    "books_book_subjects",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("book_id", Integer, ForeignKey("books_book.id")),
    Column("subject_id", Integer, ForeignKey("books_subject.id"))
)

book_bookshelves = Table(
    "books_book_bookshelves",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("book_id", Integer, ForeignKey("books_book.id")),
    Column("bookshelf_id", Integer, ForeignKey("books_bookshelf.id"))
)

book_formats = Table(
    "books_book_formats",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("book_id", Integer, ForeignKey("books_book.id")),
    Column("format_id", Integer, ForeignKey("books_format.id"))
)

# ---------------------- Models ----------------------

# Many-to-many association between books and authors
class BookAuthorLink(Base):
    __tablename__ = "books_book_authors"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books_book.id"))
    author_id = Column(Integer, ForeignKey("books_author.id"))

class Book(Base):
    __tablename__ = "books_book"

    id = Column(Integer, primary_key=True, index=True)
    gutenberg_id = Column(Integer, nullable=False)
    title = Column(Text)
    media_type = Column(String(16), nullable=False)
    download_count = Column(Integer)

    authors = relationship("Author", secondary="books_book_authors", back_populates="books")
    languages = relationship("Language", secondary=book_languages, back_populates="books")
    subjects = relationship("Subject", secondary=book_subjects, back_populates="books")
    bookshelves = relationship("Bookshelf", secondary=book_bookshelves, back_populates="books")

class Author(Base):
    __tablename__ = "books_author"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), nullable=False)
    birth_year = Column(SmallInteger)
    death_year = Column(SmallInteger)

    books = relationship("Book", secondary="books_book_authors", back_populates="authors")

class Subject(Base):
    __tablename__ = "books_subject"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)

    books = relationship("Book", secondary=book_subjects, back_populates="subjects")

class Bookshelf(Base):
    __tablename__ = "books_bookshelf"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)

    books = relationship("Book", secondary=book_bookshelves, back_populates="bookshelves")

class Language(Base):
    __tablename__ = "books_language"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(8), nullable=False)

    books = relationship("Book", secondary=book_languages, back_populates="languages")
class Format(Base):
    __tablename__ = "books_format"

    id = Column(Integer, primary_key=True, index=True)
    mime_type = Column(String(255), nullable=False)
    url = Column(Text, nullable=False)

