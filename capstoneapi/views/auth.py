from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from capstoneapi.models import UserType

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    '''Handles the authentication of a applicant or employer

    Method arguments:
      request -- The full HTTP request object
    '''
    username = request.data['username']
    password = request.data['password']

    # Use the built-in authenticate method to verify
    # authenticate returns the user object or None if no user is found
    authenticated_user = authenticate(username=username, password=password)
    app_user = UserType.objects.get(user=authenticated_user)
    # If authentication was successful, respond with their token
    if authenticated_user is not None:
        token = Token.objects.get(user=authenticated_user)
        data = {
            'valid': True,
            'token': token.key,
            'isEmployer': app_user.isEmployer,
            'userId': authenticated_user.id
            }
        return Response(data)
    else:
        # Bad login details were provided. So we can't log the user in.
        data = { 'valid': False }
        return Response(data)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    '''Handles the creation of a new applicant for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # Create a new user by invoking the `create_user` helper method
    # on Django's built-in User model
    new_user = User.objects.create_user(
        username=request.data['username'],
        password=request.data['password'],
        first_name=request.data['first_name'],
        last_name=request.data['last_name']
    )

    if request.data['acctype'] == 'Applicant' :
        # Now save the extra info in the levelupapi_gamer table
        applicant = UserType.objects.create(
            user=new_user,
            isEmployer = False
        )

        # Use the REST Framework's token generator on the new user account
        token = Token.objects.create(user=applicant.user)
        # Return the token to the client
        data = { 'token': token.key, 'isEmployer': False, 'userId': new_user.id }
        return Response(data, status=201)
    
    else : 
        # Now save the extra info in the levelupapi_gamer table
        employer = UserType.objects.create(
            user=new_user,
            isEmployer = True
        )

        # Use the REST Framework's token generator on the new user account
        token = Token.objects.create(user=employer.user)
        # Return the token to the client
        data = { 'token': token.key, 'isEmployer': True, 'userId': new_user.id}
        return Response(data, status=201)
