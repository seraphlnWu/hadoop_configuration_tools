#!/usr/bin/env python
# coding=utf8

import os
import sys

from optparse import OptionParser

from config import USAGE
from config import CONF_MAPPER
from config import DEFAULT_SERVERS
from config import SERVICE_MAPPER
from config import PATH_MAPPER
from config import SERVICE_PATH


def init_options():
    ''' init the options. '''
    parser = OptionParser()
    parser.add_option(
        "-f",
        "--files",
        dest="config_files",
        type="str",
        default="",
        help="files to push. use ',' to split each file if you need more than 1 file.",
    )
    parser.add_option(
        "-t",
        "--type",
        dest="file_type",
        type="str",
        default="",
        help="To push hadoop conf files or hbase conf files or other kinds of files if needed",
    )
    parser.add_option(
        "-d",
        "--destination",
        dest="destination_servers",
        type="str",
        default="",
        help="To choose those servers to update config files, use ',' to split files if need more than 1 servers.",
    )

    parser.add_option(
        "-s",
        "--services",
        dest="services",
        type="str",
        default="",
        help="To choose those services after push config files. use ',' to split files if need more than 1 services.",
    )

    options, args = parser.parse_args()

    return options, args


def prepare_works():
    '''
        parse the options, define the files to put, services to restart.
    '''
    options, args = init_options() 

    if not options.file_type:
        sys.stdout.write("Error: file_type must be choosed")
        sys.stdout.write("USAGE: %s" %(USAGE, ))
        sys.stdout.flush()
        sys.exit(0)

    if options.config_files:
        o_files = map(lambda x: x.strip(), options.config_files.split(','))
    else:
        o_files = CONF_MAPPER.get(options.file_type, [])

    if options.destination_servers:
        o_servers = map(lambda x: x.strip(), options.destination_servers.split(','))
    else:
        o_servers = DEFAULT_SERVERS

    if options.services:
        o_services = map(lambda x: x.strip(), options.services.split(','))
    else:
        o_services = SERVICE_MAPPER

    return (options.file_type, o_files, o_servers, o_services)


def main():
    ''' main function to put files.  '''
    f_type, o_files, o_servers, o_services = prepare_works()

    file_path = PATH_MAPPER[f_type]
    if o_servers:
        for cur_server in o_servers:
            print 'Here in %s' % (cur_server, )

            if o_files:
                print 'Putting Configuration files...'
                for cur_file in o_files:
                    print 'The target file is %s.' % (cur_file, )
                    os.system('scp %s%s root@%s:%s' % (
                        file_path,
                        SERVICE_MAPPER.get(cur_file, ''),
                        cur_server,
                        file_path,
                    ))
                print 'Done of Putting Configuration files.'

            if o_services:
                print 'Restarting services...'
                for cur_services in o_services:
                    print 'The target service is %s.' % (cur_services, )
                    os.system("ssh root@%s '%s restart'" % (
                        cur_server,
                        SERVICE_PATH,
                    ))
                print 'Done of Restarting services...'

            print 'Done of Server: %s' % (cur_server, )
    else:
        pass


if __name__ == '__main__':
    main()
