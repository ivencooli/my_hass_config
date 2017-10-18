#! usr/bin/python
#coding=utf-8
musicurl="https://m7.music.126.net/20170825043803/c79496f67c935077b00e15b1211df785/ymusic/5a50/58e4/7946/fd26a60a4c7a18990044e8a5847c1d94.mp3"
hass.states.set('sensor.musicurl', musicurl,{
    'friendly_name': '网易云音乐mp3地址',

})
