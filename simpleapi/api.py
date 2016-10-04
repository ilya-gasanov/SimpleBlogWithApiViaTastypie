from tastypie.resources import ModelResource
from tastypie.authorization import DjangoAuthorization
from tastypie.validation import Validation
from tastypie.serializers import Serializer
from tastypie import fields
from django.contrib.auth.models import User
from tastypie.authentication import BasicAuthentication
from blog.models import Post


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        fields = ['username']
        allowed_methods = []


class EntryResource(ModelResource):

    owner = fields.ForeignKey(UserResource,'owner')

    class Meta:
        queryset = Post.objects.all()
        resource_name = 'blog'
        authorization = DjangoAuthorization()
        authentication = BasicAuthentication()
        validation = Validation()
        serializer= Serializer()
        list_allowed_methods = ['get','post']
        detail_allowed_methods = ['get','put','delete','patch']

    def obj_create(self, bundle, **kwargs):
        bundle.data["owner"] = bundle.request.user
        return super(EntryResource, self).obj_create(bundle, **kwargs)

    def dehydrate(self, bundle):
        bundle.data['owner'] = User.get_username(bundle.obj.owner)
        return bundle