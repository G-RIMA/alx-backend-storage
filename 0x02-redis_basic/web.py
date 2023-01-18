#!/usr/bin/env python3
import requests
import redis

#create redis connection
r = redis.StrictRedis()

def get_page(url: str) -> str:
    #check if we have a cached result for this url
    cache_key = "count:" + url
    cached_result = r.get(cache_key)
    if cached_result:
        r.incr(cache_key)
        return cached_result.decode()
    else:
        #if no cached result, request the page and cache the result
        result = requests.get(url)
        r.set(cache_key, result.text, ex=10)
        r.incr(cache_key)
        return result.text

