from fastapi import APIRouter,Depends,status,HTTPException,Response
from sqlalchemy.orm import Session
from .. import schema,models,database
from typing import List
from ..repository import blog
from ..oauth2 import get_current_user

router = APIRouter(
    #prefix = "/blog",
    #tags=['blogs']
)

@router.get("/blog",response_model=list[schema.ShowBlog],tags = ['blogs'])
def all(db : Session = Depends(database.get_db),current_user : schema.User = Depends(get_current_user)):
    return blog.get_all(db)
    # blogs = db.query(models.Blog).all()
    # return blogs


@router.post("/blog", status_code=status.HTTP_201_CREATED,tags=['blogs'])
def create_blog(request: schema.Blog, db: Session = Depends(database.get_db),current_user : schema.User = Depends(get_current_user)):
    return blog.create(request,db)


@router.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED,tags= ['blogs'])
def update(id,request : schema.Blog, db : Session = Depends(database.get_db),current_user : schema.User = Depends(get_current_user)):
    return blog.update(id,request,db)
    # blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    # if not blog.first():
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail=f"Blog with id {id} not found")
    
    # blog.update(request)
    # db.commit()
    # return 'updated'


# -----------------------
# Get single blog by id
# -----------------------
@router.get("/blog/{id}", response_model=schema.ShowBlog,tags=['blogs'])
def get_blog(id: int, db: Session = Depends(database.get_db),current_user : schema.User = Depends(get_current_user)):
    return blog.get_id(id,db)
    # blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    # if not blog:
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND,
    #         detail=f"Blog with id {id} not found."
    #     )
    # return blog


# -----------------------
# Delete blog by id
# -----------------------
@router.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT,tags=['blogs'])
def delete_blog(id: int, db: Session = Depends(database.get_db),current_user : schema.User = Depends(get_current_user)):
    return blog.Destroy_blog(id,db)
    # blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    # if not blog:
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND,
    #         detail=f"Blog with id {id} not found."
    #     )
    # db.delete(blog)
    # db.commit()
    # return Response(status_code=status.HTTP_204_NO_CONTENT)
