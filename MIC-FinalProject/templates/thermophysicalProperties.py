#!/usr/bin/env python




##################################################
## DEPENDENCIES
import sys
import os
import os.path
try:
    import builtins as builtin
except ImportError:
    import __builtin__ as builtin
from os.path import getmtime, exists
import time
import types
from Cheetah.Version import MinCompatibleVersion as RequiredCheetahVersion
from Cheetah.Version import MinCompatibleVersionTuple as RequiredCheetahVersionTuple
from Cheetah.Template import Template
from Cheetah.DummyTransaction import *
from Cheetah.NameMapper import NotFound, valueForName, valueFromSearchList, valueFromFrameOrSearchList
from Cheetah.CacheRegion import CacheRegion
import Cheetah.Filters as Filters
import Cheetah.ErrorCatchers as ErrorCatchers

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '2.4.4'
__CHEETAH_versionTuple__ = (2, 4, 4, 'development', 0)
__CHEETAH_genTime__ = 1449712223.015
__CHEETAH_genTimestamp__ = 'Wed Dec 09 19:50:23 2015'
__CHEETAH_src__ = 'thermophysicalProperties.tmpl'
__CHEETAH_srcLastModified__ = 'Wed Dec 09 19:42:21 2015'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class thermophysicalProperties(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(thermophysicalProperties, self).__init__(*args, **KWs)
        if not self._CHEETAH__instanceInitialized:
            cheetahKWArgs = {}
            allowedKWs = 'searchList namespaces filter filtersLib errorCatcher'.split()
            for k,v in KWs.items():
                if k in allowedKWs: cheetahKWArgs[k] = v
            self._initCheetahInstance(**cheetahKWArgs)
        

    def respond(self, trans=None):



        ## CHEETAH: main method generated for this template
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        write(u'''/*--------------------------------*- C++ -*----------------------------------*\\
| =========                 |                                                 |
| \\\\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
|  \\\\    /   O peration     | Version:  2.4.0                                 |
|   \\\\  /    A nd           | Web:      www.OpenFOAM.org                      |
|    \\\\/     M anipulation  |                                                 |
\\*---------------------------------------------------------------------------*/
FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    location    "constant";
    object      thermophysicalProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

thermoType
{
    type            ''')
        _v = VFFSL(SL,"node.thermoType",True) # u'$node.thermoType' on line 20, col 21
        if _v is not None: write(_filter(_v, rawExpr=u'$node.thermoType')) # from line 20, col 21.
        write(u''';
    mixture         ''')
        _v = VFFSL(SL,"node.mixtureType",True) # u'$node.mixtureType' on line 21, col 21
        if _v is not None: write(_filter(_v, rawExpr=u'$node.mixtureType')) # from line 21, col 21.
        write(u''';
    transport       ''')
        _v = VFFSL(SL,"node.transportType",True) # u'$node.transportType' on line 22, col 21
        if _v is not None: write(_filter(_v, rawExpr=u'$node.transportType')) # from line 22, col 21.
        write(u''';
    thermo          ''')
        _v = VFFSL(SL,"node.thermo",True) # u'$node.thermo' on line 23, col 21
        if _v is not None: write(_filter(_v, rawExpr=u'$node.thermo')) # from line 23, col 21.
        write(u''';
    equationOfState ''')
        _v = VFFSL(SL,"node.equationOfState",True) # u'$node.equationOfState' on line 24, col 21
        if _v is not None: write(_filter(_v, rawExpr=u'$node.equationOfState')) # from line 24, col 21.
        write(u''';
    specie          ''')
        _v = VFFSL(SL,"node.specie",True) # u'$node.specie' on line 25, col 21
        if _v is not None: write(_filter(_v, rawExpr=u'$node.specie')) # from line 25, col 21.
        write(u''';
    energy          ''')
        _v = VFFSL(SL,"node.energy",True) # u'$node.energy' on line 26, col 21
        if _v is not None: write(_filter(_v, rawExpr=u'$node.energy')) # from line 26, col 21.
        write(u''';
}

mixture
{
    specie
    {
        nMoles      ''')
        _v = VFFSL(SL,"node.nMoles",True) # u'$node.nMoles' on line 33, col 21
        if _v is not None: write(_filter(_v, rawExpr=u'$node.nMoles')) # from line 33, col 21.
        write(u''';
        molWeight   ''')
        _v = VFFSL(SL,"node.molWeight",True) # u'$node.molWeight' on line 34, col 21
        if _v is not None: write(_filter(_v, rawExpr=u'$node.molWeight')) # from line 34, col 21.
        write(u''';
    }
    thermodynamics
    {
        Cp          ''')
        _v = VFFSL(SL,"node.Cp",True) # u'$node.Cp' on line 38, col 21
        if _v is not None: write(_filter(_v, rawExpr=u'$node.Cp')) # from line 38, col 21.
        write(u''';
        Hf          ''')
        _v = VFFSL(SL,"node.Hf",True) # u'$node.Hf' on line 39, col 21
        if _v is not None: write(_filter(_v, rawExpr=u'$node.Hf')) # from line 39, col 21.
        write(u''';
    }
    transport
    {
        As          ''')
        _v = VFFSL(SL,"node.As",True) # u'$node.As' on line 43, col 21
        if _v is not None: write(_filter(_v, rawExpr=u'$node.As')) # from line 43, col 21.
        write(u''';
        Ts          ''')
        _v = VFFSL(SL,"node.Ts",True) # u'$node.Ts' on line 44, col 21
        if _v is not None: write(_filter(_v, rawExpr=u'$node.Ts')) # from line 44, col 21.
        write(u''';
    }
}


// ************************************************************************* //
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        
    ##################################################
    ## CHEETAH GENERATED ATTRIBUTES


    _CHEETAH__instanceInitialized = False

    _CHEETAH_version = __CHEETAH_version__

    _CHEETAH_versionTuple = __CHEETAH_versionTuple__

    _CHEETAH_genTime = __CHEETAH_genTime__

    _CHEETAH_genTimestamp = __CHEETAH_genTimestamp__

    _CHEETAH_src = __CHEETAH_src__

    _CHEETAH_srcLastModified = __CHEETAH_srcLastModified__

    _mainCheetahMethod_for_thermophysicalProperties= 'respond'

## END CLASS DEFINITION

if not hasattr(thermophysicalProperties, '_initCheetahAttributes'):
    templateAPIClass = getattr(thermophysicalProperties, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(thermophysicalProperties)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=thermophysicalProperties()).run()

