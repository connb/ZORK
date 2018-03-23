#Code provided by Prof. Woodring

from abc import ABCMeta, abstractmethod

###########################################
# Updates the observers
#
# @param object
############################################
class Observer(object):
        __metaclass__ = ABCMeta

        @abstractmethod
        def update(self):
                pass
