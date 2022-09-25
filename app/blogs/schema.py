from app import ma
from . models import Author, Blog


class AuthorSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Author

    id = ma.auto_field()
    name = ma.auto_field()
    books = ma.auto_field()


class BlogSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Blog
        include_fk = True

blog_schema = BlogSchema()
blogs_schema = BlogSchema(many=True)