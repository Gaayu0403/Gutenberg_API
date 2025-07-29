from fastapi import FastAPI, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from . import models, crud
from .database import SessionLocal
from fastapi.responses import JSONResponse
from .schemas import HTTPValidationError


app = FastAPI()

# Dependency to get a DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", summary="Root Welcome", description="Returns a welcome message to confirm API is running.")
def root():
    return {"message": "Welcome to the Gutenberg API 🚀", "version": "1.0"}

@app.get("/books/")
def get_books(
    db: Session = Depends(get_db),
    book_ids: Optional[List[int]] = Query(None, alias="book_id"),
    languages: Optional[List[str]] = Query(None),
    mime_types: Optional[List[str]] = Query(None),
    topics: Optional[List[str]] = Query(None),
    author: Optional[str] = None,
    title: Optional[str] = None,
    skip: int = 0,
    limit: int = 25
):
    try:
        print("📥 Starting get_books route")
        total, books = crud.get_filtered_books(
            db=db,
            book_ids=book_ids,
            languages=languages,
            mime_types=mime_types,
            topics=topics,
            author=author,
            title=title,
            skip=skip,
            limit=limit
        )

        results = []
        for book in books:
            results.append({
                "title": book.title,
                "gutenberg_id": book.gutenberg_id,
                "authors": [a.name for a in book.authors],
                "languages": [lang.code for lang in book.languages],
                "subjects": [s.name for s in book.subjects],
                "bookshelves": [b.name for b in book.bookshelves],
                # Removed formats due to missing 'books_book_formats' table
                "download_count": book.download_count,
            })

        print(f"Returning {len(results)} books")
        return JSONResponse(content={
            "total": total,
            "results": results
        })

    except Exception as e:
        print("❌ Error in get_books:", str(e))
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.get("/books/{book_id}")
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    return {
        "title": book.title,
        "gutenberg_id": book.gutenberg_id,
        "id": book.id,
        "media_type": book.media_type,
        "download_count": book.download_count,
        "authors": [a.name for a in book.authors],
        "languages": [lang.code for lang in book.languages],
        "subjects": [s.name for s in book.subjects],
        "bookshelves": [b.name for b in book.bookshelves],
    }


@app.get("/authors/")
def read_authors(limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_authors(db, limit)
@app.get("/authors/{author_id}", responses={422: {"model": HTTPValidationError}})
def read_author(author_id: int, db: Session = Depends(get_db)):
    author = crud.get_author(db, author_id)
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return author
