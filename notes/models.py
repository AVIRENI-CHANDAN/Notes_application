from django.db import models
import hashlib

# Create your models here.


class UserModel(models.Model):
    fullname = models.CharField(
        verbose_name="Full Name", max_length=200, null=False, editable=True, help_text="Full name of the user"
    )
    username = models.CharField(
        verbose_name="User Name", max_length=200, unique=True, null=False, editable=False, help_text="The user name of user"
    )
    password = models.CharField(
        verbose_name="Password", max_length=200, null=False, editable=False, help_text="Password of the user, used for login."
    )
    email = models.EmailField(
        verbose_name="Email", null=False, unique=True, editable=True, help_text="Email of the user"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False, help_text="The date time of the user created"
    )
    isActive = models.BooleanField(
        default=True, editable=True, help_text="To note the inactive users"
    )

    class Meta:
        verbose_name = "NotesModel"
        verbose_name_plural = "NotesModels"
    
    def save(self, *args, **kwargs):
        self.password = hashlib.sha3_256(self.password.encode('utf-8')).hexdigest()
        self.username = hashlib.sha3_256(self.username.encode('utf-8')).hexdigest()
        super(UserModel,self).save(*args, **kwargs)

    def __str__(self):
        return self.fullname

    def get_absolute_url(self):
        return reverse("NotesModel_detail", kwargs={"pk": self.pk})
