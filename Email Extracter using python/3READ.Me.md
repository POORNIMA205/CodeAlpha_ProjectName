# 📧 Email Extractor using Python

## 📌 Project Overview

**Email Extractor** is a Python-based application that extracts useful information from email text and stores the extracted data in a **ChromaDB vector database** using embeddings.

The project demonstrates how unstructured email content can be processed, converted into numerical vector representations, stored in ChromaDB, and searched using semantic similarity.

The main purpose of this project is to understand how **text extraction + embeddings + vector databases** work together.

---

## 🎯 Objectives

The project is designed to:

* Extract useful information from emails.
* Store email content in a structured format.
* Generate or use embeddings for email text.
* Store embeddings in ChromaDB.
* Add metadata along with documents.
* Perform similarity searches.
* Retrieve relevant emails based on a query.
* Demonstrate basic ChromaDB operations.

---

## 🛠️ Technologies Used

| Technology            | Purpose                             |
| --------------------- | ----------------------------------- |
| Python                | Main programming language           |
| ChromaDB              | Vector database                     |
| Embeddings            | Convert text into numerical vectors |
| Sentence Transformers | Generate text embeddings, if used   |
| VS Code / PyCharm     | Development environment             |

---

## 📂 Project Structure

```text
Email Extracter using python/
│
├── sanp/
│   ├── Embeddings.py
│   ├── Email_Extractor.py
│   └── ...
│
├── chroma_db/
│   └── ChromaDB persistent database files
│
└── README.md
```

> Your actual filenames may be different. Update the structure above according to your project.

---

# ⚙️ How the Project Works

The application follows this general workflow:

```text
Email Text
    ↓
Extract Email Information
    ↓
Clean / Prepare Text
    ↓
Create Embedding
    ↓
Store in ChromaDB
    ↓
Add Metadata
    ↓
User Query
    ↓
Create Query Embedding
    ↓
Similarity Search
    ↓
Return Relevant Emails
```

---

# 🧠 What is an Embedding?

An embedding converts text into a list of numerical values called a **vector**.

For example:

```text
"Python is a programming language."
```

can be represented by a vector such as:

```text
[0.12, 0.45, 0.78, 0.91, ...]
```

In your project, you are using **20-dimensional embeddings**.

That means every document must have exactly **20 numbers** in its embedding.

For example:

```python
[
    0.12, 0.45, 0.78, 0.91, 0.11,
    0.25, 0.36, 0.47, 0.58, 0.69,
    0.70, 0.81, 0.92, 0.13, 0.24,
    0.35, 0.46, 0.57, 0.68, 0.79
]
```

---

# 🗄️ What is ChromaDB?

ChromaDB is a **vector database**.

It allows us to store:

* Documents
* Embeddings
* IDs
* Metadata

For example:

```text
ID: doc1

Document:
"Machine learning is a branch of AI."

Embedding:
[0.12, 0.45, 0.78, ...]

Metadata:
{
    "category": "AI",
    "author": "John",
    "year": 2024
}
```

---

# 🏷️ Metadata

Metadata provides additional information about an email/document.

Example:

```python
metadatas = [
    {
        "category": "AI",
        "author": "John",
        "year": 2024
    },
    {
        "category": "Programming",
        "author": "Alice",
        "year": 2023
    }
]
```

For an email project, metadata could instead contain:

```python
{
    "sender": "example@gmail.com",
    "subject": "Project Update",
    "date": "2026-08-25",
    "category": "Work"
}
```

This makes it easier to filter and organize emails.

---

# 📦 Installation

## Step 1: Install Python

Make sure Python is installed.

Check using:

```bash
python --version
```

---

## Step 2: Install ChromaDB

```bash
pip install chromadb
```

---

## Step 3: Install Sentence Transformers

If your project generates embeddings using Sentence Transformers:

```bash
pip install sentence-transformers
```

If you previously received:

```text
ModuleNotFoundError: No module named 'sentence_transformers'
```

this command fixes that issue.

---

## Step 4: Verify Installation

Run:

```bash
python -c "import chromadb; print('ChromaDB installed successfully')"
```

For Sentence Transformers:

```bash
python -c "from sentence_transformers import SentenceTransformer; print('Sentence Transformers installed successfully')"
```

---

# ▶️ How to Run the Project

Open the project folder in VS Code.

For example:

```bash
cd "C:\Users\poornima\Email Extracter using python"
```

Go to the folder containing your Python file:

```bash
cd sanp
```

Then run:

```bash
python Embeddings.py
```

Alternatively, if your file is named differently:

```bash
python Email_Extractor.py
```

---

# 🔢 ChromaDB Collection

The project creates a persistent ChromaDB database:

```python
client = chromadb.PersistentClient(
    path="./chroma_db"
)
```

Then a collection is created:

```python
collection = client.get_or_create_collection(
    name="my_collection_20d"
)
```

