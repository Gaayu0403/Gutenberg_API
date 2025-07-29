from sqlalchemy.orm import Session
from sqlalchemy import or_, func
from . import models
from typing import List, Optional, Tuple

# Get books with optional limit
def get_books(db: Session, limit: int = 10):
    return db.query(models.Book).limit(limit).all()

# Get a book by ID
def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

# Get authors with optional limit
def get_authors(db: Session, limit: int = 10):
    return db.query(models.Author).limit(limit).all()

# Get an author by ID
def get_author(db: Session, author_id: int):
    return db.query(models.Author).filter(models.Author.id == author_id).first()

def get_filtered_books(
    db: Session,
    book_ids: Optional[List[int]] = None,
    languages: Optional[List[str]] = None,
    mime_types: Optional[List[str]] = None,
    topics: Optional[List[str]] = None,
    author: Optional[str] = None,
    title: Optional[str] = None,
    skip: int = 0,
    limit: int = 25
) -> Tuple[int, List[models.Book]]:

    query = db.query(models.Book)

    if book_ids:
        query = query.filter(models.Book.gutenberg_id.in_(book_ids))

    if languages:
        query = query.join(models.Book.languages).filter(models.Language.code.in_(languages))


    if mime_types:
        query = query.join(models.Book.formats).filter(models.Format.mime_type.in_(mime_types))

    if topics:
        topic_filter = []
        for topic in topics:
            pattern = f"%{topic.lower()}%"
            topic_filter.append(func.lower(models.Subject.name).like(pattern))
            topic_filter.append(func.lower(models.Bookshelf.name).like(pattern))
        query = query.outerjoin(models.Book.subjects).outerjoin(models.Book.bookshelves)
        query = query.filter(or_(*topic_filter))

    if author:
        query = query.join(models.Book.authors).filter(func.lower(models.Author.name).like(f"%{author.lower()}%"))

    if title:
        query = query.filter(func.lower(models.Book.title).like(f"%{title.lower()}%"))

    total = query.distinct().count()
    books = query.order_by(models.Book.download_count.desc()).offset(skip).limit(limit).all()

    return total, books