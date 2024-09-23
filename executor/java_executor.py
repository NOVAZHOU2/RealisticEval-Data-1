JAVA_RUN_ENV = "../envs/java/src"


class JavaExecutor:
    def __init__(self, model_name):
        self._env_path = JAVA_RUN_ENV
        self.model_name = model_name

    def single_run(self, code, test_code):
        with open(f"{self._env_path}/temp.cpp", "w", encoding="utf8") as temp_file:
            temp_file.write(code)
            temp_file.flush()