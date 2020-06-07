import unittest
from app.models import Pitch, User,
from app import db


class BlogModelTest(unittest.TestCase):
    def setUp(self):
        self.user_midumbi = User(
            username='midumbi', password='midumbi', email='midumbi.webdev@gmail.com')
        self.new_pitch = Pitch(
            id=1, title='Test', content='This is a test pitch', user_id=self.user_midumbi.id)

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.title, 'Test')
        self.assertEquals(self.new_pitch.content, 'This is a test pitch')
        self.assertEquals(self.new_pitch.user_id, self.user_midumbi.id)

    def test_save_pitch(self):
        self.new_pitch.save()
        self.assertTrue(len(Pitch.query.all()) > 0)

    def test_get_pitch(self):
        self.new_pitch.save()
        got_pitch = Pitch.get_pitch(1)
        self.assertTrue(get_pitch is not None)
