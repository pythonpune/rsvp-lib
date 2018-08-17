# RSVP Main File
from uuid import uuid4

from rsvp.helpers import RSVP_Helpers
from rsvp.constants import MEMBER_KEYS
from rsvp.exceptions import EXCEPTION_MESSAGES


class RSVP(object):
    """
    RSVP Main Class
    """

    def __init__(self):
        """
        constructor
        """
        self.helpers = RSVP_Helpers()
        self.store_file_name = ''

    def _locate_file(self, event_id):
        all_files = self.helpers.get_all_store_files()
        required_file = [file for file in all_files if event_id in file]
        if isinstance(required_file, list) and len(required_file) > 0:
            return required_file[0]
        return ''

    def create_rsvp_store(self, *source, **event_details):
        """
        Creates a new RSVP store object
        :param source: Source details
            - rsvp_source           string
        :param event_details: Event detail kwargs
            - event_slug            slug
            - event_name            string
            - event_description     string
            - event_start_date      datetime
            - event_end_date        datetime
            - event_members         list

        :return: event_id           uuid as string
        """
        if not isinstance(source, (list, tuple)) and len(source) > 0:
            raise Exception(EXCEPTION_MESSAGES['SOURCE_NOT_FOUND'])

        rsvp_source = source[0]
        if not event_details.get('event_slug'):
            raise Exception(EXCEPTION_MESSAGES['EVENT_SLUG_NOT_FOUND'])

        if not event_details.get('event_start_date'):
            raise Exception(EXCEPTION_MESSAGES['START_DATE_NOT_FOUND'])

        event_id = uuid4()
        event_master_dict = dict()
        event_master_dict['event_id'] = str(event_id)
        event_master_dict['event_source'] = rsvp_source
        event_master_dict['event_slug'] = event_details['event_slug']
        event_master_dict['event_name'] = event_details.get('event_name')
        event_master_dict['event_description'] = event_details.get('event_description')
        event_master_dict['event_start_date'] = str(event_details['event_start_date'])
        event_master_dict['event_end_date'] = str(event_details.get('event_end_date'))
        event_master_dict['event_members'] = event_details.get('event_members', [])

        self.store_file_name = str(event_id) + '.' + event_details['event_slug']
        if self.helpers.save_rsvp(self.store_file_name, event_master_dict):
            return str(event_id)
        return

    def delete_rsvp_store(self, event_id):
        """
        Deletes RSVP store file
        :param event_id: uuid as string
        :return: boolean
        """
        file_to_delete = self._locate_file(event_id)
        if file_to_delete and self.helpers.delete_store_file(file_to_delete):
                return True
        return False

    def add_members(self, event_id, members):
        """
        Add members to event
        :param event_id: uuid as string
        :param members: list of names (string)
        :return: boolean
        """
        file_to_append = self._locate_file(event_id)
        event_data = self.helpers.load_file_data(file_to_append)
        member_keys_dict = {key: False for key in MEMBER_KEYS}
        members_list = [{member: member_keys_dict} for member in members]
        event_data['event_members'].extend(members_list)
        if self.helpers.save_rsvp(self.store_file_name, event_data):
            return True
        return False
