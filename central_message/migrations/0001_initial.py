# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('messages_extends', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='CentralMessage',
            fields=[
                ('message_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='messages_extends.Message')),
                ('generated', models.BooleanField(default=False, help_text=b'If true, user notices have already been generated.')),
                ('generated_on', models.DateTimeField(help_text=b'Timestamp notices were generated on.', null=True, blank=True)),
            ],
            options={
            },
            bases=('messages_extends.message',),
        ),
        migrations.CreateModel(
            name='CentralUserMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('master', models.ForeignKey(related_name='central_message_centralusermessage_related', verbose_name=b'Master message', to='central_message.CentralMessage', help_text=b'CentralMessage which contains message.')),
                ('message', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='messages_extends.Message')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
