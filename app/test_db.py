from .database import SessionLocal
from .models import Book, Author

def test_query():
    db = SessionLocal()
    try:
        books = db.query(Book).limit(5).all()
        for book in books:
            print(f"{book.id}: {book.title} (Downloads: {book.download_count})")
            for author in book.authors:
                print(f"   Author: {author.name}")
    finally:
        db.close()

if __name__ == "__main__":
    test_query()
