from base.base_case import BaseTestCase
from base.accounting.base_closure import (ClosureBase,
                                          SellingCostsBase,
                                          ProductionCostsBase,
                                          RequisitionRawMaterialsBase,
                                          FinalInspectionBase)


class ClosurePage(BaseTestCase, ClosureBase):
    def switch_to_closure_frame(self):
        self.switch_to_frame(self.closure_frame())
        self.close_closure_popups()

    def click_buttons(self, button):
        self.click(self.buttons(button))

    def click_input_buttons(self, value):
        self.click(self.input_buttons(value))

    def click_generate_voucher_button(self, model):
        self.click(self.generate_voucher_button(model))

    def click_generate_operate_button(self, model, operate):
        self.click(self.generate_operate_button(model, operate))
        self.wait(1)

    def click_generate_checkbox(self, model):
        self.click(self.generate_checkbox(model))

    def click_add_box_button(self):
        self.click(self.add_box_button())

    def type_to_new_template_abstract_input(self, line, abstract):
        self.type(self.new_template_abstract_input(line), abstract)

    def click_new_template_operate_span(self, line, operate):
        self.click(self.new_template_operate_span(line, operate))

    def select_new_template_direction_select(self, line, value):
        """
        @param line:
        @param value: credit::-1,debit::1
        @return:
        """
        self.select_option_by_text(self.new_template_direction_select(line), value)

    def new_template_select_subject(self, line, subject):
        self.type(self.new_template_subject_input(line), subject)
        self.click(self.new_template_subject_items(subject))

    def select_new_template_rule_select(self, line, value):
        """
        @param line:
        @param value: 转入、转出期末余额
        @return:
        """
        self.select_option_by_text(self.new_template_rule_select(line), value)

    def type_to_new_template_proportion_input(self, line, proportion):
        self.type(self.new_template_proportion_input(line), proportion)

    def get_new_template_amount(self, line):
        self.wait(3)
        return self.get_text(self.new_template_amount_div(line))

    def click_new_template_amount(self, line):
        self.click(self.new_template_amount_div(line))

    def type_to_new_template_name_input(self, name):
        self.type(self.new_template_name_input(), name)

    def type_template_info_single_line(self, line, abstract, direction_value, subject, rule_value, proportion):
        self.type_to_new_template_abstract_input(line, abstract)
        self.select_new_template_direction_select(line, direction_value)
        self.new_template_select_subject(line, subject)
        self.select_new_template_rule_select(line, rule_value)
        self.type_to_new_template_proportion_input(line, proportion)

    def is_amount_visible(self, line):
        return self.is_element_visible(self.new_template_amount_div(line))

    def click_new_template_demo_button(self):
        self.click(self.new_template_demo_button())

    def is_demo_img_visible(self):
        self.wait(1)
        return self.is_element_visible(self.new_template_demo_img())

    def click_closure_check_buttons(self, button):
        if button in ['查看报告', '重新检测']:
            if self.is_element_visible(self.closure_check_buttons('立即检测')):
                self.click(self.closure_check_buttons('立即检测'))
                return
        self.click(self.closure_check_buttons(button))

    def wait_for_closure_check_button_disappear(self):
        self.wait_for_element_not_visible(self.closure_check_buttons('立即检测'))
        self.wait(3)

    def close_closure_popups(self):
        if self.is_element_visible(self.closure_popup_buttons('下一步')):
            self.click(self.closure_popup_buttons('下一步'))
            self.click(self.closure_popup_buttons('知道了'))

    def get_text_from_taxes_table_input_value(self, line, input_id):
        return self.get_text(self.taxes_table_input_value(line, input_id))

    def get_text_from_taxes_table_2022_notice(self):
        return self.get_text(self.taxes_table_2022_notice())

    def check_taxes_table_small_profit_input(self):
        self.check_if_unchecked(self.taxes_table_small_profit_input())

    def uncheck_taxes_table_small_profit_input(self):
        self.uncheck_if_checked(self.taxes_table_small_profit_input())


class RequisitionRawMaterialsPage(BaseTestCase, RequisitionRawMaterialsBase):
    def switch_to_requisition_raw_materials_frame(self):
        self.switch_to_frame(self.requisition_raw_materials_frame())


class ProductionCostsPage(BaseTestCase, ProductionCostsBase):
    def switch_to_production_costs_frame(self):
        self.switch_to_frame(self.production_costs_frame())


class SellingCostsPage(BaseTestCase, SellingCostsBase):
    def switch_to_selling_costs_frame(self):
        self.switch_to_frame(self.selling_costs_frame())


class FinalInspectionPage(BaseTestCase, FinalInspectionBase):
    def switch_to_final_inspection_frame(self):
        self.switch_to_frame(self.final_inspection_frame())

    def click_final_inspection_re_check_button(self):
        self.click(self.final_inspection_re_check_button())
        self.wait(5)

    def wait_for_final_inspection_checking_disappear(self):
        self.wait_for_element_not_present(self.final_inspection_checking())

    def is_report_present(self):
        return self.is_element_visible(self.final_inspection_report_span())

    def click_report_formula_tips_by_label(self, label):
        self.click(self.report_formula_tips_by_label(label))

    def get_text_from_report_formula_tips_td_value(self, label, row, col):
        return self.get_text(self.report_formula_tips_td_value(label, row, col))

    def get_text_from_report_formula_tips_p_value(self, label):
        return self.get_text(self.report_formula_tips_p_value(label))

    def click_report_icon_tips_by_label(self, label):
        self.click(self.report_icon_tips_by_label(label))

    def get_text_from_report_icon_tips_value(self, label):
        return self.get_text(self.report_icon_tips_value(label))
