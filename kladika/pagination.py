from rest_framework.pagination import(
	LimitOffSetPagination,
	PageNumberPagination,
	 )

class PostLimitOffSetPagination(LimitOffSetPagination):
	default_limit = 2
	max_limit = 10