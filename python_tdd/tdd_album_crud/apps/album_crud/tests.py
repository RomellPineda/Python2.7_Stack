from django.test import TestCase, Client

class AlbumTest(TestCase):

    # urls test
    def test_urls(self):
        c = Client()
        res = c.get('/')
        self.assertEqual(res.status_code, 200)