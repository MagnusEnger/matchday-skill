from mycroft import MycroftSkill, intent_file_handler


class Matchday(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('matchday.intent')
    def handle_matchday(self, message):
        self.speak_dialog('matchday')


def create_skill():
    return Matchday()

