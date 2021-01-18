from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType
from api.models import profile
from graphql_jwt.shortcuts import create_refresh_token, get_token
import graphene
import graphql_jwt

# Create Users
class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()

class UserProfile(DjangoObjectType):
    class Meta:
        model = profile

class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)
    profile = graphene.Field(UserProfile)
    token = graphene.String()
    refresh_token = graphene.String()

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        user = get_user_model()(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        profile_obj = profile.objects.get(user=user.id)        
        token = get_token(user)
        refresh_token = create_refresh_token(user)
        
        return CreateUser(user=user, profile=profile_obj, token=token, refresh_token=refresh_token)
    
class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    
class Query(graphene.ObjectType):
    query_placeholder = graphene.String()
    def none():
        return None