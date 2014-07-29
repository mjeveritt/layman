# Copyright 2014 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2

'''
G-Common plug-in module for layman.
'''

module_spec = {
    'name': 'g-common',
    'description': __doc__,
    'provides':{
        'g-common-module': {
            'name': 'g-common',
            'class': 'GCommonOverlay',
            'description': __doc__,
            'functions': ['add', 'supported', 'sync'],
            'func_desc': {
                'add': 'Creates the base dir and clones a g_common repository',
                'supported': 'Confirms if overlay type is supported',
                'sync': 'Performs a sync of the repository',
            },
        }
    }
}
