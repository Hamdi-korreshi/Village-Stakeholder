from rest_framework import serializers

class ChangePasswordSerializer(serializers.Serializer):
    old_pass = serializers.CharField(required=True)
    new_pass = serializers.CharField(required=True)
    confirm_pass = serializers.CharField(required=True)

    def validate(self, data):
        if data["new_pass"] != data["confirm_pass"]:
            raise serializers.ValidationError("New passwords do not match.")
        return data