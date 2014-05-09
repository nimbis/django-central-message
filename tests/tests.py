import os
import datetime
from pytz import UTC

from django.test import TestCase
from django.contrib.auth.models import User

import messages_extends
from central_message.models import CentralMessage


class SimpleTestCase(TestCase):
    '''
    Simple test cases that verifies basic model functionality.
    '''

    def setUp(self):
        '''
        Set up the test environment.
        '''

        # enable debug mode
        os.environ["DEBUG"] = "True"
        self.user1 = User.objects.create(username="test1")
        self.user2 = User.objects.create(username="test2")
        self.user3 = User.objects.create(username="test3")

    def tearDown(self):
        '''
        Tear down the test environment.
        '''

        pass

    def test_messages(self):
        """
        Testing that .generate() creates the same number of Messages as Users
        """

        central_message = CentralMessage.objects.create(
            user=self.user1,
            message="Test Message",
            level=messages_extends.SUCCESS_PERSISTENT,
            extra_tags="",
            expires=datetime.datetime.now(tz=UTC))

        central_message.generate()

        num_users = User.objects.all()
        num_messes = messages_extends.models.Message.objects.all()
        self.assertEqual(len(num_users), len(num_messes))

        # Killing Central Message, Messages should follow
        central_message.delete()
        num_messes = messages_extends.models.Message.objects.all()
        self.assertEqual(0, len(num_messes))
