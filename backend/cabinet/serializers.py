from rest_framework import serializers
from profiles.models import Profile
from courses.models import Course
from subjects.models import Subject
from reviews.models import Review
from ratings.models import Rating
from django.db.models import Avg
from subjects.serializers import SubjectSerializer
from profiles.serializers import ProfileSerializer


class ProfileDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        exclude = ['id', 'user']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        
        avg_rating = instance.rating_recipients.aggregate(Avg("rating_value"))
        data["rating_value"] = avg_rating["rating_value__avg"]

        reviews = instance.review_recipients.all().values()
        data["reviews"] = reviews

        courses = instance.course_set.all().values()
        data["courses"] = courses

        return data


class NewCourseSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(read_only=True)
    profile = ProfileSerializer(read_only=True)
    
    class Meta:
        model = Course
        fields = [
            'price',
            'lesson_format',
            'subject',
            'profile'
        ]

    def create(self, validated_data):
        validated_data['subject_id'] = self.initial_data['subject']
        validated_data['profile_id'] = self.context["request"].user.profile_set.get(user=self.context["request"].user.id).id
        validated_data['price'] = self.initial_data['price']
        validated_data['lesson_format'] = self.initial_data['lesson_format']

        course = Course.objects.create(**validated_data)
    
        return course


class NewReviewSerializer(serializers.ModelSerializer):
    review_by = ProfileSerializer(read_only=True)
    review_for = ProfileSerializer(read_only=True)
    
    class Meta:
        model = Review
        fields = [
            'review_text',
            'review_by',
            'review_for'
        ]

    def create(self, validated_data):
        validated_data['review_text'] = self.initial_data['review_text']
        validated_data['review_by_id'] = Profile.objects.get(user_id=self.context["request"].user.id).id
        validated_data['review_for_id'] = Profile.objects.get(user_id=self.context["request"].parser_context['kwargs']['pk']).id

        review = Review.objects.create(**validated_data)
    
        return review


class NewRatingSerializer(serializers.ModelSerializer):
    rating_by = ProfileSerializer(read_only=True)
    rating_for = ProfileSerializer(read_only=True)
    
    class Meta:
        model = Rating
        fields = [
            'rating_value',
            'rating_by',
            'rating_for'
        ]

    def create(self, validated_data):
        validated_data['rating_value'] = self.initial_data['rating_value']
        validated_data['rating_by_id'] = Profile.objects.get(user_id=self.context["request"].user.id).id
        validated_data['rating_for_id'] = Profile.objects.get(user_id=self.context["request"].parser_context['kwargs']['pk']).id

        rating = Rating.objects.create(**validated_data)
    
        return rating
