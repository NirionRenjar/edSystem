from rest_framework import serializers
from .models import AccessLevels, User, Lesson, Product, ViewStatistics


class LessonSerializer(serializers.Serializer):
    class Meta:
        model = Lesson
        fields = ['title', 'url', 'Duration']

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.url = validated_data.get('url', instance.url)
        instance.Duration = validated_data.get('Duration', instance.Duration)
        instance.save()
        return instance

    def create(self, validated_data):
        return Lesson.objects.create(**validated_data)


class ViewingSerializer(serializers.Serializer):
    lesson = LessonSerializer()

    class Meta:
        model = ViewStatistics
        fields = ['viewLesson', 'viewingUser', 'viewingDuration']

    def update(self, instance, validated_data):

        instance.viewLesson = validated_data.get('viewLesson', instance.viewLesson)
        instance.viewingUser = validated_data.get('viewingUser', instance.viewingUser)
        instance.viewingDuration = validated_data.get('viewingDuration', instance.viewingDuration)
        if self.lesson['Duration'] * 0.8 <= instance.viewingDuration:
            instance['videoWatched'] = True
        else:
            instance['videoWatched'] = False
        instance.save()
        return instance

    def create(self, validated_data):
        return ViewStatistics.objects.create(**validated_data)


class ProductSerializer(serializers.Serializer):
    class Meta:
        model = Product
        fields = ['owner', 'user_access', 'lessons']

    def update(self, instance, validated_data):
        instance.owner = validated_data.get('owner', instance.owner)
        instance.user_access = validated_data.get('user_access', instance.user_access)
        instance.lessons = validated_data.get('lessons', instance.lessons)
        instance.save()
        return instance

    def create(self, validated_data):
        return Product.objects.create(**validated_data)


class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['name', 'access_level']

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.access_level = validated_data.get('access_level', instance.access_level)
        instance.save()
        return instance

    def create(self, validated_data):
        return User.objects.create(**validated_data)


class LessonListSerializer(serializers.Serializer):
    product = Product.objects.all()
    user = User.objects.all()

    class Meta:
        model = Lesson
        fields = ['user_access', 'lessons']


class LessonByProductSerializer(serializers.Serializer):
    product = ProductSerializer()
    user = UserSerializer()

    class Meta:
        model = Product
        fields = ['user_access', 'lessons']


class StatisticSerializer(serializers.Serializer):
    product = ProductSerializer()
    user = UserSerializer()

    class Meta:
        model = Product
        fields = ['user_access', 'lessons']
