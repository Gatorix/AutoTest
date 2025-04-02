class CreateSetBase:
    @staticmethod
    def create_mode_span(mode):
        return f'//div[@id="mode"]//span[text()="{mode}"]'

    @staticmethod
    def import_set_type(mode):
        mode_kv = {'导入第三方': 1, '从备份文件恢复账套': 2}
        return f'(//input[@type="radio"])[{mode_kv.get(mode)}]'

    @staticmethod
    def import_file_inputs(file_type):
        return f'//input[@type="file" and @accept=".{file_type}"]'

    @staticmethod
    def uploading_file_div():
        return '//div[contains(text(),"正在上传备份")]'
