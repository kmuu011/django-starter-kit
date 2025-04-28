from .models import Memo


class MemoRepository:
  @staticmethod
  def list_by_author(author):
    return Memo.objects.filter(author=author)

  @staticmethod
  def create(author, **attrs):
    return Memo.objects.create(author=author, **attrs)
