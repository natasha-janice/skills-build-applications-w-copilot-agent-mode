from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team', universe='Marvel')
        self.assertEqual(str(team), 'Test Team')
    def test_create_user(self):
        team = Team.objects.create(name='Test Team2', universe='DC')
        user = User.objects.create(email='test@example.com', name='Test User', team=team)
        self.assertEqual(str(user), 'Test User')
    def test_create_activity(self):
        team = Team.objects.create(name='Test Team3', universe='Marvel')
        user = User.objects.create(email='test2@example.com', name='Test User2', team=team)
        activity = Activity.objects.create(user=user, activity_type='run', duration=30, date='2025-11-03')
        self.assertEqual(str(activity), 'Test User2 - run')
    def test_create_workout(self):
        workout = Workout.objects.create(name='Pushups', description='Do pushups', suggested_for='strength')
        self.assertEqual(str(workout), 'Pushups')
    def test_create_leaderboard(self):
        team = Team.objects.create(name='Test Team4', universe='DC')
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(str(leaderboard), 'Test Team4 - 100')
