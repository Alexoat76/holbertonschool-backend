#!/usr/bin/python3
"""
This module contains the `BasicCache` class that inherits from the
`BaseCaching` Parent Class and is a caching system that stores data
in a dictionary.
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    This class is a caching system that stores data in a dictionary.
    """

    def put(self, key, item):
        """
        Adds an item to the cache.
        """
        self.cache_data[key] = item

    def get(self, key):
        """
        Returns an item from the cache.
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
