from rest_framework import serializers

from videos.models import Video

class VideoSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    is_test_field = serializers.SerializerMethodField()
    class Meta:
        model = Video
        fields = ["name", "slug", "embed", "featured", "image", "title", "is_test_field",]

    # Adding specific field to use with serializer save method
    def get_image(self, obj):
        return "/static/ang/assets/images/nature/4.jpg"

    def get_is_test_field(self, obj):
        return False