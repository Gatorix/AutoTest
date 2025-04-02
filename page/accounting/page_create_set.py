from base.accounting.base_create_set import CreateSetBase
from base.base_case import BaseTestCase


class CreateSetPage(CreateSetBase, BaseTestCase):
    def click_create_mode_span(self, mode):
        self.click(self.create_mode_span(mode))

    def click_import_set_type(self, mode):
        self.click(self.import_set_type(mode))

    def upload_file_to_import_file_inputs(self, file_type, file_path):
        self.choose_file(self.import_file_inputs(file_type), file_path)

    def wait_for_upload_finish(self):
        self.wait_for_element_not_present(self.uploading_file_div(),timeout=120)
