from django.db import models
from django.utils.translation import gettext_lazy as _ # noqa
from django.core.validators import MinLengthValidator, MaxLengthValidator
class Hotel(models.Model):
    image = models.ImageField(
        upload_to="media/%H-%S-%M/",
        null=True, 
        blank=True,
    )
    name = models.CharField(max_length=200)
    description = models.TextField(
        validators=[MinLengthValidator(50), MaxLengthValidator(300)],
        help_text=_("what's interesting about this hotel?"),
        blank=False,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self) -> str:
        return self.name
