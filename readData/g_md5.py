#! usr/bin/env python3
#-*- coding:utf-8 -*-
import hashlib,time
def g_md5(userId,m):
    m5 = hashlib.md5()
    m_data = userId.encode('utf-8') + str(int(time.time())).encode('utf-8') + m.encode('utf-8')
    m5.update(m_data)
    return m5.hexdigest()