############################################################################## 
#
#     Copyright 
#
#       Copyright 1997 Digital Creations, L.C., 910 Princess Anne
#       Street, Suite 300, Fredericksburg, Virginia 22401 U.S.A. All
#       rights reserved.
#
############################################################################## 
__doc__='''External Method Product Initialization
$Id: __init__.py,v 1.7 1998/05/20 21:18:49 jim Exp $'''
__version__='$Revision: 1.7 $'[11:-2]

import ExternalMethod
from ImageFile import ImageFile

classes=('ExternalMethod.ExternalMethod',)

meta_types=	{'name':'External Method',
		 'action':'manage_addExternalMethodForm'
		 },

methods={
    'manage_addExternalMethodForm':
    ExternalMethod.manage_addExternalMethodForm,
    'manage_addExternalMethod':
    ExternalMethod.manage_addExternalMethod,
    }

misc_={'function_icon':
       ImageFile('www/function.gif', globals())}


__ac_permissions__=(
    ('Add External Methods',
     ('manage_addExternalMethodForm', 'manage_addExternalMethod')),
    ('Change External Methods', ()),
    )


############################################################################## 
#
# $Log: __init__.py,v $
# Revision 1.7  1998/05/20 21:18:49  jim
# Updated permissions.
#
# Revision 1.6  1998/02/23 18:28:36  jim
# updated permissions
#
# Revision 1.5  1998/01/29 15:54:58  brian
# Added eval support
#
# Revision 1.4  1997/12/23 22:15:34  jim
# up to date with product and security layout
#
# Revision 1.3  1997/12/22 15:18:13  jeffrey
# typo fix
#
# Revision 1.2  1997/12/19 22:18:16  jeffrey
# fixes for icons
#
# Revision 1.1  1997/10/09 17:34:53  jim
# first cut, no testing
#
# Revision 1.1  1997/07/25 18:14:28  jim
# initial
#