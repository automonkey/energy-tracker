import subprocess


class ApiDeployer:
    def __init__(self, api_deployer_status_monitor):
        self.api_deployer_status_monitor = api_deployer_status_monitor

    def deploy(self, env):
        self.ensure_build_tools_installed()
        self.install_api_dependencies()
        self.do_serverless_deploy(env)

    def ensure_build_tools_installed(self):
        self.api_deployer_status_monitor.checking_build_tool_dependencies()

        deps = [{"name": "npm", "check_cmd": "npm --version"}, {"name": "node", "check_cmd": "node --version"}]

        missing_deps = []
        for dep in deps:
            try:
                subprocess.run(dep["check_cmd"].split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except Exception as ex:
                missing_deps.append({"dep": dep, "cause": ex})

        if len(missing_deps) > 0:
            raise MissingDependenciesError(missing_deps)

    def install_api_dependencies(self):
        self.api_deployer_status_monitor.installing_api_dependencies()

        try:
            completed_process = subprocess.run("npm install".split(), cwd="./api")
        except Exception as ex:
            raise DependenciesInstallationFailedError(ex)

        if completed_process.returncode != 0:
            raise DependenciesInstallationFailedError(
                "npm install returned status code: {}".format(completed_process.returncode)
            )

    def do_serverless_deploy(self, env):
        self.api_deployer_status_monitor.performing_serverless_deploy()

        try:
            completed_process = subprocess.run(
                "./node_modules/serverless/bin/serverless.js deploy --stage {}".format(env).split(), cwd="./api"
            )
        except Exception as ex:
            raise ServerlessDeploymentError(ex)

        if completed_process.returncode != 0:
            raise ServerlessDeploymentError(
                "serverless deploy returned status code: {}".format(completed_process.returncode)
            )


class ApiDeployerStatusMonitor:
    def checking_build_tool_dependencies(self):
        pass

    def installing_api_dependencies(self):
        pass

    def performing_serverless_deploy(self):
        pass


class ApiDeploymentError(Exception):
    pass


class ServerlessDeploymentError(Exception):
    def __init__(self, cause):
        super().__init__("Serverless deployment failed: {}".format(cause))


class DependenciesInstallationFailedError(ApiDeploymentError):
    def __init__(self, cause):
        super().__init__("Failed to install API dependencies: {}".format(cause))


class MissingDependenciesError(ApiDeploymentError):
    def __init__(self, missing_deps):
        output_data = self.missing_deps_to_cmd_and_error(missing_deps)
        super().__init__(
            "Missing required dependencies:\n  {}\n\nErrors{}".format(
                ", ".join(output_data[0]), "\n\n  ".join([""] + output_data[1])
            )
        )

    @staticmethod
    def missing_deps_to_cmd_and_error(missing_deps):
        missing_dependency_names = [missing_dep["dep"]["name"] for missing_dep in missing_deps]
        cmd_and_error_strings = [
            "{}: {}".format(missing_dep["dep"]["check_cmd"], missing_dep["cause"]) for missing_dep in missing_deps
        ]

        return missing_dependency_names, cmd_and_error_strings
