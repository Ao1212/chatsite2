from django.db import models

# Create your models here.

# userテーブルに対応するモデルクラスの作成
class User(models.Model):
    user_id = models.AutoField(verbose_name="user_id", primary_key=True)
    username = models.CharField(verbose_name="username", max_length=20)
    mail = models.EmailField(verbose_name="mail", unique=True)
    password = models.CharField(verbose_name="password", max_length=30)

    # このモデルを表すカラムを返す
    def __str__(self):
        return self.username

    # DBの名前のカスタム設定
    class Meta:
        db_table = "user"


# groupテーブルに対応するモデルクラスの作成
class Group(models.Model):
    group_id = models.AutoField(verbose_name="group_id", primary_key=True)
    group_name = models.CharField(verbose_name="group_name", max_length=20)

    def __str__(self):
        return self.group_name

    class Meta:
        db_table = "group"


# chat_historyテーブルに対応するモデルクラスの作成
class ChatHistory(models.Model):
    chat_id = models.BigAutoField(verbose_name="chat_id", primary_key=True)
    text = models.TextField(verbose_name="text", max_length=500)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="user_id")
    datetime = models.DateTimeField(verbose_name="datetime")
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="group_id")

    def __str__(self):
        return self.text

    class Meta:
        db_table = "chat_history"


# group_memberテーブルに対応するモデルクラスの作成
class GroupMember(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="user_id", primary_key=True)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="group_id")

    class Meta:
        db_table = "group_member"

        # 疑似的に複合キーのような状態にする
        constraints = [
            models.UniqueConstraint(fields=["user_id", "group_id"], name="belongs")
        ]
