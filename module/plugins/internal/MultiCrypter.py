# -*- coding: utf-8 -*-

from module.plugins.internal.SimpleCrypter import SimpleCrypter


class MultiCrypter(SimpleCrypter):
    __name__    = "MultiCrypter"
    __type__    = "hoster"
    __version__ = "0.07"
    __status__  = "stable"

    __pattern__ = r'^unmatchable$'
    __config__  = [("activated"         , "bool"          , "Activated"                       , True     ),
                   ("use_premium"       , "bool"          , "Use premium account if available", True     ),
                   ("folder_per_package", "Default;Yes;No", "Create folder for each package"  , "Default")]

    __description__ = """Multi decrypter plugin"""
    __license__     = "GPLv3"
    __authors__     = [("Walter Purcaro", "vuolter@gmail.com")]


    def init(self):
        self.PLUGIN_NAME = self.pyload.pluginManager.crypterPlugins.get(self.classname)['name']


    def _log(self, level, plugintype, pluginname, messages):
        messages = (self.PLUGIN_NAME,) + messages
        return super(MultiCrypter, self)._log(level, plugintype, pluginname, messages)
