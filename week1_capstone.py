import asyncio
import time

class DataPipeline:
    def __init__(self, name, source):
        self.name = name
        self.source = source
        self._status = "idle"

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        allowed = ["idle", "running", "completed", "failed"]
        if value not in allowed:
            raise ValueError(f"Invalid status: {value}")
        self._status = value

    async def run(self):
        self.status = "running"
        print(f"Pipeline {self.name} started from {self.source}")
        
        await asyncio.sleep(2)  # simulate work
        
        self.status = "completed"
        print(f"Pipeline {self.name} completed")
        
        return f"{self.name} - success"

    async def run_with_error_handling(self):
        try:
            result = await self.run()
            return result
        except Exception as e:
            self.status = "failed"
            return f"{self.name} - failed: {str(e)}"


class PipelineManager:
    def __init__(self):
        self.pipelines = []

    def add_pipeline(self, pipeline):
        self.pipelines.append(pipeline)

    async def run_all(self):
        return await asyncio.gather(
            *[p.run_with_error_handling() for p in self.pipelines]
        )

    def print_summary(self, results):
        print("\n--- Pipeline Summary ---")
        for pipeline, result in zip(self.pipelines, results):
            print(f"{pipeline.name} | Status: {pipeline.status} | Result: {result}")


async def main():
    manager = PipelineManager()

    # Create pipelines
    p1 = DataPipeline("SalesETL", "MySQL")
    p2 = DataPipeline("WeatherData", "Weather API")
    p3 = DataPipeline("AIInsights", "OpenAI")

    # Add to manager
    manager.add_pipeline(p1)
    manager.add_pipeline(p2)
    manager.add_pipeline(p3)

    start = time.time()
    results = await manager.run_all()
    end = time.time()

    manager.print_summary(results)
    print(f"\nTotal time: {end - start:.2f} seconds")

asyncio.run(main())