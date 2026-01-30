from rest_framework import serializers
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard


class TeamSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)  # Convert ObjectId to string
    
    class Meta:
        model = Team
        fields = ['id', 'name']


class UserSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)  # Convert ObjectId to string
    team_name = serializers.CharField(source='team.name', read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'team', 'team_name']


class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)  # Convert ObjectId to string
    user_username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Activity
        fields = ['id', 'user', 'user_username', 'type', 'duration', 'calories', 'timestamp']


class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)  # Convert ObjectId to string
    
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'difficulty']


class LeaderboardSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)  # Convert ObjectId to string
    user_username = serializers.CharField(source='user.username', read_only=True)
    user_email = serializers.CharField(source='user.email', read_only=True)
    team_name = serializers.CharField(source='user.team.name', read_only=True)
    
    class Meta:
        model = Leaderboard
        fields = ['id', 'user', 'user_username', 'user_email', 'team_name', 'score']
