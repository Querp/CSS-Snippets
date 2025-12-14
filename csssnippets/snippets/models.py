from django.db import models
from django.core.exceptions import ValidationError

class CodingLanguage(models.TextChoices):
    HTML = 'html', 'HTML'
    CSS = 'css', 'CSS'
    JS = 'javascript', 'JavaScript'
    

class BlockType(models.TextChoices):
    TEXT = 'p', 'Paragraph'
    CODE = 'code', 'Code'
    HEADING = 'h3', 'Heading'


class Snippet(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    can_i_use_url = models.URLField(blank=True)
    code_preview = models.TextField()
    preview_language = models.CharField(
        max_length=20,
        choices=CodingLanguage.choices
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    
class SnippetBody(models.Model):
    snippet = models.ForeignKey(
        Snippet,
        on_delete=models.CASCADE,
        related_name='bodies'
    )

    block_type = models.CharField(
        max_length=10,
        choices=BlockType.choices,
        blank=True,
        null=True
    )

    language = models.CharField(
        max_length=20,
        choices=CodingLanguage.choices,
        blank=True,
        null=True
    )

    content = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def clean(self):
        if self.block_type == BlockType.CODE and not self.language:
            raise ValidationError("Code blocks require a language.")

        if self.block_type != BlockType.CODE and self.language:
            raise ValidationError("Only code blocks can have a language.")

    
    
