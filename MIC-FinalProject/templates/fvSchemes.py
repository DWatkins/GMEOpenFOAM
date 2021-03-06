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
__CHEETAH_genTime__ = 1449712222.975
__CHEETAH_genTimestamp__ = 'Wed Dec 09 19:50:22 2015'
__CHEETAH_src__ = 'fvSchemes.tmpl'
__CHEETAH_srcLastModified__ = 'Wed Dec 09 19:41:13 2015'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class fvSchemes(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(fvSchemes, self).__init__(*args, **KWs)
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
    location    "system";
    object      fvSchemes;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

ddtSchemes
{
    default         ''')
        _v = VFFSL(SL,"node.ddtSchemes",True) # u'$node.ddtSchemes' on line 20, col 21
        if _v is not None: write(_filter(_v, rawExpr=u'$node.ddtSchemes')) # from line 20, col 21.
        write(u''';
}

gradSchemes
{
    default         ''')
        _v = VFFSL(SL,"node.gradSchemes",True) # u'$node.gradSchemes' on line 25, col 21
        if _v is not None: write(_filter(_v, rawExpr=u'$node.gradSchemes')) # from line 25, col 21.
        write(u''';
}

divSchemes
{
    default         none;

    div(phi,U)      bounded Gauss upwind;
    div((muEff*dev2(T(grad(U))))) Gauss linear;
    div(phi,e)      bounded Gauss upwind;
    div(phi,epsilon) bounded Gauss upwind;
    div(phi,k)      bounded Gauss upwind;
    div(phi,Ekp)    bounded Gauss upwind;
}

laplacianSchemes
{
    default         ''')
        _v = VFFSL(SL,"node.laplacianSchemes",True) # u'$node.laplacianSchemes' on line 42, col 21
        if _v is not None: write(_filter(_v, rawExpr=u'$node.laplacianSchemes')) # from line 42, col 21.
        write(u''';
}

interpolationSchemes
{
    default         ''')
        _v = VFFSL(SL,"node.interpolationSchemes",True) # u'$node.interpolationSchemes' on line 47, col 21
        if _v is not None: write(_filter(_v, rawExpr=u'$node.interpolationSchemes')) # from line 47, col 21.
        write(u''';
}

snGradSchemes
{
    default         ''')
        _v = VFFSL(SL,"node.snGradSchemes",True) # u'$node.snGradSchemes' on line 52, col 21
        if _v is not None: write(_filter(_v, rawExpr=u'$node.snGradSchemes')) # from line 52, col 21.
        write(u''';
}

fluxRequired
{
    default         ''')
        _v = VFFSL(SL,"node.fluxRequired",True) # u'$node.fluxRequired' on line 57, col 21
        if _v is not None: write(_filter(_v, rawExpr=u'$node.fluxRequired')) # from line 57, col 21.
        write(u''';
    p               ;
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

    _mainCheetahMethod_for_fvSchemes= 'respond'

## END CLASS DEFINITION

if not hasattr(fvSchemes, '_initCheetahAttributes'):
    templateAPIClass = getattr(fvSchemes, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(fvSchemes)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=fvSchemes()).run()


