from rest_framework import pagination

#自定义分页类
class MyPageNumberPagination(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = "size"
    max_page_size = 10
    page_query_param = "page"