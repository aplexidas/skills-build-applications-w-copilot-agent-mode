from django.contrib import admin
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    """Admin interface for Team model"""
    list_display = ['id', 'name']
    search_fields = ['name']
    ordering = ['name']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Admin interface for User model"""
    list_display = ['id', 'username', 'email', 'first_name', 'last_name', 'team', 'is_active', 'date_joined']
    list_filter = ['is_active', 'is_staff', 'team', 'date_joined']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    ordering = ['-date_joined']
    readonly_fields = ['date_joined', 'last_login']
    
    fieldsets = (
        ('User Information', {
            'fields': ('username', 'email', 'first_name', 'last_name')
        }),
        ('Team', {
            'fields': ('team',)
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    """Admin interface for Activity model"""
    list_display = ['id', 'user', 'type', 'duration', 'calories', 'timestamp']
    list_filter = ['type', 'timestamp']
    search_fields = ['user__username', 'type']
    ordering = ['-timestamp']
    readonly_fields = ['timestamp']
    
    fieldsets = (
        ('Activity Information', {
            'fields': ('user', 'type', 'duration', 'calories')
        }),
        ('Timestamp', {
            'fields': ('timestamp',)
        }),
    )


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    """Admin interface for Workout model"""
    list_display = ['id', 'name', 'difficulty', 'description_preview']
    list_filter = ['difficulty']
    search_fields = ['name', 'description']
    ordering = ['name']
    
    def description_preview(self, obj):
        """Return a preview of the description"""
        return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description
    description_preview.short_description = 'Description'


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    """Admin interface for Leaderboard model"""
    list_display = ['id', 'user', 'get_user_email', 'get_team', 'score']
    list_filter = ['user__team']
    search_fields = ['user__username', 'user__email']
    ordering = ['-score']
    
    def get_user_email(self, obj):
        """Return user's email"""
        return obj.user.email
    get_user_email.short_description = 'Email'
    
    def get_team(self, obj):
        """Return user's team"""
        return obj.user.team.name if obj.user.team else 'No Team'
    get_team.short_description = 'Team'
