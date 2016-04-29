import bisect
import os
import time
import uuid
import redis

# <start id="_1314_14473_8396"/>
valid_characters = '`abcdefghijklmnopqrstuvwxyz{'             #A

def find_prefix_range(prefix):
    posn = bisect.bisect_left(valid_characters, prefix[-1:])  #B
    suffix = valid_characters[(posn or 1) - 1]                #C
    print (prefix, prefix[-1:], posn, suffix)
    return prefix[:-1] + suffix + '{', prefix + '{'           #D
# <end id="_1314_14473_8396"/>
#A Set up our list of characters that we know about
#B Find the position of prefix character in our list of characters
#C Find the predecessor character
#D Return the range
#END

# <start id="_1314_14473_8399"/>
def autocomplete_on_prefix(conn, guild, prefix):
    start, end = find_prefix_range(prefix)                 #A
    print (start, end)
    identifier = str(uuid.uuid4())                         #A
    start += identifier                                    #A
    end += identifier                                      #A
    zset_name = 'members:' + guild

    print (start, end)
    conn.zadd(zset_name, 0, start, 0, end)                 #B
    pipeline = conn.pipeline(True)
    while 1:
        try:
            pipeline.watch(zset_name)
            sindex = pipeline.zrank(zset_name, start)      #C
            eindex = pipeline.zrank(zset_name, end)        #C
            erange = min(sindex + 9, eindex - 2)           #C
            pipeline.multi()
            pipeline.zrem(zset_name, start, end)           #D
            pipeline.zrange(zset_name, sindex, erange)     #D
            items = pipeline.execute()[-1]                 #D
            break
        except redis.exceptions.WatchError:                #E
            continue                                       #E

    print (items)
    return [item for item in items if b'{' not in item]     #F


def join_guild(conn, guild, user):
    conn.zadd('members:' + guild, 0, user)

def leave_guild(conn, guild, user):
    conn.zrem('members:' + guild, user)


# conn = redis.StrictRedis(host='10.11.31.47', port=6381, db=0)

# conn.delete('members:test')
# print ( "the start/end range of 'abc' is:", find_prefix_range('abc') )
# print ()

# print ( "Let's add a few people to the guild" )
# for name in ['jeff', 'jenny', 'jack', 'jennifer']:
#     join_guild(conn, 'test', name)
# print ()
# print ( "now let's try to find users with names starting with 'je':" )
# r = autocomplete_on_prefix(conn, 'test', 'je')
# print ( r )

# print ( "jeff just left to join a different guild..." )
# leave_guild(conn, 'test', 'jeff')
# r = autocomplete_on_prefix(conn, 'test', 'je')
# print ( r )

# conn.delete('members:test')
