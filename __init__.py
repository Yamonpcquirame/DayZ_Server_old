# -*- encoding: utf-8 -*-

# This file was auto generated by Bec
# Please do not remove it

from twisted.internet import task

CONFIG = {
    'interval': 1,
    'message_singular': 'Vous etes seul/e sur le serveur / You are alone on this server.',
    'base_message': 'Vous n etes pas seul/e sur le serveur / You are not alone on this server.'
}


class RobbysPlayerPlugin:
    def __init__(self, instance):
        self.bec = instance
        self.player_count_task = task.LoopingCall(self.send_player_count)
        self.player_count_task.start(CONFIG.get('interval') * 60, False)

    def get_players(self):
        return self.bec.Bec_playersconnected

    def send_player_count(self):
        player_count = len(self.get_players())
        if player_count == 0:
            return

        elif player_count == 1:
            message = CONFIG.get('message_singular')

        else:
            message = CONFIG.get('base_message')

        command_to_fire = 'say -1 {0}'.format(message)
        self.bec._Bec_queuelist.append(command_to_fire)


def start(instance):
    RobbysPlayerPlugin(instance)