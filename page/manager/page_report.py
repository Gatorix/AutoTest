from base.manager.base_report import RenewalAnalysisBase
from base.base_case import BaseTestCase


class RenewalAnalysisPage(RenewalAnalysisBase, BaseTestCase):
    def renewal_analysis_click_report_type_div(self, name):
        self.click(self.renewal_analysis_report_type_div(name))
