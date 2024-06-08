from django.db import models

class Contact(models.Model):
    LINK_PRECEDENCE_CHOICES = [
        ('primary', 'Primary'),
        ('secondary', 'Secondary'),
    ]

    id = models.AutoField(primary_key=True)
    phoneNumber = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    linkedId = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='linked_contacts')
    linkPrecedence = models.CharField(max_length=9, choices=LINK_PRECEDENCE_CHOICES)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    deletedAt = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Contact {self.id}: {self.email or self.phoneNumber}"


