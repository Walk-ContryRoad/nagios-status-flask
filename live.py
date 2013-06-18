#!/usr/bin/python
#
socket_path = "/opt/monitor/var/rw/live"
import operator
import ConfigParser
parser = ConfigParser.ConfigParser()
import socket
s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
s.connect(socket_path)

# Write command to socket
s.send("GET hosts\nColumns: name groups state acknowledged num_services_hard_ok num_services_hard_unknown num_services_hard_warn num_services_hard_crit\n")

# Important: Close sending direction. That way
# the other side knows, we are finished.
s.shutdown(socket.SHUT_WR)

# Now read the answer
answer = s.recv(1000000000)

# Parse the answer into a table (a list of lists)
table = [ line.split(';') for line in answer.split('\n')[:-1] ]

def matching_servers(import_text):
    temp_list = []
    import_table = import_text.split(',')
    for i in range(0, len(table)):
        if len(import_table) == len(set(table[i][1].split(',')) & set(import_table)):
            temp_list.append(table[i])
    temp_list.sort(key=operator.itemgetter(5), reverse=True)
    temp_list.sort(key=operator.itemgetter(6), reverse=True)
    temp_list.sort(key=operator.itemgetter(7), reverse=True)
    temp_list.sort(key=operator.itemgetter(2), reverse=True)
    return temp_list


def is_error(host_error):
    host_ok = '<div class="ok"><img src="icons/shield-ok.png"></img>'
    host_down = '<div class="critical_host"><img src="icons/shield-error-host.png"></img>'
    service_crit = '<div class="critical"><img src="icons/shield-error.png"></img>'
    service_warn = '<div class="warning"><img src="icons/shield-warning.png"></img>'
    service_unknown = '<div class="unknown"><img src="icons/shield-unknown.png"></img>'

    if host_error[2] == 1:
        return host_down
    elif host_error[7] >= 1:
        return service_crit
    elif host_error[6] >= 1:
        return service_warn
    elif host_error[5] >= 1:
        return service_unknown
    else:
        return host_ok


# Read from a file containing most of the html code such as stylesheets and so forth.

def painting_base():
    return None

# Creating all the html code for the rows.

def painting_rows():
    return None

# Insert hosts in the rows, check for status of the first host and ad apropriate image from that.

def painting_hosts():
    return None


def main():
    parser.read('live.conf')
    row_list = []
    hostgrp_list = []
    for i in range(0, len(parser.sections())):
        if parser.sections()[i].startswith('row'):
            row_list.append([parser.sections()[i],parser.get(parser.sections()[i],'title')])
        else:
            hostgrp_list.append([parser.get(parser.sections()[i],'row'),parser.sections()[i],matching_servers(parser.get(parser.sections()[i],'groups'))])
    print row_list
    print hostgrp_list

    


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print "\nKeyboard interrupt, hiding under my bed!"
