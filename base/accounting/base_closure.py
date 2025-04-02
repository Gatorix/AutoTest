class ClosureBase:
    @staticmethod
    def closure_frame():
        return 'checkout-newcheckout'

    @staticmethod
    def buttons(button):
        button_id = {'一键生成': 'btn-create',
                     '测算金额': 'btn-calculate',
                     '结转到下期': 'close-period',
                     '反结账': 'unclose-period'}
        return f'//a[@id="{button_id.get(button)}"]'

    @staticmethod
    def generate_voucher_button(model):
        return f'//a[@tabtxt="{model}" and text()="生成凭证"]'

    @staticmethod
    def generate_operate_button(model, operate):
        """
        @param model:
        @param operate: setting/delete
        @return:
        """
        return f'//span[text()="{model}"]//preceding-sibling::div[contains(@class,"{operate}")]//i'

    @staticmethod
    def generate_checkbox(model):
        return f'//span[text()="{model}"]//following-sibling::span'

    @staticmethod
    def add_box_button():
        return '//li[@id="addCustomBox"]//i'

    @staticmethod
    def input_buttons(value):
        return f'//input[@type="button" and @value="{value}"]'

    @staticmethod
    def new_template_name_input():
        return '//input[@id="templateName"]'

    @staticmethod
    def new_template_operate_span(line, operate):
        """
        @param operate: add/del
        @param line:
        @return:
        """
        return f'(//span[contains(@class,"operate") and contains(@id,"{operate}")])[{line}]'

    @staticmethod
    def new_template_abstract_input(line):
        return f'(//input[@class="vcAbstract"])[{line}]'

    @staticmethod
    def new_template_direction_select(line):
        return f'(//select[@class="dircretion"])[{line}]'

    @staticmethod
    def new_template_subject_input(line):
        return f'(//input[contains(@name,"subject")])[{line}]'

    @staticmethod
    def new_template_subject_items(item):
        return f'//div[not(contains(@style,"none"))]/div[@class="droplist"]//div[contains(text(),"{item}")]'

    @staticmethod
    def new_template_rule_select(line):
        return f'(//select[@class="acRule"])[{line}]'

    @staticmethod
    def new_template_proportion_input(line):
        return f'(//input[@class="percent"])[{line}]'

    @staticmethod
    def new_template_amount_div(line):
        return f'(//input[@class="percent"])[{line}]//parent::div//following-sibling::div'

    @staticmethod
    def new_template_blank_space():
        return '//div[contains(@style,"visible")]//div[@class="ui_content"]'

    @staticmethod
    def new_template_demo_button():
        return '//span[@id="demo-wrap-text"]'

    @staticmethod
    def new_template_demo_img():
        return '//img[@class="custom-demo"]'

    @staticmethod
    def closure_period_input():
        return '//div[text()="请确认要结账到"]//input'

    @staticmethod
    def closure_period_items(item):
        return f'//div[@class="droplist"]//div[@data-value="{item}"]'

    @staticmethod
    def closure_check_buttons(button):
        button_kv = {
            '立即检测': 'startCheckBtn',
            '重新检测': 'reCheckBtn',
            '查看报告': 'checkReportBtn'
        }
        return f'//div[@id="{button_kv.get(button)}"]'

    @staticmethod
    def closure_popup_buttons(button):
        return f'//div[@class="zzsjm-tips"]//div[text()="{button}"]'

    @staticmethod
    def closure_write_off_tips():
        return f'//*[@id="writeOffTips"]//div[@id="IknowBtn"]'

    @staticmethod
    def taxes_table_input_value(line, input_id):
        return (f'//div[@class="zzsjm_table_con"]//div[@class="table_line" and @line-data="{line}"]'
                f'//input[contains(@id,"{input_id}")]')

    @staticmethod
    def taxes_table_2022_notice():
        return '//table//div[@class="notice-text"][1]'

    @staticmethod
    def taxes_table_small_profit_input():
        return '//input[@id="small-profit"]'

    @staticmethod
    def closure_current_period():
        return '//div[@id="vch-title"]//*[@id="curPeriod"]'

    @staticmethod
    def closure_reverse_period_select_input_trigger():
        return '//span[@id="unClosePeriod"]//span[@class="trigger"]'

    @staticmethod
    def closure_reverse_period_select_drop_down_items(item):
        return f'//div[@id="COMBO_WRAP"]//div[text()="{item}"]'


class RequisitionRawMaterialsBase:
    @staticmethod
    def requisition_raw_materials_frame():
        return 'productionRequisition'


class ProductionCostsBase:
    @staticmethod
    def production_costs_frame():
        return 'productionCosts'

    @staticmethod
    def production_costs_next_step():
        return f'//span[@id="stepOneNext"]'

    @staticmethod
    def production_costs_show_wg():
        return '//input[@id="showWg"]'

    @staticmethod
    def production_costs_total_jz():
        return f'//span[@id="jzTotal"]'


class SellingCostsBase:
    @staticmethod
    def selling_costs_frame():
        return 'carryoverSellingcost'

    @staticmethod
    def selling_costs_buttons(button):
        return f'//span[@id="{button}"]'


class FinalInspectionBase:
    @staticmethod
    def final_inspection_frame():
        return 'finalInspection'

    @staticmethod
    def final_inspection_re_check_button():
        return '//div[@id="reCheck"]'

    @staticmethod
    def final_inspection_checking():
        return '//div[id="checking"]'

    @staticmethod
    def final_inspection_report_span():
        return '//span[text()="记账完整性检查"]'

    @staticmethod
    def report_formula_tips_by_label(label):
        return f'//div[text()="{label}"]//following-sibling::div//div[text()="计算公式"]'

    @staticmethod
    def report_formula_tips_td_value(label, row, col):
        return f'//div[text()="{label}"]//following-sibling::div' \
               f'//div[text()="计算公式"]//following-sibling::div//tr[{row}]/td[{col}]'

    @staticmethod
    def report_formula_tips_p_value(label):
        return f'//div[text()="{label}"]//following-sibling::div' \
               f'//div[text()="计算公式"]//following-sibling::div//p'

    @staticmethod
    def report_icon_tips_by_label(label):
        return f'//*[text()="{label}"]//following-sibling::div//i'

    @staticmethod
    def report_icon_tips_value(label):
        return f'//*[text()="{label}"]//following-sibling::div//p'
