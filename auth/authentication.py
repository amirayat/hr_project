from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from auth.oauth2 import create_access_token
from db.db_admin import find_admin
from db.hash import Hash


router = APIRouter(
  tags=['authentication']
)

@router.post('/token')
def get_token(request: OAuth2PasswordRequestForm = Depends()):
  """
  rest post method to authenticate admin
  """
  user = find_admin(request.username)
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
  if not Hash.verify(user["password"], request.password):
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
  
  access_token = create_access_token(data={'sub': user["username"]})

  return {
    'access_token': access_token,
    'token_type': 'bearer'
  }
