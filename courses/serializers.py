from rest_framework import serializers

from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(max_digits=10, decimal_places=2, min_value=0)
    duration = serializers.IntegerField(min_value=1)

    class Meta:
        model = Course
        fields = "__all__"
        read_only_fields = ("created_at",)

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Название курса не должно быть пустым.")
        return value