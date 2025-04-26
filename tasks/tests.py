from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile


# tests.py
class IndexViewTest(TestCase):
    def test_get_request(self):
        response = self.client.get('/index/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Validación de archivos")

    def test_post_request(self):
        content = b"a1,b1,c1,d1,e1\n,a2,b2,c2,d2,e2\n"
        file = SimpleUploadedFile(
            "test.txt", content, content_type="text/plain")

        response = self.client.post('/index/', {'file': file})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('content' in response.context)

    def test_post_no_file(self):
        response = self.client.post('/index/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['error_modal'])

    def test_post_valid_file(self):
        content = b"54563,pepe@gmail.com,CC,600000,Valor"
        file = SimpleUploadedFile(
            "test.txt", content, content_type="text/plain")

        response = self.client.post('/index/', {'file': file})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('content' in response.context)
