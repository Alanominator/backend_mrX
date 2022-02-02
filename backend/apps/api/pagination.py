from rest_framework.pagination import PageNumberPagination

class CPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = '_limit'
    max_page_size = 50
    page_query_param = '_page'