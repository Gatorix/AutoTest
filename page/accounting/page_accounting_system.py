from base.accounting.base_accounting_system import AccountingStandardsForGovernmentBase

from base.base_case import BaseTestCase


class AccountingStandardsForSmallBusinessesPage:
    pass


class NewAccountingStandardsPage:
    pass


class NewAccountingStandardsForBusinessEnterprisesExecutedPage:
    pass


class NewAccountingStandardsForBusinessEnterprisesPage:
    pass


class AccountingStandardsForPrivateNonProfitOrganizationsPage:
    pass


class AccountingStandardsForVillageCollectiveEconomicOrganizationsPage:
    pass


class AccountingStandardsForGovernmentPage(BaseTestCase, AccountingStandardsForGovernmentBase):
    def click_sync_bookkeeping_button(self):
        self.click(self.sync_bookkeeping_button())


class AccountingStandardsForFarmersProfessionalCooperativesPage:
    pass
