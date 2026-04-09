class DataPipeline:
    def __init__(self,pipeline,source):
        self.pipeline=pipeline
        self.source=source
        self.status="idle"
    def run(self):
        self.status="running"
        print(f"Pipeline {self.pipeline} is now running from {self.source}.")
    def finish(self):
        self.status="completed"
        print(f"Pipeline {self.pipeline} completed successfully.")
    def get_status(self):
        print(f"{self.status}.")
class AIDataPipeline(DataPipeline):
    def __init__(self, pipeline, source,model):
        super().__init__(pipeline, source)
        self.model=model
    def analyze(self):
        print(f"Running AI analysis using {self.model} on {self.pipeline} data")

ai=AIDataPipeline("SalesETL","Mysql","gpt-4")
ai.run()
ai.analyze()