from .models import Blog
from rest_framework import viewsets
from .serializers import BlogSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from utils.reds_cli import search_cli


class BlogViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Blog.objects.all().order_by('-create_time')
    serializer_class = BlogSerializer


    @action(methods=['get'], detail=False)
    def search(self, request, ):
        words = request.query_params.get('words')
        ids = search_cli.query(words).end()
        queryset = self.queryset.filter(id__in=ids)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
