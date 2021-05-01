from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'pages': self.page.paginator.num_pages,
            'count': self.page.paginator.count, #quantity of data
            'data': data,
            "page": int(self.request.GET.get('page', 1)),
        })