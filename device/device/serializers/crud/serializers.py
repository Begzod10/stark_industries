from rest_framework import serializers

from device.models import Device


class DeviceSerializer(serializers.ModelSerializer):
    img_url = serializers.SerializerMethodField(read_only=True)

    def get_img_url(self, obj):
        if obj.img:
            return obj.img.url
        return None

    class Meta:
        model = Device
        fields = '__all__'
        extra_kwargs = {
            'img': {'write_only': True, 'required': False}
        }
