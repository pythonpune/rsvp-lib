# RSVP Library
import os
import json


class RSVP_Helpers(object):
    """
    Helper methods for RSVP
    """

    store_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'store'
    )

    def save_rsvp(self, filename, json_data):
        """
        writes/overwrites rsvp object to the file
        :param filename: string
        :return: boolean
        """
        try:
            filename = os.path.join(self.store_path, filename)
            with open(filename, 'w') as outfile:
                json.dump(json_data, outfile)
        except Exception as e:
            raise Exception(e)
        else:
            return True

    def get_all_store_files(self):
        """
        Return list of all files in the store
        :return: list
        """
        store_files = [f for f in os.listdir(self.store_path)
                       if os.path.isfile(os.path.join(self.store_path, f))]
        return store_files

    def delete_store_file(self, filename):
        """
        Deletes event store file
        :return: boolean
        """
        try:
            os.remove(os.path.join(self.store_path, filename))
        except Exception as e:
            raise Exception(e)
        else:
            return True

    def load_file_data(self, filename):
        """
        Load json data from event file
        :param filename: string
        :return: json data (dict)
        """
        try:
            filename = os.path.join(self.store_path, filename)
            with open(filename) as infile:
                json_data = json.load(infile)
        except Exception as e:
            raise Exception(e)
        else:
            return json_data
