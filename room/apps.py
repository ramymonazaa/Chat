from django.apps import AppConfig


class RoomConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "room"
    def ready(self):
        import room.signals  # Ensure your signals are imported
