from rest_framework import status
from rest_framework.test import APITestCase

from .models import Course

class CourseApiTests(APITestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title="Python",
            description="Основы Python",
            price="120.00",
            duration=3,
        )

    def test_create_and_list_courses(self):
        response = self.client.post(
            "/api/courses/",
            {
                "title": "Django",
                "description": "Создание сайтов",
                "price": "150.00",
                "duration": 4,
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "Django")
        self.assertEqual(self.client.get("/api/courses/").status_code, status.HTTP_200_OK)

    def test_retrieve_update_and_delete_course(self):
        detail_url = f"/api/courses/{self.course.id}/"
        self.assertEqual(self.client.get(detail_url).status_code, status.HTTP_200_OK)

        update_response = self.client.patch(
            detail_url,
            {"title": "Новый Python"},
            format="json",
        )
        self.assertEqual(update_response.status_code, status.HTTP_200_OK)
        self.assertEqual(update_response.data["title"], "Новый Python")

        delete_response = self.client.delete(detail_url)
        self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Course.objects.filter(id=self.course.id).exists())

    def test_invalid_course_data_returns_errors(self):
        response = self.client.post(
            "/api/courses/",
            {
                "title": "   ",
                "description": "Некорректный курс",
                "price": "-1.00",
                "duration": 0,
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("title", response.data)
        self.assertIn("price", response.data)
        self.assertIn("duration", response.data)

    def test_filter_by_price_and_search_by_title(self):
        Course.objects.create(
            title="Django REST",
            description="API түзүү",
            price="150.00",
            duration=2,
        )

        price_response = self.client.get("/api/courses/?price=120.00")
        search_response = self.client.get("/api/courses/?search=Django")

        self.assertEqual(len(price_response.data), 1)
        self.assertEqual(price_response.data[0]["title"], "Python")
        self.assertEqual(len(search_response.data), 1)
        self.assertEqual(search_response.data[0]["title"], "Django REST")