The collection acts like a container for your documents, embeddings, and metadata.

---

# ➕ Adding Data

Documents, IDs, embeddings, and metadata are added using:

```python
collection.add(
    ids=ids,
    documents=documents,
    embeddings=embeddings,
    metadatas=metadatas
)
```

For example:

```text
ID          Document                    Category
------------------------------------------------
doc1        Machine Learning...         AI
doc2        Python...                   Programming
doc3        ChromaDB...                 Database
```

---

# 🔍 Searching the Collection

A query embedding can be used to find similar documents:

```python
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=3
)
```

If the query is:

```text
"What is machine learning?"
```

ChromaDB compares the query embedding with the stored embeddings and returns the most similar documents.

---

# 📖 Reading Stored Data

To retrieve documents:

```python
results = collection.get()

print(results)
```

To retrieve specific documents:

```python
results = collection.get(
    ids=["doc1", "doc2"]
)

print(results)
```

---

# 🔎 Filtering Using Metadata

You can search based on metadata.

For example:

```python
results = collection.get(
    where={
        "category": "AI"
    }
)

print(results)
```

This returns documents whose metadata contains:

```text
category = AI
```

---

# ✏️ Updating Data

An existing document can be updated:

```python
collection.update(
    ids=["doc1"],
    documents=[
        "Machine Learning is a field of Artificial Intelligence."
    ],
    metadatas=[
        {
            "category": "AI",
            "author": "John",
            "year": 2025
        }
    ]
)
```

---

# 🗑️ Deleting Data

A document can be removed using:

```python
collection.delete(
    ids=["doc3"]
)
```

---

# 🔢 Counting Documents

To check how many documents are stored:

```python
print(collection.count())
```

---

# 📊 Main ChromaDB Operations

| Operation | ChromaDB Method       |
| --------- | --------------------- |
| Add data  | `collection.add()`    |
| Read data | `collection.get()`    |
| Search    | `collection.query()`  |
| Update    | `collection.update()` |
| Delete    | `collection.delete()` |
| Count     | `collection.count()`  |

---

# 📧 Example Email Data

An email can be represented like this:

```python
document = """
Subject: Project Meeting

The project meeting will be held tomorrow
at 10 AM. Please bring the project report.
"""
```

Metadata:

```python
metadata = {
    "sender": "manager@example.com",
    "subject": "Project Meeting",
    "category": "Work",
    "date": "2026-08-25"
}
```

The email text is stored as the **document**, while information such as sender, subject, category, and date is stored as **metadata**.

---

# 💡 Example Use Case

Suppose your database contains 10 emails.

A user searches:

```text
"Show me emails about project meetings"
```

The system:

1. Takes the query.
2. Converts the query into an embedding.
3. Compares it with stored email embeddings.
4. Finds the most semantically similar emails.
5. Returns the matching emails.
6. Displays their metadata such as sender, subject, and date.

This is more powerful than simply searching for an exact keyword.

---

# ⚠️ Important: Embedding Dimension

If your collection is created using **20-dimensional embeddings**, every embedding supplied to that collection must contain exactly **20 values**.

For example:

```text
20 values → ✅ Correct

19 values → ❌ Error

384 values → ❌ Error
```

This is especially important if you change embedding models.

For example, `all-MiniLM-L6-v2` normally produces **384-dimensional embeddings**, not 20-dimensional embeddings.

Therefore, do not mix a 384-dimensional embedding with a collection expecting 20 dimensions.

---

# 🐛 Common Errors

## Error 1

```text
ModuleNotFoundError:
No module named 'sentence_transformers'
```

Solution:

```bash
pip install sentence-transformers
```

---

## Error 2

```text
Collection expecting embedding with dimension of 20,
got 384
```

This means the collection expects 20-dimensional vectors but you supplied a 384-dimensional vector.

Use embeddings with the same dimension as the collection.

---

## Error 3

```text
ModuleNotFoundError: No module named 'chromadb'
```

Solution:

```bash
pip install chromadb
```

---

# 🚀 Future Improvements

The project can be extended with:

* Gmail integration
* Outlook integration
* Automatic email extraction
* Email classification
* Spam detection
* Semantic email search
* RAG-based email assistant
* FastAPI backend
* Web interface
* User authentication
* Multiple ChromaDB collections
* Email summarization
* Automatic metadata extraction

---

# 👩‍💻 Author

**Poornima**

Python | ChromaDB | Embeddings | Vector Database

---

# 📌 Conclusion

The Email Extractor project demonstrates how email data can be processed and stored using Python and ChromaDB.

The important concepts demonstrated are:

```text
Email
 ↓
Text Extraction
 ↓
Embedding
 ↓
ChromaDB
 ↓
Metadata
 ↓
Similarity Search
 ↓
Relevant Email
```

This project provides a foundation for building an **AI-powered email search and retrieval system**.

# Author

Poornima H B

---
