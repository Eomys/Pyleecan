# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/Simulation.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/Simulation
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.Simulation.run import run
except ImportError as error:
    run = error


from ._check import InitUnKnowClassError
from .Machine import Machine
from .Input import Input
from .VarSimu import VarSimu
from .Post import Post


class Simulation(FrozenClass):
    """Abstract class for the simulation"""

    VERSION = 1

    # cf Methods.Simulation.Simulation.run
    if isinstance(run, ImportError):
        run = property(
            fget=lambda x: raise_(
                ImportError("Can't use Simulation method run: " + str(run))
            )
        )
    else:
        run = run
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        name="",
        desc="",
        machine=-1,
        input=-1,
        logger_name="Pyleecan.Simulation",
        var_simu=None,
        postproc_list=-1,
        index=None,
        path_result=None,
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for pyleecan type, -1 will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with property names as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Load from a file
            init_dict = load_init_dict(init_str)[1]
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "name" in list(init_dict.keys()):
                name = init_dict["name"]
            if "desc" in list(init_dict.keys()):
                desc = init_dict["desc"]
            if "machine" in list(init_dict.keys()):
                machine = init_dict["machine"]
            if "input" in list(init_dict.keys()):
                input = init_dict["input"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
            if "var_simu" in list(init_dict.keys()):
                var_simu = init_dict["var_simu"]
            if "postproc_list" in list(init_dict.keys()):
                postproc_list = init_dict["postproc_list"]
            if "index" in list(init_dict.keys()):
                index = init_dict["index"]
            if "path_result" in list(init_dict.keys()):
                path_result = init_dict["path_result"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.name = name
        self.desc = desc
        self.machine = machine
        self.input = input
        self.logger_name = logger_name
        self.var_simu = var_simu
        self.postproc_list = postproc_list
        self.index = index
        self.path_result = path_result

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Simulation_str = ""
        if self.parent is None:
            Simulation_str += "parent = None " + linesep
        else:
            Simulation_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Simulation_str += 'name = "' + str(self.name) + '"' + linesep
        Simulation_str += 'desc = "' + str(self.desc) + '"' + linesep
        if self.machine is not None:
            tmp = self.machine.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Simulation_str += "machine = " + tmp
        else:
            Simulation_str += "machine = None" + linesep + linesep
        if self.input is not None:
            tmp = self.input.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Simulation_str += "input = " + tmp
        else:
            Simulation_str += "input = None" + linesep + linesep
        Simulation_str += 'logger_name = "' + str(self.logger_name) + '"' + linesep
        if self.var_simu is not None:
            tmp = self.var_simu.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Simulation_str += "var_simu = " + tmp
        else:
            Simulation_str += "var_simu = None" + linesep + linesep
        if len(self.postproc_list) == 0:
            Simulation_str += "postproc_list = []" + linesep
        for ii in range(len(self.postproc_list)):
            tmp = (
                self.postproc_list[ii].__str__().replace(linesep, linesep + "\t")
                + linesep
            )
            Simulation_str += (
                "postproc_list[" + str(ii) + "] =" + tmp + linesep + linesep
            )
        Simulation_str += "index = " + str(self.index) + linesep
        Simulation_str += 'path_result = "' + str(self.path_result) + '"' + linesep
        return Simulation_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.name != self.name:
            return False
        if other.desc != self.desc:
            return False
        if other.machine != self.machine:
            return False
        if other.input != self.input:
            return False
        if other.logger_name != self.logger_name:
            return False
        if other.var_simu != self.var_simu:
            return False
        if other.postproc_list != self.postproc_list:
            return False
        if other.index != self.index:
            return False
        if other.path_result != self.path_result:
            return False
        return True

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.name)
        S += getsizeof(self.desc)
        S += getsizeof(self.machine)
        S += getsizeof(self.input)
        S += getsizeof(self.logger_name)
        S += getsizeof(self.var_simu)
        if self.postproc_list is not None:
            for value in self.postproc_list:
                S += getsizeof(value)
        S += getsizeof(self.index)
        S += getsizeof(self.path_result)
        return S

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)"""

        Simulation_dict = dict()
        Simulation_dict["name"] = self.name
        Simulation_dict["desc"] = self.desc
        if self.machine is None:
            Simulation_dict["machine"] = None
        else:
            Simulation_dict["machine"] = self.machine.as_dict()
        if self.input is None:
            Simulation_dict["input"] = None
        else:
            Simulation_dict["input"] = self.input.as_dict()
        Simulation_dict["logger_name"] = self.logger_name
        if self.var_simu is None:
            Simulation_dict["var_simu"] = None
        else:
            Simulation_dict["var_simu"] = self.var_simu.as_dict()
        if self.postproc_list is None:
            Simulation_dict["postproc_list"] = None
        else:
            Simulation_dict["postproc_list"] = list()
            for obj in self.postproc_list:
                if obj is not None:
                    Simulation_dict["postproc_list"].append(obj.as_dict())
                else:
                    Simulation_dict["postproc_list"].append(None)
        Simulation_dict["index"] = self.index
        Simulation_dict["path_result"] = self.path_result
        # The class name is added to the dict for deserialisation purpose
        Simulation_dict["__class__"] = "Simulation"
        return Simulation_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.name = None
        self.desc = None
        if self.machine is not None:
            self.machine._set_None()
        if self.input is not None:
            self.input._set_None()
        self.logger_name = None
        if self.var_simu is not None:
            self.var_simu._set_None()
        self.postproc_list = None
        self.index = None
        self.path_result = None

    def _get_name(self):
        """getter of name"""
        return self._name

    def _set_name(self, value):
        """setter of name"""
        check_var("name", value, "str")
        self._name = value

    name = property(
        fget=_get_name,
        fset=_set_name,
        doc=u"""Name of the simulation

        :Type: str
        """,
    )

    def _get_desc(self):
        """getter of desc"""
        return self._desc

    def _set_desc(self, value):
        """setter of desc"""
        check_var("desc", value, "str")
        self._desc = value

    desc = property(
        fget=_get_desc,
        fset=_set_desc,
        doc=u"""Simulation description

        :Type: str
        """,
    )

    def _get_machine(self):
        """getter of machine"""
        return self._machine

    def _set_machine(self, value):
        """setter of machine"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "machine"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = Machine()
        check_var("machine", value, "Machine")
        self._machine = value

        if self._machine is not None:
            self._machine.parent = self

    machine = property(
        fget=_get_machine,
        fset=_set_machine,
        doc=u"""Machine to simulate

        :Type: Machine
        """,
    )

    def _get_input(self):
        """getter of input"""
        return self._input

    def _set_input(self, value):
        """setter of input"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "input"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = Input()
        check_var("input", value, "Input")
        self._input = value

        if self._input is not None:
            self._input.parent = self

    input = property(
        fget=_get_input,
        fset=_set_input,
        doc=u"""Input of the simulation

        :Type: Input
        """,
    )

    def _get_logger_name(self):
        """getter of logger_name"""
        return self._logger_name

    def _set_logger_name(self, value):
        """setter of logger_name"""
        check_var("logger_name", value, "str")
        self._logger_name = value

    logger_name = property(
        fget=_get_logger_name,
        fset=_set_logger_name,
        doc=u"""Name of the logger to use

        :Type: str
        """,
    )

    def _get_var_simu(self):
        """getter of var_simu"""
        return self._var_simu

    def _set_var_simu(self, value):
        """setter of var_simu"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "var_simu"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = VarSimu()
        check_var("var_simu", value, "VarSimu")
        self._var_simu = value

        if self._var_simu is not None:
            self._var_simu.parent = self

    var_simu = property(
        fget=_get_var_simu,
        fset=_set_var_simu,
        doc=u"""Multi-simulation definition

        :Type: VarSimu
        """,
    )

    def _get_postproc_list(self):
        """getter of postproc_list"""
        if self._postproc_list is not None:
            for obj in self._postproc_list:
                if obj is not None:
                    obj.parent = self
        return self._postproc_list

    def _set_postproc_list(self, value):
        """setter of postproc_list"""
        if type(value) is list:
            for ii, obj in enumerate(value):
                if type(obj) is dict:
                    class_obj = import_class(
                        "pyleecan.Classes", obj.get("__class__"), "postproc_list"
                    )
                    value[ii] = class_obj(init_dict=obj)
        if value == -1:
            value = list()
        check_var("postproc_list", value, "[Post]")
        self._postproc_list = value

    postproc_list = property(
        fget=_get_postproc_list,
        fset=_set_postproc_list,
        doc=u"""List of postprocessings to run on Output after the simulation

        :Type: [Post]
        """,
    )

    def _get_index(self):
        """getter of index"""
        return self._index

    def _set_index(self, value):
        """setter of index"""
        check_var("index", value, "int", Vmin=0)
        self._index = value

    index = property(
        fget=_get_index,
        fset=_set_index,
        doc=u"""Index of the simulation (if part of a multi-simulation)

        :Type: int
        :min: 0
        """,
    )

    def _get_path_result(self):
        """getter of path_result"""
        return self._path_result

    def _set_path_result(self, value):
        """setter of path_result"""
        check_var("path_result", value, "str")
        self._path_result = value

    path_result = property(
        fget=_get_path_result,
        fset=_set_path_result,
        doc=u"""Path to the Result folder to use (None to use default one)

        :Type: str
        """,
    )
