import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("name of song 1")