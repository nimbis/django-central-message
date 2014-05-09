from pytz import UTC
from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

from messages_extends.models import Message


class CentralMessage(Message):
    """
    Control object for Messages.  Generates UserMessages from
    admin page
    """

    generated = models.BooleanField(
        help_text="If true, user notices have already been generated.",
        default=False)

    generated_on = models.DateTimeField(
        help_text="Timestamp notices were generated on.",
        blank=True, null=True)

    def generate(self):
        """
        Generate a Message per User, associate it with a CentralUserMessage.
        Called from admin action.
        """

        users = User.objects.all()
        for user in users:
            if user == self.user:
                # Admin owner already has this message
                continue
            # Create a new Message for this User
            a_message = Message.objects.create(
                user=user,
                message=self.message,
                level=self.level,
                extra_tags=self.extra_tags,
                expires=self.expires)
            # Associate said message with this CentralMessage.  Enables
            # cascading deletion
            CentralUserMessage.objects.create(
                master=self,
                message=a_message)
        self.generated = True
        self.generated_on = datetime.now(tz=UTC)
        self.save()


class CentralUserMessage(models.Model):
    """
    Associating object model with messages_extras.Message, and CentralMessage.
    Maybe extended in the future to include other status information.
    """

    # SET_NULL avoids recursive .delete() between CentralUserMessage and
    # Message
    message = models.OneToOneField(
        Message,
        null=True,
        on_delete=models.SET_NULL)

    master = models.ForeignKey(
        CentralMessage,
        verbose_name="Master message",
        help_text="CentralMessage which contains message.",
        related_name="%(app_label)s_%(class)s_related")


@receiver(pre_delete, sender=CentralUserMessage)
def message_delete(sender, instance, **kwargs):
    """
    Because ForeignKey is on "wrong side", we have to manually cascade delete.
    """

    instance.message.delete()
