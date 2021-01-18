import jwt
import api.models
from datetime import datetime
from graphql_jwt.settings import jwt_settings

# Fix based on: https://github.com/flavors/django-graphql-jwt/issues/241
def jwt_encode(payload, context=None):
    return jwt.encode(
        payload,
        jwt_settings.JWT_SECRET_KEY,
        jwt_settings.JWT_ALGORITHM,
    )
    
def jwt_payload(user, context=None):
    jwt_datetime = datetime.utcnow() + jwt_settings.JWT_EXPIRATION_DELTA
    jwt_expires = int(jwt_datetime.timestamp())
    
    payload = {}
    payload['sub'] = str(user.id)
    payload['sub_name'] = user.username
    payload['sub_email'] = user.email
    payload['exp'] = jwt_expires
    payload['https://hasura.io/jwt/claims'] = {}
    payload['https://hasura.io/jwt/claims']['x-hasura-allowed-roles'] = [user.profile.role]
    payload['https://hasura.io/jwt/claims']['x-hasura-default-role'] = user.profile.role
    payload['https://hasura.io/jwt/claims']['x-hasura-user-id'] = str(user.id)
    
    return payload