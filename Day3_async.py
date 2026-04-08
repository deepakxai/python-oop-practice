import asyncio
import time

async def fetch_from_source(source,delay):
    print(f"Fetching data from {source}...")
    await asyncio.sleep(delay)  # Simulate network delay
    print(f"Data fetched from {source} after {delay} seconds.")
    return f"{source} Data Ready"
async def run_pipeline():
    results = await asyncio.gather(
        fetch_from_source("MySQL", 2),
        fetch_from_source("Weather API", 1),
        fetch_from_source("OpenAI", 3)
    )
    print("\nAll results:")
    for r in results:
        print(f"  - {r}")
start_time=time.time()
asyncio.run(run_pipeline())
end_time=time.time()
print(f"Total execution time: {end_time - start_time:.2f} seconds")
