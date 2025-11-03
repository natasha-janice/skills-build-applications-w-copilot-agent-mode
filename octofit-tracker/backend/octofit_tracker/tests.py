from rest_framework.test import APITestCase
from django.urls import reverse
from .models import User, Team, Workout, Activity, Leaderboard

class APISmokeTest(APITestCase):
	def test_api_root(self):
		url = reverse('api-root')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)

	def test_users_endpoint(self):
		url = reverse('user-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)

	def test_teams_endpoint(self):
		url = reverse('team-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)

	def test_workouts_endpoint(self):
		url = reverse('workout-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)

	def test_activities_endpoint(self):
		url = reverse('activity-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)

	def test_leaderboards_endpoint(self):
		url = reverse('leaderboard-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
