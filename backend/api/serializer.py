from api.models import User,TeamMember,Team,Profile
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
            
class TeamSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Team
        fields = '__all__'
        
class TeamMemberSerializer(serializers.ModelSerializer):
    team = TeamSerializer()
    user=UserSerializer()
    class Meta:
        model = TeamMember
        fields = '__all__'

#used to create access token and refresh omnce valid user found 
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        # These are claims, you can add custom claims
        if user.middle_name and user.first_name:
          token['full_name'] = user.first_name + ' ' + user.middle_name
        else:
         token['full_name'] = 'undefined name'
        token['first_name'] = user.first_name
        token['middle_name'] =  user.middle_name
        token['username'] = user.username
        token['email'] = user.email
        token['bio'] = user.profile.bio
        token['image'] = str(user.profile.image)
        token['verified'] = user.profile.verified
        # ...
        return token


#Account creation Serializers
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']

        )
       #beacuse we need to hash so this set password 
        user.set_password(validated_data['password'])
        user.save()

        return user