# -*- coding:utf8 -*-

import os , random, subprocess


music_list = os.path.join(os.path.abspath(os.path.curdir), 'music_list.lst')
music_dir = os.path.join(os.path.abspath(os.path.curdir), 'music')


if os.path.exists(music_list):
    os.remove(music_list)

all_music = [os.path.join(music_dir, music) for music in os.listdir(music_dir)]
random.shuffle(all_music)

content = '\n'.join(all_music)

open(music_list, 'w').write(content)

cmd = 'mplayer -playlist %s' % (music_list,)
a = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
a.wait()
