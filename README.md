
# Gutendex API

Gutendex is a simple Python-based API for exploring metadata from the [Project Gutenberg](https://www.gutenberg.org/) digital library. It allows users to query book titles, authors, and subjects using a structured SQL database and provides a foundation for building more advanced search and indexing tools.

## 📦 Project Structure

```
.
├── gutendex_api.ipynb        # Jupyter notebook containing API logic and usage examples
├── gutenberg.sql             # SQL schema file for creating the database
├── gutenberg_dump.sql        # Sample data dump of Gutenberg metadata
├── gutendex.sql              # Possibly updated schema or additional data
├── requirements.txt          # Python dependencies
```

## 🚀 Features

- Query books by title, author, subject, or language
- Explore metadata such as download count and publication year
- Extensible for building full REST APIs or search interfaces

## 🔧 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/gutendex-api.git
   cd gutendex-api
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**
   - Create the database and import schema/data:
     ```bash
     sqlite3 gutenberg.db < gutenberg.sql
     # or
     sqlite3 gutenberg.db < gutenberg_dump.sql
     ```

5. **Run the notebook**
   - Open the Jupyter notebook to explore and run queries:
     ```bash
     jupyter notebook gutendex_api.ipynb
     ```

## 🧪 Example Usage

Within the notebook, you can execute SQL queries like:
```python
SELECT title, author FROM books WHERE subject LIKE '%science%';
```


## 💡 Future Improvements

- Build a RESTful API using FastAPI
- Add full-text search support
- Integrate with modern frontend for browsing and search

---

*Built with ❤️ by [Gayatri Mule]*
