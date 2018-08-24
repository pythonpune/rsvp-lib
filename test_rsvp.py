# test cases for rsvp
import os
import unittest

from datetime import date
from uuid import UUID

from rsvp.constants import MEMBER_KEYS
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

    def test_adjust_rsvp_state(self):
        """
        test adjust_rsvp_state
        """
        rsvp_members = ['Rahul', 'Shyam', 'Anu', 'Isha']
        add_result = self.rsvp_object.add_members(self.new_event_rsvp, rsvp_members)

        if add_result:
            rsvp_members_to_update = ['Rahul', 'Shyam']
            state1 = {MEMBER_KEYS[0]: True}

            update_result_1 = self.rsvp_object.adjust_rsvp_state(
                self.new_event_rsvp, rsvp_members_to_update, **state1
            )
            self.assertTrue(update_result_1)

            state2 = {MEMBER_KEYS[1]: True}
            update_result_2 = self.rsvp_object.adjust_rsvp_state(
                self.new_event_rsvp, rsvp_members_to_update, **state2
            )
            self.assertTrue(update_result_2)

    def test_get_rsvp_state(self):
        """
        test get_rsvp_state
        """
        rsvp_members = ['Rahul', 'Shyam', 'Anu', 'Isha']
        add_result = self.rsvp_object.add_members(self.new_event_rsvp, rsvp_members)

        if add_result:
            rsvp_members_to_update = ['Rahul', 'Shyam']
            state1 = {MEMBER_KEYS[0]: True, MEMBER_KEYS[1]: True, MEMBER_KEYS[2]: True}

            update_result_1 = self.rsvp_object.adjust_rsvp_state(
                self.new_event_rsvp, rsvp_members_to_update, **state1
            )
            self.assertTrue(update_result_1)

            result = self.rsvp_object.get_rsvp_state(
                self.new_event_rsvp, [rsvp_members_to_update[0]]
            )
            self.assertIsInstance(result, list)
            self.assertDictEqual(
                result[0], {'Rahul': {'confirm_for_seat': True,
                                      'attended_event': True, 'in_queue_waiting': True}}
            )


def rsvp_test_suit():
    """
    Test Suit
    """
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestRSVP))
    return suite
