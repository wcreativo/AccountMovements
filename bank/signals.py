from bank.models import Client, AuditClient
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Client)
def audit_client(sender, instance, created, **kwargs):
    print("ingress signal audit client")
    # if not created:
    audit = AuditClient(
        client_id=instance.id,
        type_identification=instance.type_identification,
        number_identification=instance.number_identification,
        first_name=instance.first_name,
        last_name=instance.last_name,
        birth_date=instance.birth_date
    )
    audit.save()
