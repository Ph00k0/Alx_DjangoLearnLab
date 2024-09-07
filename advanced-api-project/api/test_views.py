from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Author
from .serializers import BookSerializer
from django.contrib.auth.models import User
from .models import Book

class BookTests(APITestCase):
    def setUp(self):
        # Create a sample author
        self.author = Author.objects.create(name="J.K. Rowling")
        # Create a sample book
        self.book = Book.objects.create(
            title="Harry Potter and the Philosopher's Stone",
            publication_year=1997,
            author=self.author
        )
          # Create a user and login
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        
        # Create test data
        self.book = Book.objects.create(title='Test Book', publication_year=2023, author='Test Author')

        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', args=[self.book.id])
        self.data = {
            'title': 'Harry Potter and the Chamber of Secrets',
            'publication_year': 1998,
            'author': self.author.id
        }

    def test_create_book(self):
        response = self.client.post(self.list_url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.latest('id').title, 'Harry Potter and the Chamber of Secrets')

    def test_read_book(self):
        response = self.client.get(self.detail_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    def test_update_book(self):
        response = self.client.put(self.detail_url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Harry Potter and the Chamber of Secrets')

    def test_delete_book(self):
        response = self.client.delete(self.detail_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books(self):
        url = f"{self.list_url}?title={self.book.title}"
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

