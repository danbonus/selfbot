from vkbottle import BaseStateGroup


class SetStatusStates(BaseStateGroup):
    GET_STATUS = 0


class StatusCreationStates(BaseStateGroup):
    GET_NAME = 1
    GET_DESCRIPTION = 2
    GET_TEXT = 3
    GET_CONFIRMATION = 4


class StatusDeletionStates(BaseStateGroup):
    GET_STATUS = 5
