from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Task
from rest_framework_simplejwt.tokens import RefreshToken

class TaskAPITest(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.task = Task.objects.create(
            title="Test Task",
            description="Test Task Description",
            status="new",
            priority="medium",
            user=self.user
        )

        # Authenticate user and generate JWT token
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_create_task(self):
        """Test creating a new task"""
        url = reverse('task-list')  # Assuming 'task-list' is the name of the create and list route
        data = {
            "title": "New Task",
            "description": "New Task Description",
            "status": "new",
            "priority": "low"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "New Task")
        self.assertEqual(response.data['status'], "new")

    def test_get_task_list(self):
        """Test retrieving a list of tasks"""
        url = reverse('task-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)  # Checking if there's 1 task in the list

    def test_get_task_detail(self):
        """Test retrieving a task by ID"""
        url = reverse('task-detail', kwargs={'pk': self.task.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.task.title)

    def test_update_task(self):
        """Test updating a task by ID"""
        url = reverse('task-detail', kwargs={'pk': self.task.pk})
        data = {
            "title": "Updated Task Title",
            "description": "Updated Task Description",
            "status": "completed",
            "priority": "high"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Updated Task Title")
        self.assertEqual(response.data['status'], "completed")

    def test_delete_task(self):
        """Test deleting a task by ID"""
        url = reverse('task-detail', kwargs={'pk': self.task.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_access_denied_for_unauthenticated_users(self):
        """Test access is denied for unauthenticated users"""
        self.client.credentials()  # Remove the token
        url = reverse('task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
