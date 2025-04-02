class ManagerHomeBase:
    @staticmethod
    def logo():
        """
        主页左上角logo
        @return:
        """
        return '//*[@class="hd_logo"]'

    @staticmethod
    def level_one_menu(level_one_menu_name):
        """
        左侧一级菜单名称
        @param level_one_menu_name: 菜单名称
        @return:
        """
        return f'//div[@class="gj_nav el-col el-col-0"]//span[text()="{level_one_menu_name}"]//parent::li'

    @staticmethod
    def level_two_menu(level_one, level_two):
        """
        左侧菜单，选中一级菜单后显示的二级菜单
        @param level_two:
        @param level_one:
        @return:
        """
        return f'//div[@class="gj_nav el-col el-col-0"]//span[@class="nav_child_item" and text()="{level_two}"]' \
               f'//parent::li//ancestor::span//following-sibling::span[@class="nav_item_txt" and text()="{level_one}"]' \
               f'//parent::li//span[@class="nav_child_item" and text()="{level_two}"]//parent::li'

    @staticmethod
    def switch_menu_span():
        return '//div[@class="change_menu"]//span[contains(text(),"菜单切换")]'

    @staticmethod
    def batch_closure_tips_step_1():
        return '//button//span[text()="下一步"]'

    @staticmethod
    def confirm_no_ticket_mask():
        return '//div[@class="confirm-no-ticket-mask"]'

    @staticmethod
    def class_notice():
        """
        进入主页后的课程弹窗关闭按钮
        @return:
        """
        return '//div[@class="liveImg"]//div[@class="self-mask-close"]'

    @staticmethod
    def password_notice():
        """
        进入主页后提示修改密码的弹窗关闭按钮
        @return:
        """
        return '//button[text()="暂不修改"]'

    @staticmethod
    def tex_period_end_notice():
        return '//div[@class="AD GGTS"]//span[text()="我知道了"]'

    @staticmethod
    def role_notice():
        """
        主页角色弹窗，取消按钮
        @return:
        """
        return f'//div[@class="role-tip"]//button//span[text()="关闭"]//parent::button'

    @staticmethod
    def big_announcement():
        return '//*[text()="公告发布"]//parent::div[contains(@class,"announcement")]//following-sibling::button/i'

    @staticmethod
    def skip_new_menu():
        return '//span[@class="jump"]'

    @staticmethod
    def float_notice():
        return '//div[@class="el-notification__closeBtn el-icon-close"]'

    @staticmethod
    def group_switch():
        return '//div[@class="el-input el-input--small el-input--suffix is-focus"]'

    @staticmethod
    def group_select(group_name):
        return f'//div[@class="el-scrollbar"]//li//span[contains(text(),"{group_name}")]'

    @staticmethod
    def top_label(label):
        return f'//div[@class="gj_con_hd clearfix"]//span[@title="{label}"]'

    @staticmethod
    def announcement():
        return '//div[@class="AD GGTS"]//span'

    @staticmethod
    def click_company_droplist():
        """选择圈子，先点击圈子下拉列表"""
        return '//div[@class="hd_company"]'

    @staticmethod
    def select_company(company_name):
        """选择圈子"""
        return f'//div[@class="el-select-dropdown el-popper"]//li//span[contains(text(),"{company_name}")]'

    @staticmethod
    def user_avatar():
        return '//span[contains(@class,"el-dropdown-link el-dropdown-selfdefine")]'

    @staticmethod
    def avatar_button(button_name):
        return f'//span[text()="{button_name}"]'

    @staticmethod
    def ask_robot():
        return '//div[@class="smartAsk-pop-content"]//span[text()="我知道了"]'

    @staticmethod
    def consultation():
        return '//div[@class="zixun-pop-content"]//span[text()="我知道了"]'

    @staticmethod
    def top_tag(tag):
        return f'//span[contains(@class,"tag")][contains(text(),"{tag}")]'

    @staticmethod
    def tag_close_button(tag):
        return f'//span[contains(@class,"tag")][@title="{tag}"]//following-sibling::i[contains(@class,"close")]'

    @staticmethod
    def tag_refresh_button(tag):
        return f'//span[contains(@class,"tag")][@title="{tag}"]//following-sibling::i[contains(@class,"refresh")]'

    @staticmethod
    def notice_area():
        return '//div[@aria-label="公告发布"]//i'

    @staticmethod
    def assistant_div():
        return '//div[@class="zwy-assistant"]'
