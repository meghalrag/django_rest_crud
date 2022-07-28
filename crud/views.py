from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Posts
from .serializers import PostsSerializer
from django.template.defaultfilters import slugify
from .helper import Helper

class PostsListApiView(APIView):

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the Posts
        '''
        posts = Posts.objects.all()
        serializer = PostsSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PostsCreateApiView(APIView):

    # Create API
    def post(self, request, *args, **kwargs):
        '''
        Create the Post with given post data
        '''
        req = request.data
        data = {
            'title': req.get('title'), 
            'slug': slugify(req.get('title')), 
            'content': req.get('content')
        }
        serializer = PostsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostsDeleteApiView(APIView):

    #delete api
    def delete(self, request, post_id, *args, **kwargs):
        '''
        Delete the post item with given post_id if exists
        '''
        d={"id":post_id}
        instance = Helper().get_object(d)
        if not instance:
            return Response(
                {"res": "This post does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        instance.delete()
        return Response(
            {"res": "Post deleted!"},
            status=status.HTTP_200_OK
        )

class PostsUpdateApiView(APIView):

    #update api
    def put(self, request, post_id, *args, **kwargs):
        '''
        update the post item with given post_id if exists
        '''
        d={"id":post_id}
        instance = Helper().get_object(d)
        if not instance:
            return Response(
                {"res": "Post id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        req = request.data
        data = {
            'title': req.get('title'), 
            'slug': slugify(req.get('title')), 
            'content': req.get('content')
        }
        serializer = PostsSerializer(instance = instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"res": "Post updated successfully!"},
                status=status.HTTP_200_OK
            )

class PostsDetailApiView(APIView):

    #detail api
    def get(self, request, post_slug, *args, **kwargs):
        '''
        Retrieves the Todo with given post_id
        '''
        d = {"slug":post_slug}
        instance = Helper().get_object(d)
        if not instance:
            return Response(
                {"res": "Post id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = PostsSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)