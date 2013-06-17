# coding=utf8

USAGE = """
    python backend.py -t <--type> [-f file1,file2,...] [-d server1,server2,...] [-s service1,service2,...]
"""

SERVICE_PATH = '/etc/init.d/'

PATH_MAPPER = {
    'hadoop': "/etc/hadoop-0.20/conf/",
    'hbase': "/etc/hbase/conf/",
}

CONF_MAPPER = {
    'hadoop': [
        'hadoop-env.sh',
        'core-site.xml',
        'mapred-site.xml',
        'hdfs-site.xml',
    ],
    'hbase': [
        'hbase-env.sh',
        'hbase-site.xml',
    ],
    'zookeeper': [
        'zoo.cfg',
    ],
}

DEFAULT_SERVERS = [
    'bjhbase01',
    'bjhbase02',
    'bjhbase03',
    'bjhbase04',
    'bjhbase05',
    'bjhbase06',
    'bjhbase07',
    'bjhbase08',
]

SERVICE_MAPPER = {
    'datanode': 'hadoop-0.20-datanode',
    'tasktracker': 'hadoop-0.20-tasktracker',
    'regionserver': 'hadoop-hbase-regionserver',
}
