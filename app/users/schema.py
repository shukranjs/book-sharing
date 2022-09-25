from run import ma


class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("email", "created_at", "_links")

    # Smart hyperlinking
    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("user_detail", values=dict(id="<id>")),
            "collection": ma.URLFor("users"),
        }
    )
