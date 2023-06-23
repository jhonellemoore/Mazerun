# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 01:54:31 2020

@author: Lael Charles
"""

WALL_MAP = '''\
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WP......W....WW......WW.....WW......WW.W
WW.WW.WWW..W..W..WW.....W...W....WW....W
W...W..VW..W.WW...W..W..WWWWWWWWv.W.WW.W
WW..W......W....W....W.....HWW.V..W....W
WW...WW.WWWWW.WW.WW.WWW.WW....W...WWW..W
W..W....W...H.......W...WW..WWW........W
W.WW........W...W..WWW..W....W..WWWW.WWW
W......WWW..W.WWWW....WW....WWW...WWV..W
W..WWH......W....W.WW.....W.....WWW....W
WW.WWWWWWWW.W....W....WWWWW.......W....W
W......VW..W...WW....W...W..WW.....W..HW
W..W.......W.W.WWW...WWWW....W....WWWWWW
W..WWWW......W.WWWW..WH.......W....W...W
WW....WWWW...WV..WWWWWWWW..WWWWW..WW...W
Wh....W..W.WWW...WH.....W.....WWWWWWWW.W
WWWW..WW...W...WW..W..WWWWW...W..W.....W
W.....W...WW...W..W..W..VWW..WW.....WWWW
W...WWWWW...W...WWWWW.WW.WW...WWW.....VW
WWW...W.....WW......W....W.WW...W.WWWW.W
WH...WWW..WWW..WWW..WWWWH............W.W
W..WWW..W......W...WW..W.W...WW..WW.WW.W
W......W...WH........W.W...W............
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
\
''' 

WALL_MAP = '''\
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WP......WV...WW......WW.....WW......WW.W
WW.WW.WWW..W..W..WW.....W...W....WW....W
W...W..VW..W.WW...W..W..WWWWWWWWv.W.WW.W
WW.....HW..W....W....W.....HWW.V..W....W
WW...WW.W.WWW.WW.WW.WWW.WW....W...WWW..W
W..W....W...H.......W...WW..WWW........W
WWWW........W...W..WWW..W....W..WWWW.WWW
W....W.WWW..W.WWWW....WW....WWW...WWV..W
W..WWH......W....W.WW.....W.....WWW..W.W
WW.WWWWWWWWVW....W....WWWWW.......W.W..W
W......HW..W...WW....W...W..WW........HW
W..W.......W.W.WWW...WWWW....W....WWWWWW
W..WWWW......W.WWWW..WH.......W....W...W
WW....WWWW...WV..WWWWWWWW..WWWWW..WW...W
Wh....W..W.WWW....H.....W.....WWWWWWWW.W
WWWW..WW...W...WW..W..WWWWW...W..W.....W
WH.....W...WW...W..W...WH.....W.....WWWW
W...WWWWW...W...WWWW..WW.WW...WWW.....VW
WWW...W.....WW......WW...W.WW...W.WWWW.W
WH...WWW..WWW..WWW..WWWWH............W.W
W..WWW..W......W...WW..W.W...WW..WW.WW.W
W......W...WH........W.W...W....WW......
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
\
''' 

#ORIGINAL FROM BESTVERSIONSOFARCODE
WALL_MAP = '''\ 
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
W.......W....WW...W..WW.....WW......WW..
WW.WWWWWW..W..W..WW.....W...W....WW....W
W..W...VW..W.WW...W..W..WWWWWWWWv.W.WW.W
WW.WWW..W..W....W....W......WW.V..W..W.W
WW...W....WW.WW.WW.WWW.WW....W...WWW...W
W..W...WW..VH.......W...WW..WWW........W
W.WWWWWW....W..WW..WWW..W....W..WWWWWWWW
W......WWW..W.WWWW....WW...WWWW...WWV..W
W..WWH......W....W.WW.....W.....WWW....W
WW.WWWW.WWW.W....W....WWWWW.......W....W
W........W..WWWWWW....W...W..WWW......HW
W..W..WWWW.....WH....WWWW....W....WWWWWW
W..WWWW.....WW.WWWW..WH.......W....W...W
WW....WWWW...WV..W..WWWWW..WWWW....W...W
Wh....W..W.WWW...WH.....W.....WWWWWW...W
WWWW..WW...W...WW..W..WWWWW...W..W.....W
W.....W...WW...W..W..W..VWW..WW.....WWWW
W...WWWWW...W...WWWWW.WW.WW...WWW.....VW
WWW...W.....WW......W....W.WW...WWWWWW.W
WH......WWWWW..WWW..WWWW......WV.....W.W
W..WWW..W......W...WW..W.W.WW.W..WWWWW.W
WP.........W...WH........W.W..W........W 
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
\
'''

# BLANK_WALL_MAP = '''\
# WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
# W......................................W
# W......................................W
# W......................................W
# W......................................W
# W......................................W
# W......................................W
# W......................................W
# W......................................W
# W......................................W
# W......................................W
# W......................................W
# W......................................W
# W......................................W
# W......................................W
# W......................................W
# W......................................W
# W......................................W
# W......................................W
# W......................................W
# W......................................W
# W......................................W
# W.......................................
# WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
# \
# ''' 