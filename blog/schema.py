from pydantic import BaseModel
from typing import List,Optional



class BlogBase(BaseModel):
    title: str
    body: str
    
class Blog(BlogBase):
    class Config:
        from_attributes = True



class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name : str
    email : str
    blogs : List[Blog]
    class Config():
        form_attributes = True

class ShowBlog(BaseModel):
    title: str
    body: str
    creator: Optional[ShowUser] = None
    # creator : List[ShowUser]

    class Config:
        from_attributes = True   # ✅ replaced orm_mode

class login(BaseModel):
    username : str
    password : str


class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    email : Optional[str] = None