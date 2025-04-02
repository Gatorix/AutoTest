import os
import pytest

from utils.file_utils import get_project_path

from utils.cloud_hub import send_results

from config.config import MULTIPROCESS, RERUNS, RERUNS_DELAY, DEFAULT_TEST_FEATURE, DEFAULT_TEST_MODEL
from utils.random_data import random_string_generator

if __name__ == '__main__':
    try:
        build_num = os.environ['BUILD_NUMBER']
    except KeyError:
        build_num = random_string_generator(str_size=5, start_with='')

    try:
        test_models = os.environ['test_model']
    except KeyError:
        test_models = DEFAULT_TEST_MODEL

    try:
        test_features = os.environ['test_feature']
    except KeyError:
        test_features = DEFAULT_TEST_FEATURE

    allure_dir = fr'{get_project_path()}\allure\allure_result\{build_num}'

    feature_mark_kv = {
        '管家': 'manager',
        '管家-菜单遍历': 'manager_menu',
        '管家-系统设置': 'manager_system',
        '管家-系统设置-部门职员': 'manager_system_department_staff',
        '管家-登录': 'manager_login',
        '管家-财务管理': 'manager_finance',
        '管家-财务管理-收款跟进': 'manager_finance_follow_up',
        '管家-财务管理-收款审核': 'manager_finance_audit',
        '管家-外勤管理': 'manager_field',
        '管家-客户管理': 'manager_customer',
        '管家-客户管理-客户': 'manager_customer_manage',
        '管家-客户管理-流失管理': 'manager_customer_lost_manage',
        '管家-客户管理-合同': 'manager_customer_contract',
        '管家-客户管理-合同发票': 'manager_customer_invoice',
        '管家-客户管理-服务到期明细': 'manager_customer_change_record',
        '管家-客户管理-客户物品管理': 'manager_customer_items',
        '管家-工商服务': 'manager_business',
        '管家-工商服务-服务管理': 'manager_business_manage',
        '管家-工商服务-工商年报': 'manager_business_report',
        '管家-代账服务': 'manager_agency',
        '管家-代账服务-服务管理': 'manager_agency_service',
        '管家-代账服务-收票': 'manager_agency_invoice',
        '管家-代账服务-记账': 'manager_agency_bookkeeping',
        '会计': 'accounting',
        '会计-菜单遍历': 'accounting_menu',
        '会计-菜单遍历-V1.0': 'accounting_menu_old',
        '会计-录凭证': 'accounting_voucher',
        '会计-智能记账': 'accounting_smart_bookkeeping',
        '会计-智能记账-票据附件': 'accounting_smart_bookkeeping_invoice',
        '会计-智能记账-销项票': 'accounting_smart_bookkeeping_out_invoice',
        '会计-智能记账-银行对账单': 'accounting_smart_bookkeeping_bank_bill',
        '会计-智能记账-进项票': 'accounting_smart_bookkeeping_income_invoice',
        '会计-设置': 'accounting_settings',
        '会计-设置-凭证字': 'accounting_settings_voucher_type',
        '会计-设置-科目': 'accounting_settings_subject',
        '会计-设置-辅助核算': 'accounting_settings_sub_account',
        '会计-设置-辅助核算列表': 'accounting_settings_sub_account_details',
        '会计-设置-币别': 'accounting_settings_currency',
        '会计-设置-票据凭证模板': 'accounting_settings_invoice_voucher_template',
        '会计-工资': 'accounting_salary',
        '会计-报表': 'accounting_reports',
        '会计-报表-资产负债表': 'accounting_reports_balance',
        '会计-报表-利润表': 'accounting_reports_income',
        '会计-报表-现金流量表': 'accounting_reports_cash_flow',
        '会计-查凭证': 'accounting_lookup_voucher',
        '会计-存货': 'accounting_inventory',
        '会计-存货-基础设置': 'accounting_inventory_setting',
        '会计-存货-存货管理': 'accounting_inventory_manage',
        '会计-存货-入库单': 'accounting_inventory_warehousing_entry',
        '会计-存货-出库单': 'accounting_inventory_outbound_entry',
        '会计-存货-存货汇总表': 'accounting_inventory_summary',
        '会计-存货-存货收发明细表': 'accounting_inventory_detail',
        '会计-存货-导出': 'accounting_inventory_export',
        '会计-首页': 'accounting_home',
        '会计-固定资产': 'accounting_fixed_asset',
        '会计-固定资产-导出': 'accounting_fixed_asset_export',
        '会计-固定资产-折旧明细表': 'accounting_fixed_asset_depreciation_detail',
        '会计-固定资产-折旧汇总表': 'accounting_fixed_asset_depreciation_summary',
        '会计-固定资产-卡片': 'accounting_fixed_asset_card',
        '会计-固定资产-资产类别': 'accounting_fixed_asset_class',
        '会计-结账': 'accounting_closure',
        '会计-结账-结账流程': 'accounting_closure_process',
        '会计-结账-自定义模板': 'accounting_closure_templates',
        '会计-结账-结转': 'accounting_closure_carry_forward',
        '会计-结账-期末检查': 'accounting_closure_check',
        '会计-账簿': 'accounting_books',
        '会计-账簿-明细账': 'accounting_books_subsidiary_ledger',
        '会计-账簿-总账': 'accounting_books_general_ledger',
        '会计-账簿-凭证汇总表': 'accounting_books_voucher_summary',
        '会计-账簿-科目余额表': 'accounting_books_balance',
        '会计-账簿-数量金额明细账': 'accounting_books_quantity_amount_ledger',
        '会计-账簿-数量金额总账': 'accounting_books_quantity_amount_general_ledger',
        '会计-账簿-多栏账': 'accounting_books_multi_column_ledger',
        '会计-账簿-核算项目余额表': 'accounting_books_sub_accounting_balance',
        '会计-账簿-核算项目明细表': 'accounting_books_sub_accounting_detail',
    }

    if test_models == '全部':
        run_marks = 'ui and not proj or api and not proj'

    elif test_models == '仅执行P1级别用例':
        run_marks = 'p1'

    elif test_models == '仅执行菜单遍历':
        run_marks = 'menu'

    elif test_models == '仅执行管家用例':
        run_marks = 'manager and not proj'

    elif test_models == '仅执行会计用例':
        run_marks = 'accounting and not proj'

    elif test_models == '仅执行发版内容':
        run_marks = 'proj'

    elif test_models == '仅执行指定功能':
        run_marks = None
        raw_features = test_features[1:-1].split(',')
        if test_features:
            features_list = []
            for _ in raw_features:
                features_list.append(feature_mark_kv.get(_))
            run_marks = ' or '.join(features_list)

    elif test_models == '仅执行接口测试用例':
        run_marks = 'api and not proj'

    elif test_models == '仅执行PDF解析用例':
        run_marks = 'api_accounting_smart_bookkeeping_bank_bill_pdf_parse'

    else:
        run_marks = ''

    pytest.main(
        [
            f'-m {run_marks}',
            # '--clean-alluredir',
            '--alluredir', allure_dir,
            '-n', MULTIPROCESS,
            '--reruns', RERUNS,
            '--reruns-delay', RERUNS_DELAY,
            '--html=report.html'
        ]
    )

    send_results()

    if test_models in [
        '全部',
        '仅执行管家用例',
        '仅执行会计用例'
    ]:
        pytest.main(
            [
                '-m cleanup',
                '-n', MULTIPROCESS
            ]
        )
