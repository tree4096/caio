import asyncio

from benchmark_read_common import main
from caiofix.python_aio_asyncio import AsyncioContext


if __name__ == "__main__":
    asyncio.run(main(AsyncioContext))
