# test cases for rsvp
import os
import unittest

from datetime import date
from uuid import UUID

from rsvp import RSVP


class TestRSVP(unittest.TestCase):
    """
    RSVP Test Cases
    """

    def setUp(self):
        os.environ["RSVP_TEST_CONFIG"] = 'true'
        self.rsvp_object = RSVP()

        event_source = 'PythonPune MeetUp'
        self.new_event_rsvp = self.rsvp_object.create_rsvp_store(
            event_source, **{
                'event_slug': 'python-pune-meetup',
                'event_start_date': date.today()
            }
        )

    def tearDown(self):
        del os.environ["RSVP_TEST_CONFIG"]
        self.rsvp_object.delete_rsvp_store(self.new_event_rsvp)
        del self.rsvp_object

    def test_create_delete_rsvp_store(self):
        """
        test create_rsvp store
        """
        self.assertIsInstance(UUID(self.new_event_rsvp), UUID)

    def test_add_members(self):
        """
        test add_members
        """
        rsvp_members = ['Rahul', 'Shyam', 'Anu', 'Isha']

        add_result = self.rsvp_object.add_members(self.new_event_rsvp, rsvp_members)
        self.assertTrue(add_result)


def rsvp_test_suit():
    """
    Test Suit
    """
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestRSVP))
    return suite
