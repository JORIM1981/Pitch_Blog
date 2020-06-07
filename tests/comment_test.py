import unittest
from app.models import Comment, User
from app import db


class CommentTest(unittest.TestCase):
    def setUp(self):

        self.new_comment = Comment(
            id=1, comment='Test comment', user=self.user_midumbi, pitch_id=self.new_pitch)

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment, 'Test comment')
        self.assertEquals(self.new_comment.user, self.user_midumbi)
        self.assertEquals(self.new_comment.pitch_id, self.new_pitch)


class CommentTest(unittest.TestCase):
    def setUp(self):
        self.user_midumbi = User(
            username='midumbi', password='midumbi', email='midumbi.webdev@gmail.com')
        self.new_pitch = Pitch(
            id=1, title='Test', content='This is a test pitch', user_id=self.user_midumbi.id)
        self.new_comment = Comment(
            id=1, comment='This is a test comment', user_id=self.user_midumbi.id, pitch_id=self.new_pitch.id)

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()
        Comment.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment, 'This is a test comment')
        self.assertEquals(self.new_comment.user_id, self.user_essy.id)
        self.assertEquals(self.new_comment.pitch_id, self.new_pitch.id)

    def test_save_comment(self):
        self.new_comment.save()
        self.assertTrue(len(Comment.query.all()) > 0)

    def test_get_comment(self):
        self.new_comment.save()
        got_comment = Comment.get_comment(1)
        self.assertTrue(get_comment is not None)
