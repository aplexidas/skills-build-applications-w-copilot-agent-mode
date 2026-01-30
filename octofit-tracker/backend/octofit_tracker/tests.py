from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard


class TeamModelTest(TestCase):
    """Test Team model"""
    
    def setUp(self):
        self.team = Team.objects.create(name="Test Team")
    
    def test_team_creation(self):
        """Test team is created correctly"""
        self.assertEqual(self.team.name, "Test Team")
        self.assertEqual(str(self.team), "Test Team")


class UserModelTest(TestCase):
    """Test User model"""
    
    def setUp(self):
        self.team = Team.objects.create(name="Test Team")
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123",
            team=self.team
        )
    
    def test_user_creation(self):
        """Test user is created correctly"""
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.team, self.team)


class ActivityModelTest(TestCase):
    """Test Activity model"""
    
    def setUp(self):
        self.team = Team.objects.create(name="Test Team")
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123",
            team=self.team
        )
        self.activity = Activity.objects.create(
            user=self.user,
            type="Running",
            duration=30,
            calories=300
        )
    
    def test_activity_creation(self):
        """Test activity is created correctly"""
        self.assertEqual(self.activity.user, self.user)
        self.assertEqual(self.activity.type, "Running")
        self.assertEqual(self.activity.duration, 30)
        self.assertEqual(self.activity.calories, 300)


class WorkoutModelTest(TestCase):
    """Test Workout model"""
    
    def setUp(self):
        self.workout = Workout.objects.create(
            name="Morning Run",
            description="A refreshing morning run",
            difficulty="Medium"
        )
    
    def test_workout_creation(self):
        """Test workout is created correctly"""
        self.assertEqual(self.workout.name, "Morning Run")
        self.assertEqual(self.workout.description, "A refreshing morning run")
        self.assertEqual(self.workout.difficulty, "Medium")


class LeaderboardModelTest(TestCase):
    """Test Leaderboard model"""
    
    def setUp(self):
        self.team = Team.objects.create(name="Test Team")
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123",
            team=self.team
        )
        self.leaderboard = Leaderboard.objects.create(
            user=self.user,
            score=100
        )
    
    def test_leaderboard_creation(self):
        """Test leaderboard entry is created correctly"""
        self.assertEqual(self.leaderboard.user, self.user)
        self.assertEqual(self.leaderboard.score, 100)


class APIEndpointTests(APITestCase):
    """Test API endpoints"""
    
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(name="Test Team")
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123",
            team=self.team
        )
    
    def test_api_root(self):
        """Test API root endpoint returns expected links"""
        url = reverse('api-root')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('teams', response.data)
        self.assertIn('users', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('workouts', response.data)
        self.assertIn('leaderboard', response.data)
    
    def test_team_list(self):
        """Test team list endpoint"""
        url = reverse('team-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_user_list(self):
        """Test user list endpoint"""
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_activity_list(self):
        """Test activity list endpoint"""
        url = reverse('activity-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_workout_list(self):
        """Test workout list endpoint"""
        url = reverse('workout-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_leaderboard_list(self):
        """Test leaderboard list endpoint"""
        url = reverse('leaderboard-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_team(self):
        """Test creating a team via API"""
        url = reverse('team-list')
        data = {'name': 'New Team'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Team.objects.count(), 2)  # including setUp team
    
    def test_create_activity(self):
        """Test creating an activity via API"""
        url = reverse('activity-list')
        data = {
            'user': self.user.id,
            'type': 'Running',
            'duration': 30,
            'calories': 300
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Activity.objects.count(), 1)
