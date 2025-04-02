class RenewalAnalysisBase:
    @staticmethod
    def renewal_analysis_report_type_div(name):
        return f'//div[@class="topLabel"]//div[text()="{name}"]'
