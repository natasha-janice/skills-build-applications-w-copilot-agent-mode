from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        for model in [Activity, Leaderboard, User, Team, Workout]:
            for obj in model.objects.all():
                if obj.pk:
                    obj.delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Team Marvel')
        dc = Team.objects.create(name='DC', description='Team DC')

        # Create users (superheroes)
        users = []
        users.append(User(name='Spider-Man', email='spiderman@marvel.com', team=marvel, is_superhero=True))
        users.append(User(name='Iron Man', email='ironman@marvel.com', team=marvel, is_superhero=True))
        users.append(User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc, is_superhero=True))
        users.append(User(name='Batman', email='batman@dc.com', team=dc, is_superhero=True))
        for user in users:
            user.save()

        # Create workouts
        workouts = []
        workouts.append(Workout(name='Pushups', description='Upper body workout', difficulty='Easy'))
        workouts.append(Workout(name='Running', description='Cardio workout', difficulty='Medium'))
        workouts.append(Workout(name='Deadlift', description='Strength workout', difficulty='Hard'))
        for workout in workouts:
            workout.save()

        # Create activities
        users = list(User.objects.all())
        workouts = list(Workout.objects.all())
        activities = []
        activities.append(Activity(user=users[0], workout=workouts[0], date=timezone.now(), duration_minutes=30, points=50))
        activities.append(Activity(user=users[1], workout=workouts[1], date=timezone.now(), duration_minutes=45, points=70))
        activities.append(Activity(user=users[2], workout=workouts[2], date=timezone.now(), duration_minutes=60, points=100))
        activities.append(Activity(user=users[3], workout=workouts[0], date=timezone.now(), duration_minutes=20, points=30))
        for activity in activities:
            activity.save()

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, total_points=120)
        Leaderboard.objects.create(team=dc, total_points=130)

        # Ensure unique index on email
        with connection.cursor() as cursor:
            cursor.db_conn['user'].create_index('email', unique=True)

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
