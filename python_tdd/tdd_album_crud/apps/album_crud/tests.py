from django.test import TestCase, Client
from .models import Album

class AlbumTest(TestCase):

    # urls test
    def test_urls(self):
        c = Client()
        res = c.get('/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(c.get('/add').status_code, 302)
        self.assertEqual(c.get('/edit').status_code, 302)
        self.assertEqual(c.get('/delete').status_code, 302)

    def test_model_creation(self):
        a = Album.objects.create(title = 'License to Ill', artist = 'Beastie Boys', year = 1986)
        self.assertEqual(a.title, 'License to Ill')
        self.assertEqual(a.artist, 'Beastie Boys')
        self.assertEqual(a.year, 1986)