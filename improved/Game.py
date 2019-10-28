#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import traceback
import numpy as np
import _Bot

class Game(_Bot.Mixin):
    """ Class which implements the bots parsing game bot
        Github project: https://github.com/markusfisch/bots
    """
    def __init__(self, host, port):
        # connect to server
        self._socket = socket.socket()
        self._socket.connect((host, port))
        self.f = self._socket.makefile()

        # view specific variables
        self.view = None
        #self.get_view()

        # count every turn from connecting to server
        self.turn_counter = 0
    
    def __enter__(self):
        return self

    def get_view(self):
        view = self.f.readline().strip("\n")
        self.fov = len(view)
        
        if not view:
            return False

        for _ in range(2, len(view)+1):
            line = self.f.readline().strip("\n")
            if not line:
                return False
            view += line
        self.view = np.array(list(view)).reshape(self.fov, self.fov)
        return True

    def send_command(self, command):
        try:
            self._socket.send(bytearray(command[0], "utf-8") if command[0] != '\n' else b'^')
            return True
        except Exception as e:
            print(e)
            traceback.print_exc()
            return False
    
    def __exit__(self, exc_type, exc_value, traceback):
        self._socket.close()
