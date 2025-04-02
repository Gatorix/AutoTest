import pytest
from page.web_ui.page_login import LoginPage

# company = 'api-test-1101'
company = 'autotest_pwBOPeajBjha'


class TestReportsBalanceSheetExport(
    LoginPage
):
    @pytest.mark.test_into
    def test_balance_sheet_export_00(self):
        self.login(company=company)

    @pytest.mark.test_into
    def test_balance_sheet_export_01(self):
        self.login(company=company)

    @pytest.mark.test_into
    def test_balance_sheet_export_02(self):
        self.login(company=company)

    @pytest.mark.test_into
    def test_balance_sheet_export_03(self):
        self.login(company=company)

    @pytest.mark.test_into
    def test_balance_sheet_export_04(self):
        self.login(company=company)

    @pytest.mark.test_into
    def test_balance_sheet_export_05(self):
        self.login(company=company)

    @pytest.mark.test_into
    def test_balance_sheet_export_06(self):
        self.login(company=company)

    @pytest.mark.test_into
    def test_balance_sheet_export_07(self):
        self.login(company=company)

    @pytest.mark.test_into
    def test_balance_sheet_export_08(self):
        self.login(company=company)

    @pytest.mark.test_into
    def test_balance_sheet_export_09(self):
        self.login(company=company)
