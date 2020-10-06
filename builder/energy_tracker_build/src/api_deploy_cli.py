from energy_tracker_build.src.api_deploy import ApiDeployer, MissingDependenciesError, ApiDeployerStatusMonitor


class ApiDeployCli:
    @staticmethod
    def deploy(env):
        deployer = ApiDeployer(CliApiDeployerStatusMonitor())
        try:
            deployer.deploy(env)
        except MissingDependenciesError as error:
            raise SystemExit(str(error))


class CliApiDeployerStatusMonitor(ApiDeployerStatusMonitor):
    def checking_build_tool_dependencies(self):
        self.report_status("Checking build tools installed")

    def installing_api_dependencies(self):
        self.report_status("Installing API dependencies")

    def performing_serverless_deploy(self):
        self.report_status("Performing serverless deploy of API")

    @staticmethod
    def report_status(status):
        print("\n\n{}...".format(status))
