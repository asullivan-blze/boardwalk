"""
This type stub file was generated by pyright.
"""

logger = ...

class BaseExecutionMode:
    NONE = ...
    ANSIBLE_COMMANDS = ...
    GENERIC_COMMANDS = ...

class BaseConfig:
    def __init__(
        self,
        private_data_dir=...,
        host_cwd=...,
        envvars=...,
        passwords=...,
        settings=...,
        project_dir=...,
        artifact_dir=...,
        fact_cache_type=...,
        fact_cache=...,
        process_isolation=...,
        process_isolation_executable=...,
        container_image=...,
        container_volume_mounts=...,
        container_options=...,
        container_workdir=...,
        container_auth_data=...,
        ident=...,
        rotate_artifacts=...,
        timeout=...,
        ssh_key=...,
        quiet=...,
        json_mode=...,
        check_job_event_data=...,
        suppress_env_files=...,
    ) -> None: ...

    _CONTAINER_ENGINES = ...
    @property
    def containerized(self): ...
    def wrap_args_for_containerization(self, args, execution_mode, cmdline_args): ...
    def wrap_args_with_ssh_agent(
        self, args, ssh_key_path, ssh_auth_sock=..., silence_ssh_add=...
    ):  # -> list[str]:
        """
        Given an existing command line and parameterization this will return the same command line wrapped with the
        necessary calls to ``ssh-agent``
        """
        ...
