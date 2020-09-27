# imports
from rest_framework import serializers
from .models import Customer,Profile

# Customer profile serializer  
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

# Customer serializer 
class CustomerSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=False)
    class Meta:
        model = Customer
        fields = '__all__'

    #creating customer and profile in one request
    def create(self, validated_data):
        profile_data = None
        if 'profile' in validated_data:
            profile_data = validated_data.pop('profile')
            this_profile_serializer = ProfileSerializer(data=dict(profile_data))
            if this_profile_serializer.is_valid():
                profile_data = this_profile_serializer.save()
        customer = Customer.objects.create(**validated_data)
        customer.profile = profile_data
        customer.save()
        return customer

    # Updating customer and related profile.
    def update(self, instance, validated_data):
        if "profile" in validated_data:
            profile_data = validated_data.pop('profile')
            profile = instance.profile
            patientSerializer = ProfileSerializer(profile, data=profile_data, partial=True)
            patientSerializer.is_valid(raise_exception=True)
            patientSerializer.save()
        instance.name = validated_data.get('name', instance.name)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.save()
        return instance

