from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Village, TestData
from rest_framework import status

class VillageTestCase(TestCase):
    def setUp(self):
        """Set up test data before each test."""
        self.User = get_user_model()

        # Create a test user (not tied to a village directly)
        self.user = self.User.objects.create_user(
            username="owneruser",
            email="owneruser@example.com",
            password="password123"
        )

        # Create 5 test users
        self.user1 = self.User.objects.create_user(
            username="Alice", email="alice@example.com", password="password1"
        )
        self.user2 = self.User.objects.create_user(
            username="Bob", email="bob@example.com", password="password2"
        )
        self.user3 = self.User.objects.create_user(
            username="Charlie", email="charlie@example.com", password="password3"
        )
        self.user4 = self.User.objects.create_user(
            username="David", email="david@example.com", password="password4"
        )
        self.user5 = self.User.objects.create_user(
            username="Eve", email="eve@example.com", password="password5"
        )

        # Create villages
        self.village1 = Village.objects.create(user=self.user1, description="Alice's Village")
        self.village2 = Village.objects.create(user=self.user2, description="Bob's Village")
        self.village3 = Village.objects.create(user=self.user3, description="Charlie's Village")
        self.village4 = Village.objects.create(user=self.user4, description="David's Village")
        self.village5 = Village.objects.create(user=self.user5, description="Eve's Village")

        # Add residents to Alice's village
        self.village1.residents.add(self.user2, self.user3, self.user4, self.user5)

    def test_personal_village_members(self):
        """Test the personal_village_members function to check the user's village residents."""
        self.client.login(username="Alice", password="password1")

        response = self.client.get('/village/v1/get-village-members/')

        self.assertEqual(response.status_code, 200)
        response_data = response.json()

        expected_residents = [
            {"user_id": str(self.user2.id), "username": self.user2.username},
            {"user_id": str(self.user3.id), "username": self.user3.username},
            {"user_id": str(self.user4.id), "username": self.user4.username},
            {"user_id": str(self.user5.id), "username": self.user5.username},
        ]

        self.assertEqual(
            sorted(response_data["members"], key=lambda x: x["user_id"]),
            sorted(expected_residents, key=lambda x: x["user_id"])
        )

    def test_rate_limiting(self):
        """Test rate limiting on the random_string view."""
        # Ensure at least one test record exists
        TestData.objects.create(name="Test", value="12345")

        url = '/village/v1/random_string/'

        # Simulate 5 allowed requests
        for _ in range(5):
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

        # 6th request should be blocked
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_429_TOO_MANY_REQUESTS)
        self.assertEqual(response.json().get('error'), 'Rate limit exceeded')
