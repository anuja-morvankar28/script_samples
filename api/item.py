import mongoengine


class Item(mongoengine.Document):
 """
    here we defined class field names

    """
name = mongoengine.StringField(required=True)