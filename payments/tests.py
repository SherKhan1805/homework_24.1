from rest_framework.test import APITestCase, force_authenticate
from rest_framework import status

from materials.models import Course, Lesson
from payments.models import Payments
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(name='Test', surname='Test', email='test@t.com', is_superuser=True)
        self.payment = Payments.objects.create(payment_user=1, payment_course=1, payment_method='transfer')



    def test_create_lesson(self):
        """
        Тестирование создания урока
        """
        data = {
            'name_lesson': 'Test',
            'description': 'Test',
            'link': 'https://my.sky.pro/youtube.com',
            'course_id': self.course.id,
            'author': self.user.id
        }
        self.client.force_authenticate(user=self.user)

        response = self.client.post(
            '/payments/payment_create/',
            data=data
        )
        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
