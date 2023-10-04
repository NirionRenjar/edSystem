from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LessonListSerializer, LessonByProductSerializer, StatisticSerializer, ProductSerializer, \
    LessonSerializer
from .models import Product, Lesson


@api_view(['GET'])
def product_api(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def lesson_api(request):
    lesson = Lesson.objects.all()
    serializer = LessonSerializer(lesson, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def lesson_list_api(request):
    lesson = Lesson.objects.all()
    serializer = LessonListSerializer(lesson, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def lesson_by_product_api(request):
    lesson = Lesson.objects.all()
    serializer = LessonByProductSerializer(lesson, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def statistic_api(request):
    lesson = Lesson.objects.all()
    serializer = StatisticSerializer(lesson, many=True)
    return Response(serializer.data)



