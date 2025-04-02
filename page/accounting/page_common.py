from base.accounting.base_common import AccountingCommonBase

from base.base_case import BaseTestCase

VOUCHER_TEMPLATE = ['采购增值税普通发票-往来结算-采购原材料',
                    '采购增值税普通发票-往来结算-采购商品',
                    '采购增值税普通发票-往来结算-采购固定资产',
                    '采购增值税普通发票-现金-采购原材料',
                    '采购增值税普通发票-现金-采购商品',
                    '采购增值税普通发票-现金-采购固定资产',
                    '采购增值税专用发票-往来结算-采购原材料',
                    '采购增值税专用发票-往来结算-采购商品',
                    '采购增值税专用发票-往来结算-采购固定资产',
                    '采购增值税专用发票-现金-采购原材料',
                    '采购增值税专用发票-现金-采购商品',
                    '采购增值税专用发票-现金-采购固定资产',
                    '费用票据-现金-福利费',
                    '费用票据-现金-办公用品',
                    '费用票据-现金-业务招待费',
                    '费用票据-现金-交通费',
                    '费用票据-现金-运杂费',
                    '费用票据-现金-差旅费',
                    '费用票据-现金-通讯费',
                    '费用票据-现金-修理费',
                    '费用票据-现金-租赁费',
                    '费用票据-现金-物业水电费',
                    '费用票据-现金-汽车费用',
                    '费用票据-现金-服务费']

ACCOUNTING_MENU = {
    '智能记账': [
        '票据附件',
        '销项票',
        '进项票',
        '费用票',
        '银行对账单'
    ],
    '录凭证': [],
    '政府录凭证': [
        '财务凭证',
        '预算凭证'
    ],
    '查凭证': [],
    '账簿': [
        '明细账',
        '总账',
        '凭证汇总表',
        '科目余额表',
        '数量金额明细账',
        '数量金额总账',
        '多栏账',
        '核算项目余额表',
        '核算项目明细账'
    ],
    '报表': [
        '资产负债表',
        '利润表',
        '现金流量表',
        '简易现金流量表',
        '标准现金流量表',
        '纳税一览表'
    ],
    '非盈利报表': [
        '资产负债表',
        '现金流量表',
        '标准现金流量表',
        '纳税一览表',
        '业务活动表'
    ],
    '政府报表': [
        '资产负债表',
        '收入费用表',
        '净资产变动表',
        '现金流量表',
        '预算收入支出表',
        '预算结转结余变动表',
        '财政拨款预算收入支出表'
    ],
    '村集体报表': [
        '资产负债表',
        '收益及收益分配表'
    ],
    '工资': [],
    '库存': [
        '基础设置',
        '存货管理',
        '入库单',
        '出库单',
        '存货汇总表',
        '存货收发明细表'
    ],
    '资产': [
        '资产类别',
        '卡片',
        '折旧汇总表',
        '折旧明细表'
    ],
    '结账': [],
    '设置': [
        '凭证字',
        '科目',
        '币别',
        '辅助核算',
        '财务初始余额',
        '现金流量初始金额',
        '凭证模版',
        '票据凭证模版',
        '套打模版',
        '操作日志',
        '凭证回收站',
        '系统参数',
        '备份与恢复',
        '增值服务',
        '附件管理',
        '明细科目转核算项目'
    ]
}


class AccountingCommonPage(BaseTestCase, AccountingCommonBase):
    def get_floating_errors(self):
        text = self.get_text(self.accounting_floating_errors())
        self.wait(3)
        return text

    def get_floating_tips(self):
        text = self.get_text(self.accounting_floating_tips())
        self.wait(3)
        return text

    def get_floating_warning(self):
        text = self.get_text(self.accounting_floating_warning())
        self.wait(3)
        return text

    def get_all_floating_tip(self):
        text = self.get_text(self.accounting_all_floating_tips())
        self.wait(3)
        return text

    def is_floating_tip_visible(self):
        return self.is_element_visible(self.accounting_all_floating_tips())

    def multiple_assert_in_tip(self, lines):
        result = []
        tips = self.get_all_floating_tip()
        for _ in lines:
            result.append(_ in tips)
        return result

    def switch_default_frame(self):
        self.switch_to_default_content()
        self.wait(1)

    def do_accept_alert(self):
        self.accept_alert()

    def do_dismiss_alert(self):
        self.dismiss_alert()

    def close_tab_by_tab_name(self, tab):
        self.click(self.top_tabs_close_button(tab))

    def click_top_tabs_label(self, tab):
        self.click(self.top_tabs_label(tab))

    def is_top_tab_visible(self, tab):
        return self.is_element_visible(self.top_tabs_label(tab))

    def click_accounting_focus_table_buttons(self, button):
        self.click(self.accounting_focus_table_buttons(button))
        self.wait(0.5)

    def click_accounting_focus_table_close_button(self):
        self.click(self.accounting_focus_table_close_button())

    def switch_to_accounting_focus_table_inner_frame(self, title):
        self.switch_to_frame(self.accounting_focus_table_inner_frame(title))

    def click_accounting_subject_drop_down_list_item(self, subject):
        self.click(self.accounting_subject_drop_down_list_item(subject))

    def click_accounting_focus_table_input_radio_by_label(self, label):
        self.click(self.accounting_focus_table_input_radio_by_label(label))
