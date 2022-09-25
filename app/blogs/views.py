from . import blog
from . models import Blog
from . schema import blog_schema, blogs_schema

@blog.route('/')
def blogs():
    blogs = Blog.query.all()
    return blogs_schema.dump(blogs)
