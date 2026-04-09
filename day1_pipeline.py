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
        if value in ["idle", "running", "completed", "failed"]:
            self._status = value
        else:
            raise ValueError(f"Invalid status value: {value}. Allowed values are: idle, running, completed, failed.")  
         
    def run(self):
        self._status = "running"
        print(f"Pipeline {self.pipeline_name} is now running from {self.source}.")

    def finish(self):
        self._status = "completed"
        print(f"Pipeline {self.pipeline_name} completed successfully.")
    
    def reset(self):
        self._status = "idle"
        print(f"Pipeline {self.pipeline_name} has been reset.")

    def get_status(self):
        return self._status          # return, not print


class AIDataPipeline(DataPipeline):
    def __init__(self, pipeline_name, source, model):
        super().__init__(pipeline_name, source)
        self.model = model

    def analyze(self):
        print(f"Running AI analysis using {self.model} on {self.pipeline_name} data.")


# Testing DataPipeline directly
p = DataPipeline("SalesETL", "MySQL")
p.run()
print(p.status)
p.status = "running"
p.status = "banana"
print(p.get_status())    # running
p.finish()
print(p.get_status())    # completed
p.reset()
print(p.get_status())

print("---")

# Testing AIDataPipeline
ai = AIDataPipeline("SalesETL", "MySQL", "gpt-4")
ai.run()
ai.analyze()
ai.finish()
print(ai.get_status())   # completed — inherited from parent