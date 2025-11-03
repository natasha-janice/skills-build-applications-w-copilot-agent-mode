from rest_framework import serializers
from .models import User, Team, Workout, Activity, Leaderboard

class TeamSerializer(serializers.ModelSerializer):
	id = serializers.SerializerMethodField()
	def get_id(self, obj):
		return str(obj.id) if obj.id else None
	class Meta:
		model = Team
		fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
	id = serializers.SerializerMethodField()
	team = serializers.SerializerMethodField()
	def get_id(self, obj):
		return str(obj.id) if obj.id else None
	def get_team(self, obj):
		try:
			return str(obj.team.id) if obj.team else None
		except Exception:
			return None
	class Meta:
		model = User
		fields = '__all__'

class WorkoutSerializer(serializers.ModelSerializer):
	id = serializers.SerializerMethodField()
	def get_id(self, obj):
		return str(obj.id) if obj.id else None
	class Meta:
		model = Workout
		fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
	id = serializers.SerializerMethodField()
	user = serializers.SerializerMethodField()
	workout = serializers.SerializerMethodField()
	def get_id(self, obj):
		return str(obj.id) if obj.id else None
	def get_user(self, obj):
		try:
			return str(obj.user.id) if obj.user else None
		except Exception:
			return None
	def get_workout(self, obj):
		try:
			return str(obj.workout.id) if obj.workout else None
		except Exception:
			return None
	class Meta:
		model = Activity
		fields = '__all__'

class LeaderboardSerializer(serializers.ModelSerializer):
	id = serializers.SerializerMethodField()
	team = serializers.SerializerMethodField()
	def get_id(self, obj):
		return str(obj.id) if obj.id else None
	def get_team(self, obj):
		try:
			return str(obj.team.id) if obj.team else None
		except Exception:
			return None
	class Meta:
		model = Leaderboard
		fields = '__all__'
