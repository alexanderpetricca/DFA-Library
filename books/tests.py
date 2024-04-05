from django.test import TestCase
from django.urls import reverse


from .models import Book


class BookTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title = 'A Good Title',
            subtitle = 'An Excellent Subtitle',
            author = 'Tom Christie',
            isbn = '1234567890123',
        )
    

    def testBookContent(self):
        self.assertEqual(self.book.title, 'A Good Title')
        self.assertEqual(self.book.subtitle, 'An Excellent Subtitle')
        self.assertEqual(self.book.author, 'Tom Christie')
        self.assertEqual(self.book.isbn, '1234567890123')


    def testBookListView(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'An Excellent Subtitle')
        self.assertTemplateUsed(response, 'books/book_list.html')