from django.db import models
from rest_framework import serializers

class Comment(models.Model):

    # def __init__(self, **kwargs) -> None:
    #     self.title = kwargs.get('title')
    #     self.content = kwargs.get('content')
    title = models.CharField( max_length = 25 )
    content = models.CharField( max_length = 25)

class CommentModelSerailzer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'title',
            'content',
        ]

        

# class CommentSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     content = serializers.CharField()

#     def create(self, serializer_obj):
#         if serializer_obj.is_valid():
#             return Comment.create(**serializer_obj.validated_data)
#         return None

#     def update(self, instance, serializer_obj):
#         if serializer_obj.is_valid():
#             instance.title = serializer_obj.validated_data.get('title')
#             instance.content = serializer_obj.validated_data.get('content')
#             instance.save
#             return instance
#         return None

# comment = Comment(title = 'title', content = 'This is the content')
# data = CommentSerializer(comment)
# print(data.data)
# data_in_json = renderers.JSONRenderer().render(data.data)
# stream = io.BytesIO(data_in_json)
# data = JSONParser().parse(stream)
# data = CommentSerializer(data)
# comment = Comment(data)
# comment = CommentSerializer.create(data)
# updated_comment = CommentSerializer.update(comment, data)

