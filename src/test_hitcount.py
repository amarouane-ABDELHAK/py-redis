from unittest.mock import patch
import unittest
import hitcount
import mockredis
class HitCountTest(unittest.TestCase):
    @patch('hitcount.r',mockredis.mock_strict_redis_client(host="0.0.0.0", port=6379, db=0))
    def testOneHit(self):
        hitcount.hit("user1")
        self.assertEqual(b'1', hitcount.gethit("user1"))
    @patch('hitcount.r',mockredis.mock_strict_redis_client(host="0.0.0.0", port=6379, db=0))
    def testTWOHits(self):
        hitcount.hit("user1")
        hitcount.hit("user1")
        self.assertEqual(b'2', hitcount.gethit("user1"))
    @patch('hitcount.r',mockredis.mock_strict_redis_client(host="0.0.0.0", port=6379, db=0))
    def testThreeHits(self):
        hitcount.hit("user1")
        hitcount.hit("user1")
        hitcount.hit("user1")
        self.assertEqual(b'3', hitcount.gethit("user1"))


if __name__=='__main__':
    unittest.main()
