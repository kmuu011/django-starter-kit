from .repository import MemoRepository


class MemoService:
  def __init__(self, repo=None):
    self.repo = repo or MemoRepository

  def list_memos(self, user):
    return (
      self.repo
      .list_by_author(user)
      .order_by('-created_at')
    )

  def create_memo(self, data, user):
    return self.repo.create(author=user, **data)
