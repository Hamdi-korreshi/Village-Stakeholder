from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.http import JsonResponse;
from .models import Village  # Import your Village model

class VillageTestCase(TestCase):
    def setUp(self):
        """Set up test data before each test."""
        self.User = get_user_model()  # Retrieve the custom user model

        # Create a test user (the owner of the first village)
        self.user = self.User.objects.create_user(
            username="owneruser", 
            email="owneruser@example.com",
            password="password123"
        )

        # Manually create 5 specific users with unique emails
        self.user1 = self.User.objects.create_user(
            username="Alice", 
            email="alice@example.com", 
            password="password1"
        )
        self.user2 = self.User.objects.create_user(
            username="Bob", 
            email="bob@example.com", 
            password="password2"
        )
        self.user3 = self.User.objects.create_user(
            username="Charlie", 
            email="charlie@example.com", 
            password="password3"
        )
        self.user4 = self.User.objects.create_user(
            username="David", 
            email="david@example.com", 
            password="password4"
        )
        self.user5 = self.User.objects.create_user(
            username="Eve", 
            email="eve@example.com", 
            password="password5"
        )

        # Create individual villages for each user with no residents
        self.village1 = Village.objects.create(owner=self.user1, description="Alice's Village")
        self.village2 = Village.objects.create(owner=self.user2, description="Bob's Village")
        self.village3 = Village.objects.create(owner=self.user3, description="Charlie's Village")
        self.village4 = Village.objects.create(owner=self.user4, description="David's Village")
        self.village5 = Village.objects.create(owner=self.user5, description="Eve's Village")

        # Add multiple residents to Alice's village
        self.village1.residents.add(self.user2, self.user3, self.user4, self.user5)

    def test_personal_village_members(self):
        """Test the personal_village_members function to check the user's village residents."""
        self.client.login(username="Alice", password="password1")  # Log in user

        # Simulate a GET request to the personal_village_members endpoint
        response = self.client.get(reverse('personal_village_members'))  # Replace with the actual URL name

        # Assert the response status code
        self.assertEqual(response.status_code, 200)

        # Parse the JSON response
        response_data = response.json()

        # Assert the response data contains the expected residents
        expected_residents = [
            {"user_id": self.user2.id, "username": self.user2.username},
            {"user_id": self.user3.id, "username": self.user3.username},
            {"user_id": self.user4.id, "username": self.user4.username},
            {"user_id": self.user5.id, "username": self.user5.username},
        ]
        self.assertEqual(response_data["members"], expected_residents)
