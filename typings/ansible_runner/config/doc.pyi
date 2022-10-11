"""
This type stub file was generated by pyright.
"""

from ansible_runner.config._base import BaseConfig

logger = ...

class DocConfig(BaseConfig):
    """
    A ``Runner`` configuration object that's meant to encapsulate the configuration used by the
    :py:mod:`ansible_runner.runner.DocConfig` object to launch and manage the invocation of
    command execution.

    Typically this object is initialized for you when using the standard ``get_plugin_docs`` or ``get_plugin_list`` interfaces
    in :py:mod:`ansible_runner.interface` but can be used to construct the ``DocConfig`` configuration to be invoked elsewhere.
    It can also be overridden to provide different functionality to the DocConfig object.

    :Example:

    >>> dc = DocConfig(...)
    >>> r = Runner(config=dc)
    >>> r.run()

    """

    def __init__(self, runner_mode=..., **kwargs) -> None: ...

    _supported_response_formats = ...
    def prepare_plugin_docs_command(
        self,
        plugin_names,
        plugin_type=...,
        response_format=...,
        snippet=...,
        playbook_dir=...,
        module_path=...,
    ): ...
    def prepare_plugin_list_command(
        self,
        list_files=...,
        response_format=...,
        plugin_type=...,
        playbook_dir=...,
        module_path=...,
    ): ...
    def prepare_role_list_command(self, collection_name, playbook_dir):  # -> None:
        """
        ansible-doc -t role -l -j <collection_name>
        """
        ...
    def prepare_role_argspec_command(
        self, role_name, collection_name, playbook_dir
    ):  # -> None:
        """
        ansible-doc -t role -j <collection_name>.<role_name>
        """
        ...
