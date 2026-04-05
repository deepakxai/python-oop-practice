class DataPipeline:
    def __init__(self, pipeline_name, source):
        self.pipeline_name = pipeline_name
        self.source = source
        self._status = "idle"

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        allowed = ["idle", "running", "completed", "failed"]
        if value not in allowed:
            raise ValueError(f"Invalid status: '{value}'. Allowed: {allowed}")
        self._status = value

    def run(self):
        self.status = "running"      # ✓ through setter
        print(f"Pipeline {self.pipeline_name} is now running from {self.source}.")

    def finish(self):
        self.status = "completed"    # ✓ through setter
        print(f"Pipeline {self.pipeline_name} completed successfully.")

    def reset(self):
        self.status = "idle"         # ✓ through setter
        print(f"Pipeline {self.pipeline_name} has been reset.")

    def get_status(self):
        return self.status


class AIDataPipeline(DataPipeline):
    def __init__(self, pipeline_name, source, model):
        super().__init__(pipeline_name, source)
        self.model = model

    def analyze(self):
        print(f"Running AI analysis using {self.model} on {self.pipeline_name} data.")


# Testing DataPipeline
p = DataPipeline("SalesETL", "MySQL")
p.run()
print(p.get_status())       # running

try:
    p.status = "banana"     # triggers ValueError
except ValueError as e:
    print(f"Caught error: {e}")

print(p.get_status())       # still running — error was handled
p.finish()
print(p.get_status())       # completed
p.reset()
print(p.get_status())       # idle

print("---")

# Testing AIDataPipeline
ai = AIDataPipeline("SalesETL", "MySQL", "gpt-4")
ai.run()
ai.analyze()
ai.finish()
print(ai.get_status())      # completed