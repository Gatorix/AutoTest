class FieldBase:
    """
    外勤管理页面元素
    """

    @staticmethod
    def field_home_button(button_name):
        """
        外勤管理主页按钮元素
        @param button_name: 按钮名称
        @return:
        """
        return f'//div[@class="middle-wrap"]//button//span[text()="{button_name}"]'

    @staticmethod
    def task_type_input():
        """
        任务类型输入框
        @return:
        """
        return '//div[@aria-label="任务类型"]//div[contains(@class,"newAddType")]//input'

    @staticmethod
    def new_task_type_button():
        """
        任务类型新增按钮
        @return:
        """
        return '//div[@aria-label="任务类型"]//div[contains(@class,"newAddType")]//following-sibling::button'

    @staticmethod
    def task_type_operate(side, operate, index):
        """
        已存在的任务类型元素
        @param index: 行数
        @param operate: input、edit、delete三种操作，输入指定操作返回对应的元素
        @param side: left表示左侧列表，输入其他为右侧列表
        @return: 返回元素xpath，该xpath可定位到左侧或右侧所有的元素，在使用时需要指定是第几行的元素
        """
        if side == 'left':
            side_xpath = 'div[@class="el-col el-col-12"]'
        else:
            side_xpath = 'div[contains(@class, "second")]'
        if operate == 'input':
            operate_xpath = operate
        else:
            operate_xpath = f'i[@class="el-icon-{operate}"]'
        return f'(//div[@aria-label="任务类型"]//{side_xpath}//{operate_xpath})[{index}]'

    @staticmethod
    def header_input(label, placeholder):
        """
        外勤页面上方的条件筛选输入框，根据label名称和placeholder进行定位
        @param label: 每个输入框左侧的标签名
        @param placeholder: 输入框的占位符
        @return:
        """
        return f'//div[@class="header-wrap"]//div[contains(@class,"select_line")]' \
               f'//div//label[contains(text(),"{label}")]//following-sibling::span//input[@placeholder="{placeholder}"]'

    @staticmethod
    def search_input():
        """
        外勤页面中间的搜索框，可根据客户名称/任务名称/执行人/创建人进行搜索
        @return:
        """
        return '//div[@class="middle-wrap"]//input'

    @staticmethod
    def search_button():
        """
        搜索框旁边的搜索按钮
        @return:
        """
        return '//div[@class="middle-wrap"]//button[@class="el-button el-button--default"]'

    @staticmethod
    def task_name_in_table(task_name):
        """
        根据表格中的任务名称定位到勾选框
        @param task_name: 任务名称
        @return:
        """
        return f'//div[@class="content-wrap"]//div[@class="missionDetailContent" and contains(text(),"{task_name}")]'

    @staticmethod
    def checkbox_in_table_by_task_name(task_name):
        """
        根据表格中的任务名称定位到勾选框
        @param task_name: 任务名称
        @return:
        """
        return f'(//div[@class="content-wrap"]//div[@class="missionDetailContent" and contains(text(),"{task_name}")]' \
               f'//ancestor::td//preceding-sibling::td//span[@class="el-checkbox__input"])[1]'

    @staticmethod
    def new_task_input(label_name):
        """
        新增任务页面的输入框，根据标签名称定位
        @param label_name:
        @return:
        """
        return f'//div[@aria-label="新增任务"]//label[text()="{label_name}"]//following-sibling::div//input'

    @staticmethod
    def new_task_select_customer(customer_name):
        """
        新增任务页面选择客户的列表
        @param customer_name:
        @return:
        """
        return f'//div[@aria-label="新增任务"]//label[text()="客户"]//following-sibling::div//li[text()="{customer_name}"]'

    @staticmethod
    def new_task_select_task_type(task_type):
        """
        新增任务页面选择任务类型的列表
        @param task_type:
        @return:
        """
        return f'//div[@class="el-scrollbar"]//li//span[text()="{task_type}"]/..'

    @staticmethod
    def new_task_input_task_detail():
        """
        新增任务页面输入任务内容
        @return:
        """
        return f'//div[@aria-label="新增任务"]//textarea[contains(@placeholder,"任务内容")]'

    @staticmethod
    def new_task_buttons(button_name):
        """
        新增任务页面按钮：确定、取消
        @param button_name:
        @return:
        """
        return f'//div[@aria-label="新增任务"]//button//span[contains(text(),"{button_name[0]}")]'

    @staticmethod
    def distribution_task_buttons(button_name):
        return f'//div[@aria-label="分配人员"]//button//span[contains(text(),"{button_name[0]}")]'

    @staticmethod
    def distribution_task_input(label):
        return f'//div[@aria-label="分配人员"]//div[@class="el-form-item"]//' \
               f'label[contains(text(),"{label}")]//following-sibling::div//input'

    @staticmethod
    def distribution_task_select_org(name):
        return f'//div[contains(@id,"el-popover")]//span[contains(.,"{name}")]'

    @staticmethod
    def distribution_task_select_employee(name):
        return f'//div[@class="el-select-dropdown el-popper"]//ul//li//span[contains(text(),"{name}")]'

    @staticmethod
    def cancel_task_textarea():
        return f'//div[@aria-label="取消任务"]//textarea'

    @staticmethod
    def cancel_task_buttons(button_name):
        return f'//div[@aria-label="取消任务"]//button//span[contains(text(),"{button_name[0]}")]'

    @staticmethod
    def close_task_textarea():
        return f'//div[@aria-label="关闭任务"]//textarea'

    @staticmethod
    def close_task_buttons(button_name):
        return f'//div[@aria-label="关闭任务"]//button//span[contains(text(),"{button_name[0]}")]'

    @staticmethod
    def finish_task_textarea():
        return f'//div[@aria-label="完成任务"]//textarea'

    @staticmethod
    def finish_task_buttons(button_name):
        return f'//div[@aria-label="完成任务"]//button//span[contains(text(),"{button_name[0]}")]'

    @staticmethod
    def filed_head_filter(label, span):
        return f'//label[contains(text(),"{label}")]//following-sibling::span//span[text()="{span}"]'
