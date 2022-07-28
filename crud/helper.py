from .models import Posts
class Helper:

    def __init__(self):
        pass
    
    def get_object(self, para_dict):
            '''
            Helper method to get the object with given post_id
            '''
            try:
                return Posts.objects.get(**para_dict)
            except Posts.DoesNotExist:
                return None