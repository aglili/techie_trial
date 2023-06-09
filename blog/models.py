from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
class Base(models.Model):
    user_id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True



class Blog(Base):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to="blog/images")

    def __str__(self) -> str:
        return f"{self.author}-{self.title}"
