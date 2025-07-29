import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/connexun-srl-connexun-srl-default/api/news67'

mcp = FastMCP('news67')

@mcp.tool()
def news_feed(categoryCode: Annotated[Union[str, None], Field(description='Filter feed of news based on IPTC categories code. Use /categories-info resource to get the values.')] = None,
              batchSize: Annotated[Union[int, float, None], Field(description='Number of news elements to be returned in each call. Defaults to 10, maximum 30')] = None,
              languages: Annotated[Union[str, None], Field(description='Two letter ISO code to filter content by language. Use /languages resource to get language codes. Defaults to all.')] = None,
              sortOrder: Annotated[Union[str, None], Field(description="Sort the final result in descending or ascending order of publication by passing 'oldest' or 'latest' respectively, defaults to oldest.")] = None,
              sources: Annotated[Union[str, None], Field(description='FIlter feed of news from different source/sources. Takes comma separated values.')] = None,
              sentiment: Annotated[Union[str, None], Field(description='Filter the feed for news with either positive or negative sentiments. Defaults to both')] = None,
              skip: Annotated[Union[int, float, None], Field(description='For next batch of results use this with value increment of previous call batchSize value. Default is zero.')] = None) -> dict: 
    '''This endpoint fetches latest news published. This endpoint can be used to get a continuous feed of news on your dashboard. Various filter can be applied to get the feed according to requirements. The topics are made available as soon as our pipeline finihes processing them, thus provding near real time output.'''
    url = 'https://news67.p.rapidapi.com/v2/feed'
    headers = {'x-rapidapi-host': 'news67.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'categoryCode': categoryCode,
        'batchSize': batchSize,
        'languages': languages,
        'sortOrder': sortOrder,
        'sources': sources,
        'sentiment': sentiment,
        'skip': skip,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def world_trending(relatedNewsLimit: Annotated[Union[int, float, None], Field(description='Limit the number of news that are returned inside a cluster.')] = None,
                   languages: Annotated[Union[str, None], Field(description='Two letter ISO code to filter content by languages. Use comman separated codes to get results for multiple languages. Use /languages resource to get language codes. Defaults to all.')] = None,
                   top: Annotated[Union[str, None], Field(description='Limit number of trending topics that are returned. Defaults to 10.')] = None,
                   skip: Annotated[Union[str, None], Field(description='For next batch of results use this with value increment of previous call top value.')] = None) -> dict: 
    '''Get trending news topics from across the world with this endpoint. We determine trending news / / topics by considering unique sources, and nationalities which are talking about the same topic, / / along with various languages the topic is published in. Thus providing an unbiased list topics which are / / being talked about across the world.'''
    url = 'https://news67.p.rapidapi.com/v2/trending'
    headers = {'x-rapidapi-host': 'news67.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'relatedNewsLimit': relatedNewsLimit,
        'languages': languages,
        'top': top,
        'skip': skip,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def topic_search(languages: Annotated[str, Field(description='Two letter ISO code to filter content by language. Use /languages resource to get language codes.')],
                 search: Annotated[str, Field(description='Phrases or topics to be searched, in any of supported language.')],
                 batchSize: Annotated[Union[int, float, None], Field(description='Number of news elements to be returned in each call. Defaults to 10, maximum 30.')] = None,
                 skip: Annotated[Union[int, float, None], Field(description='For next batch of results use this with value increment of previous call batchSize value.')] = None,
                 searchType: Annotated[Union[str, None], Field(description='Boolean search parameter applied between search terms. Must be AND or OR, defaults to OR.')] = None,
                 qField: Annotated[Union[str, None], Field(description='Field where input text would be matched Must be either title, or text.')] = None,
                 sortBy: Annotated[Union[str, None], Field(description='Sort the final results by relevance or publication date in descending order. Defaults to relevance.')] = None,
                 publishedAfter: Annotated[Union[str, None], Field(description='ISO 8601 formatted Date Time value to filter the results which are published after the input date. It must be within 30 days from the current date. example format: With date and time: YYYY-MM-DDTHH:MM:SS With only Date: YYYY-MM-DD')] = None,
                 publishedBefore: Annotated[Union[str, None], Field(description='ISO 8601 formatted Date Time value to filter the results which are published before the input date. It must be within 30 days from the current date. If using the upper limit, it will show results going as far back as 35 days. example format: With date and time: YYYY-MM-DDTHH:MM:SS With only Date: YYYY-MM-DD')] = None) -> dict: 
    '''Use topic-search endpoint to find news which talks about specific topics. Topics can range from specific keywords, to the name of a person or a place, or a combination of both. Results can be filtered by topics that are present in the title or text of the news, or both by default.'''
    url = 'https://news67.p.rapidapi.com/v2/topic-search'
    headers = {'x-rapidapi-host': 'news67.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'languages': languages,
        'search': search,
        'batchSize': batchSize,
        'skip': skip,
        'searchType': searchType,
        'qField': qField,
        'sortBy': sortBy,
        'publishedAfter': publishedAfter,
        'publishedBefore': publishedBefore,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def country_news(skip: Annotated[Union[int, float, None], Field(description='For next batch of results use this with value increment of previous call batchSize value.')] = None,
                 batchSize: Annotated[Union[int, float, None], Field(description='Number of news elements to be returned in each call.')] = None,
                 fromCountry: Annotated[Union[str, None], Field(description='Use this parameter to filter news from a given country.')] = None,
                 languages: Annotated[Union[str, None], Field(description='Two letter ISO code to filter content by languages. Use comman separated codes to get results for multiple languages. Use /languages resource to get language codes. Defaults to all.')] = None,
                 onlyInternational: Annotated[Union[bool, None], Field(description='To get only international news when getting news fromCountry, use true. Defaults to false.')] = None,
                 aboutCountry: Annotated[Union[str, None], Field(description='Use this parameter to filter news which talks about a specific country.')] = None) -> dict: 
    '''This endpoint returns news which are specific to countries. You can use different filters to get local news about a country, international news about country, or inter-country news which discusses about the two countries.'''
    url = 'https://news67.p.rapidapi.com/v2/country-news'
    headers = {'x-rapidapi-host': 'news67.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'skip': skip,
        'batchSize': batchSize,
        'fromCountry': fromCountry,
        'languages': languages,
        'onlyInternational': onlyInternational,
        'aboutCountry': aboutCountry,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def crypto_news(token: Annotated[Union[str, None], Field(description='Enter token symbol to get news specific to that currency. Default is all tokens we process.')] = None,
                languages: Annotated[Union[str, None], Field(description='Two letter ISO language code to filter the news. Multiple languages can be selected by passing a comma separated string. Default is all.')] = None,
                sentiment: Annotated[Union[str, None], Field(description='Use sentiment value of "positive" or "negative" to filter out content. Default to both')] = None,
                publishedAfter: Annotated[Union[str, None], Field(description='Date field to get news published after input date. Must be within last 30 days from current day to 30 mins ago from current time in UTC. Formatted as YYYY-MM-DDTHH:MM:SS Default to last 30th day.')] = None,
                publishedBefore: Annotated[Union[str, None], Field(description='Date field to get news published before input date. Must be within last 30 days from current day to 30 mins ago from current time in UTC. Formatted as YYYY-MM-DDTHH:MM:SS Default to last 30th day.')] = None,
                sortOrder: Annotated[Union[str, None], Field(description='Sort the news output by "latest" news first or "oldest" news first based on captured publication date using this parameter. Defaults to latest.')] = None,
                batchSize: Annotated[Union[int, float, None], Field(description='Use this parameter to limit the number of news per result. Default to 15, maximum 30 Default: 0')] = None,
                skip: Annotated[Union[int, float, None], Field(description='Use this parameter for pagination to get next batch of results. Default to 0 Default: 0')] = None) -> dict: 
    '''Get latest news and topics about Blockchain & Cryptocurrencies. Use sentiments to follow only positive news. Use token filter to get news about token that you want to follow.'''
    url = 'https://news67.p.rapidapi.com/v2/crypto'
    headers = {'x-rapidapi-host': 'news67.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'token': token,
        'languages': languages,
        'sentiment': sentiment,
        'publishedAfter': publishedAfter,
        'publishedBefore': publishedBefore,
        'sortOrder': sortOrder,
        'batchSize': batchSize,
        'skip': skip,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def language_info() -> dict: 
    '''Get two letter language codes for languages supported by us.'''
    url = 'https://news67.p.rapidapi.com/languages'
    headers = {'x-rapidapi-host': 'news67.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def catergories_info() -> dict: 
    '''Get list of IPTC media category labels and code o filter our news feed.'''
    url = 'https://news67.p.rapidapi.com/v2/categories-info'
    headers = {'x-rapidapi-host': 'news67.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def countries_info() -> dict: 
    '''Get list of two letter country codes'''
    url = 'https://news67.p.rapidapi.com/countries'
    headers = {'x-rapidapi-host': 'news67.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
