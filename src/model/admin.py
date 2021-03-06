from tortoise import Model, fields


class Administrator(Model):
    id = fields.IntField(pk=True, description="primary key")
    username = fields.CharField(max_length=32, description="管理员账户名称")
    login_password = fields.CharField(max_length=64, description="密码")

    class Meta:
        table_description = "管理员"
        table = "administrator"


class User(Model):
    username = fields.CharField(null=True, max_length=20, description="用户名")
    type = fields.BooleanField(default=False, description="用户类型 True:超级管理员 False:普通管理员")
    password = fields.CharField(null=True, max_length=255)
    nickname = fields.CharField(default='binkuolo', max_length=255, description='昵称')
    u_phone = fields.CharField(null=True, description="手机号", max_length=11)
    u_email = fields.CharField(null=True, description='邮箱', max_length=255)
    full_name = fields.CharField(null=True, description='姓名', max_length=255)
    u_status = fields.IntField(default=0, description='0未激活 1正常 2禁用')
    head_img = fields.CharField(null=True, max_length=255, description='头像')
    sex = fields.IntField(default=0, null=True, description='0未知 1男 2女')
    remarks = fields.CharField(null=True, max_length=30, description="备注")
    client_host = fields.CharField(null=True, max_length=19, description="访问IP")
    create_time = fields.DatetimeField(auto_now_add=True, description='创建时间')
    update_time = fields.DatetimeField(auto_now=True, description="更新时间")

    class Meta:
        table_description = "用户"
        table = "user"
