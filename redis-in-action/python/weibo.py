import redis
import unittest
import time, random
import functools

def redis_conn(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		conn = redis.StrictRedis(host='10.11.31.47', port=6381, db=0)
		# args.conn = redis.StrictRedis(host='10.11.31.47', port=6381, db=0)
		# args = (222)
		if len(args)==1:
			new_args = (conn, args[0])
		elif len(args)==2:
			new_args = (conn, args[0], args[1])
		elif len(args)==3:
			new_args = (conn, args[0], args[1], args[2])
		elif len(args)==4:
			new_args = (conn, args[0], args[1], args[2], args[3])
		else:
			new_args = (conn)

		return func(*new_args, **kw)
	return wrapper
	
@redis_conn
def create_user(conn, user):
	user_incr = conn.incr('weibo.user:incr')
	user['time'] = time.time()
	pipeline = conn.pipeline(True)
	pipeline.zadd('weibo.users', user['time'], user_incr)
	pipeline.hmset('weibo.user:' + str(user_incr), user)
	pipeline.execute()
	return user_incr

@redis_conn
def send_msg(conn, msg):
	msg_id = conn.incr('weibo.user:incr')
	msg['time'] = time.time()
	pipeline = conn.pipeline(True)
	pipeline.zadd('weibo.status:user:' + str(msg['uid']), msg['time'], msg_id)
	pipeline.hmset('weibo.status:' + str(msg_id), msg)
	pipeline.zadd('weibo.home:' + str(msg['uid']), msg['time'], msg_id)
	pipeline.zrevrange('followed:' + str(msg['uid']), 0, -1)
	r = pipeline.execute()

	followed_list = r[-1]
	# 我懒，就不写神马延迟发送了
	for item in followed_list:
		pipeline.zadd('weibo.home:' + str(item), msg['time'], msg_id)
	pipeline.execute()
	return True

@redis_conn
def home_list(conn, uid, pageNum, cn=20):
	return conn.zrevrange('weibo.home:' + str(msg['uid']), (pageNum-1) * cn, ((pageNum-1) * cn + cn - 1 ) )

@redis_conn
def follow(conn, uid, me):
	pipeline = conn.pipeline(False)
	pipeline.zadd('weibo.followed:' + str(uid), time.time(), me)
	pipeline.zadd('weibo.following:' + str(me), time.time(), uid)
	pipeline.zrevrange('weibo.status:user:' + str(uid), 0, 20)
	r = pipeline.execute()[-1]

	for msg in r:
		pipeline.zadd('weibo.home:' + str(me), msg['time'], uid)
	pipeline.execute()

	return True

@redis_conn
def unfollow(conn, uid, me):
	pipeline = conn.pipeline(False)
	pipeline.zrem('weibo.followed:' + str(uid), me)
	pipeline.zrem('weibo.following:' + str(me), uid)
	pipeline.zrevrange('weibo.status:user:' + str(uid), 0, 20)
	r = pipeline.execute()[-1]

	pipeline.zrem('weibo.home:' + str(me), r)
	return True


# uid = create_user({
# 	'name': 'zhoufan879',
# 	'age': 28,
# 	'job': 'IT',
# 	'address': '深圳彩田路'
# })

# print ( uid )
# uid = create_user({
# 	'name': 'james',
# 	'age': 38,
# 	'job': 'coder',
# 	'address': '上海市北京西路'
# })
# print ( uid )

# uid = create_user({
# 	'name': 'annie',
# 	'age': 24,
# 	'job': '前台小妹',
# 	'address': '火星'
# })
# print ( uid )

##############################################################################################################

follow(546789322, 546789323)

follow(546789322, 546789324)

##############################################################################################################
# uid = 1
# sid = send_msg({
# 	'message': 'Hello World 1',
# 	'uid': uid
# })


##############################################################################################################
##############################################################################################################






















