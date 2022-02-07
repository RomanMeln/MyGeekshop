from django.test import TestCase

from authapp.models import ShopUser



class TestUserManagement(TestCase):
    username = 'django'
    password = 'geekbrains'
    email = 'django@gb.local'



    def setUp(self) -> None:

        self.user = ShopUser.objects.create_superuser(
            username=self.username,
            password=self.password,
            email=self.email,
        )

    def test_user_login(self):
        # главная без логина
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        self.assertTrue(response.context['user'].is_anonymous)

        # данные пользователя
        self.client.login(username=self.username, password=self.password)

        # логинимся
        response = self.client.get('/auth/login/')
        self.assertFalse(response.context['user'].is_anonymous)


    def test_user_logout(self):
        # главная после логина
        self.client.login(username=self.username, password=self.password)
        response = self.client.get('/auth/login/')

        self.assertFalse(response.context['user'].is_anonymous)

        self.client.get('/auth/logout/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/')
        self.assertTrue(response.context['user'].is_anonymous)
