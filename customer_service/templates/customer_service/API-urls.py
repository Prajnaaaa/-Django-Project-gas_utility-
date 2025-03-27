urlpatterns += [
    path('api/requests/', ServiceRequestListCreate.as_view(), name='api_requests'),
    path('api/requests/<int:pk>/', ServiceRequestDetail.as_view(), name='api_request_detail'),
]
