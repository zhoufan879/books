import redis
import unittest
import time, random

def list(conn, sort='time', asc=True):
	pass

def add_article(conn, article):
	# 文章序列
	article_id = str(conn.incr('article:incr'))

	article['id'] = article_id
	
	# 文章 Hash
	r = conn.hmset('article:' + (article_id), article)

	# 集合 - 时间 
	conn.zadd('articles:time', article['time'], article_id)

	# 集合 - 评分
	conn.zadd('articles:score', random.randrange(100), article_id)
	return r

def list_article(conn, name='score'):
	ids = conn.zrevrange('articles:' + name, 0, -1)

	list = []
	for id in ids:
		# print ( str(id, encoding = "utf-8") )
		list.append( conn.hgetall('article:' + str(id, encoding = "utf-8")) )
	return list

def voted(conn, article, user):
	# 集合 - 评分 +1
	conn.zincrby('articles:score', 1, str(article['id']) )

	# 集合 - 投票
	return conn.sadd('voted:' + str(article['id']), user['name'])

def edit(self):
	return True


###############################################################



class TestClient(unittest.TestCase):
	def setUp(self):
		self.conn = redis.StrictRedis(host='10.11.31.47', port=6381, db=0)
		# self.conn.flushdb()

	def tearDown(self):
		pass

	def test_set(self):
		r = self.conn.set('hello', 'world')
		self.assertTrue( r )

		r = self.conn.get('hello')
		self.assertEqual( r, b'world' )

	def test_add_article(self):
		_article = {
			'author': 'zhoufan879',
			'time': time.time(),
			'title': 'redis-in-action',
			'content': 'RedisConf 2016 is near! Join us in San Francisco, May 10 - 11 2016, Mission Bay Conference Center. Registration is open here. Please also consider submitting a talk.'
		}
		r = add_article(self.conn, _article)
		self.assertTrue( r )
		time.sleep(1)

		_article = {
			'author': 'Bruce Eckel',
			'time': time.time(),
			'title': 'Thinking in java',
			'content': 'java is good.'
		}
		r = add_article(self.conn, _article)
		self.assertTrue( r )
		time.sleep(1)

		_article = {
			'author': 'Behrouz A. Forouzan ',
			'time': time.time(),
			'title': 'Foundations of computer science',
			'content': 'hen diao hen diao de shu.'
		}
		r = add_article(self.conn, _article)
		self.assertTrue( r )

	def test_list_article(self):
		score_list = list_article(self.conn)
		self.assertEqual( len(score_list), 3 )
		# print ( dir(score_list) )

		time_list = list_article(self.conn, 'time')
		self.assertEqual( len(time_list), 3 )
		self.assertEqual( time_list[0][b'id'], b'3' )
		# print ( time_list )

	def test_voted(self):
		_article = {
			'id': 1
		}
		_user = {
			'name': 'zhoufan879'
		}

		r = voted(self.conn, _article, _user)
		self.assertEqual( r, 1 )



# python3 -m unittest article.TestClient

# print ( setRedis('foo', 'bar') )












