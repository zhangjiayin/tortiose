#-*- coding: utf-8 -*-
from tortoise.lib.pyrfeed.GoogleReader import *
gr = GoogleReader()
gr.identify('zhangjiayin99@gmail.com', 'mql860206')

if gr.login():
    print "Login OK"
else:
    print "Login KO"
#print "[%s]" % gr.get_token()

# print gr.set_read("tag:google.com,2005:reader/item/c3abf620979a5d06")
#print gr.set_unread("tag:google.com,2005:reader/item/8b1030db93c70e9e")
# print gr.del_label(entry="tag:google.com,2005:reader/item/8b1030db93c70e9e",labelname="vorkana")
#xmlfeed = gr.get_feed(feed=CONST.ATOM_PREFIXE_LABEL+'url',order=CONST.ORDER_REVERSE,start_time=1165482202,count=15)
#print xmlfeed
#print dir(xmlfeed)

#print xmlfeed.get_title()
# for entry in xmlfeed.get_entries() :
#     print "    %s\n"%entry['title']
#     print "      %s\n"%entry['published']
# continuation = xmlfeed.get_continuation()
# print "(%s)\n"%continuation
#
# while continuation != None :
#     xmlfeed = gr.get_feed(feed=CONST.ATOM_PREFIXE_LABEL+'url',order=CONST.ORDER_REVERSE,start_time=1165482202,count=2,continuation=continuation)
#     print xmlfeed
#     print xmlfeed.get_title()
#     for entry in xmlfeed.get_entries() :
#         print "    %s\n"%entry['title']
#         print "      %s\n"%entry['published']
#     continuation = xmlfeed.get_continuation()
#     print "(%s)\n"%continuation

# print gr.get_preference()
# print gr.get_subscription_list()
# print gr.get_tag_list()


# print gr.get_feed("http://action.giss.ath.cx/RSSRewriter.py/freenews",order=CONST.ORDER_REVERSE,start_time=1165482202,count=2)

#gf = GoogleFeed(xmlfeed)
#print gf.get_title()

xmlfeed = gr.get_feed(order=CONST.ORDER_REVERSE,count=3,ot=1166607627)
print xmlfeed
title = xmlfeed.get_title()
print title.encode("utf8")
for entry in xmlfeed.get_entries() :
    print "    %s %s %s\n" % (entry['google_id'].encode("utf8"),entry['published'],entry['title'].encode('utf8'))
print xmlfeed.get_continuation()

#xmlfeed = gr.get_feed(order=CONST.ORDER_REVERSE,count=3)
#print xmlfeed.get_title()
#for entry in xmlfeed.get_entries() :
#    print "    %s %s %s\n" % (entry['google_id'],entry['published'],entry['title'])
