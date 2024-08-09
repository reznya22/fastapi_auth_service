from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    @abstractmethod
    async def find_by_id(self, *args, **kwargs):
        raise NotImplementedError

    # @abstractmethod
    # async def add_one(self, *args, **kwargs):
    #     raise NotImplementedError
    #
    # @abstractmethod
    # async def find_all(self, *args, **kwargs):
    #     raise NotImplementedError
    #
