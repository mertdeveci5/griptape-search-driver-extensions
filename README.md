# Griptape Serper Search Extension

A driver extension for [Serper.dev] (https://serper.dev/) for web searching functionality. This extension also provides functionality to search for only `news`, `places`, `images` and `patents`. You can also use a `date_range` parameter to restrict the search results.

## Getting Started

Get an API key at [Serper.dev] (https://serper.dev/)

1. Import `WebSearchTool` and specify the `SerperWebSearchDriver` as the driver.

```python
web_search_tool = WebSearchTool(
    web_search_driver=SerperWebSearchDriver(api_key=os.getenv("SERPER_API_KEY"))
)
agent = Agent(tools=[web_search_tool])

agent.run("Find out recent news on Griptape.ai")
```

2. You can use `date_range` parameter and `type` parameter to focus the search results

```python
web_search_tool = WebSearchTool(
    web_search_driver=SerperWebSearchDriver(
        api_key=os.getenv("SERPER_API_KEY"), type="news", date_range="d"
    )
)
agent = Agent(tools=[web_search_tool])

agent.run("Recent news on Trump please")
```

Available date ranges:

- `h` - past hour
- `d` - past 24 hours/day
- `w` - past week
- `m` - past month
- `y` - past year

#### Running Example

This template includes an [example](https://github.com/griptape-ai/tool-template/blob/main/examples/tools/example_agent.py) demonstrating how to use the extension. It shows how to import the `ReverseStringTool`, provide it to an Agent, and run it.

1. Set the required environment variables. The example needs the `OPENAI_API_KEY` and `SERPER_API_KEY` environment variable to be set.
2. Run the example:

```bash
poetry run python examples/tools/example_agent.py
```

If successful, you should see:

```
[01/17/25 15:46:00] INFO     ToolkitTask 5def898884834cc9a49150d475275db3
                             Input: Recent news on Trump please
[01/17/25 15:46:01] INFO     Subtask ce7f72d30ba9423ca2e7997f339b5010
                             Actions: [
                               {
                                 "tag": "call_tFCr2OMPuwnCm0wfwChjQ1rn",
                                 "name": "WebSearchTool",
                                 "path": "search",
                                 "input": {
                                   "values": {
                                     "query": "recent news on Trump"
                                   }
                                 }
                               }
                             ]
[01/17/25 15:46:02] INFO     Subtask ce7f72d30ba9423ca2e7997f339b5010
                             Response: {"url":
                             "https://www.washingtonpost.com/politics/2025/01/16/biden-last-minute-moves-h
                             ard-for-trump-undo/", "title": "Biden seeks last-minute moves that could be
                             hard for Trump to undo", "description": "From clemency to conservation, the
                             outgoing president pushes to cement his legacy ahead of a successor
                             determined to erase it.", "date": "8 hours ago", "source": "The Washington
                             Post"}

                             {"url": "https://www.nytimes.com/live/2025/01/16/us/trump-news-hearings",
                             "title": "Trump Transition Live Updates: The Latest on Senate Confirmation
                             Hearings", "description": "More Senate confirmation hearings for prospective
                             members of the Trump cabinet wrapped up on Thursday. Scott Bessent,
                             President-elect Donald J. Trump's pick...", "date": "3 hours ago", "source":
                             "The New York Times"}

                             {"url": "https://www.bbc.com/news/articles/cn07dv4mrg2o", "title": "Who is JD
                             Vance, a 'never Trump guy' who will be vice-president?", "description": "The
                             conservative from Ohio shot to fame writing about his hard upbringing and
                             morphed from a harsh critic of Donald Trump into a Maga champion.", "date":
                             "12 hours ago", "source": "BBC"}

                             {"url":
                             "https://www.poynter.org/commentary/2025/another-tech-big-boss-headed-to-dona
                             ld-trumps-inauguration-elon-musk-jeff-bezos-mark-zuckerberg/", "title":
                             "Opinion | Google CEO is the latest tech boss headed to Donald Trump\u2019s
                             inauguration", "description": "Sundar Pichai joins CEOs from X, Meta, Amazon
                             and TikTok for prime spot at ceremony.", "date": "1 hour ago", "source":
                             "Poynter"}

                             {"url":
                             "https://www.yahoo.com/news/tiktok-ban-latest-app-reveals-173823265.html",
                             "title": "TikTok ban live: Shutdown in doubt as Biden suggests Trump could
                             save app", "description": "Supreme Court is set to release at least one
                             opinion on Friday morning.", "date": "4 hours ago", "source": "Yahoo"}

                             {"url": "https://www.voanews.com/z/4720", "title": "2024 US Election",
                             "description": "News, analysis and context about the 2024 U.S. elections.",
                             "date": "4 hours ago", "source": "VOA - Voice of America English News"}

                             {"url":
                             "https://www.cbsnews.com/video/main-takeaways-from-trump-nominees-latest-sena
                             te-confirmation-hearings/", "title": "The main takeaways from Trump nominees'
                             latest Senate confirmation hearings", "description": "On Thursday, Senators
                             heard from President-elect Donald Trump's picks for secretary of the
                             Interior, secretary of the Treasury, Environmental Protection...", "date":
                             "16 hours ago", "source": "CBS News"}

                             {"url": "https://www.cnn.com/2025/01/16/politics/cnn-poll-trump/index.html",
                             "title": "CNN Poll: Trump will enter the White House with more positive
                             sentiment than his last term", "description": "Donald Trump continues to see
                             some of the most positive ratings of his political career, according to a new
                             CNN poll conducted by SSRS, which finds the...", "date": "23 hours ago",
                             "source": "CNN"}

                             {"url":
                             "https://www.hindustantimes.com/world-news/donald-trump-inauguration-january-
                             20-coldest-washington-dc-weather-temperature-snow-101737096315890.html",
                             "title": "'Will be very cold': Donald Trump's inauguration on January 20 to
                             be coldest US president swearing-in of recent history", "description": "With
                             temperatures forecast to plummet well below average for Jan, the Jan 20
                             ceremony is set to take place amid bitterly cold, with a chance of snow on
                             Jan...", "date": "7 hours ago", "source": "Hindustan Times"}

                             {"url":
                             "https://www.israelhayom.com/2025/01/17/trump-slams-biden-for-not-doing-anyth
                             ing-on-hostages/", "title": "Trump slams Biden for 'not doing anything' on
                             hostages", "description": "Former President Donald Trump discussed the
                             Israel-Hamas hostage negotiations and asserted his influence over recent
                             developments in an interview with The...", "date": "7 hours ago", "source":
                             "www.israelhayom.com"}
```
