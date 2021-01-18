import graphene
import graphql_jwt
import api.schema

# Mutation for sending the data to the server.
class Mutation(api.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    pass

# Query placeholder.
class Query(api.schema.Query, graphene.ObjectType):
    pass

# Create schema
schema = graphene.Schema(query=Query, mutation=Mutation)