from django.core.management.base import BaseCommand # カスタムコマンドに使用する親クラス
from chatterbot.ext.django_chatterbot.models import Statement # 会話データが格納されているモデル
from . import corpus_list
from . import bot_training


class Command(BaseCommand):

    def handle(self, **options):
        statement = Statement.objects.all()
        if statement:
            statement.delete()
            self.stdout.write(self.style.SUCCESS('データを削除しました'))
        bot_training.training(corpus_list.CORPUS_LIST)
        self.stdout.write(self.style.SUCCESS('トレーニング終了'))