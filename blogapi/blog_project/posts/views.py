# posts/views.py
from django.contrib.auth import get_user_model # new
from rest_framework import viewsets # new
from .models import Post
from .serializers import PostSerializer, UserSerializer # new
from .permissions import IsAuthorOrReadOnly # new


 
class PostViewSet(viewsets.ModelViewSet): # new
    permission_classes = (IsAuthorOrReadOnly,) # new
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet): # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer