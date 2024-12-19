import unittest
from app import app

class TestLibraryAPI(unittest.TestCase):
    def test_book_crud(self):
        with app.test_client() as client:
            # Create a book
            response = client.post('/books', json={"title": "Book 1", "author": "Author 1"},
                                   headers={"Authorization": "token123"})
            self.assertEqual(response.status_code, 201)

            # Get books
            response = client.get('/books')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.json['books']), 1)

            # Update a book
            response = client.put('/books/1', json={"title": "Updated Book 1"},
                                  headers={"Authorization": "token123"})
            self.assertEqual(response.status_code, 200)

            # Delete a book
            response = client.delete('/books/1', headers={"Authorization": "token123"})
            self.assertEqual(response.status_code, 204)
