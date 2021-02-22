from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.views import APIView


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'name':'shivendu',
            'age':20
        }
        return Response(data)


# def test_view(request):
#     data={
#         'name':'shivendu',
#         'age':20
#     }
#     return JsonResponse(data)
