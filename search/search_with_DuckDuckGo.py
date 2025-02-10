from langchain_community.tools import  DuckDuckGoSearchResults

# https://python.langchain.com/v0.2/api_reference/community/tools/langchain_community.tools.ddg_search.tool.DuckDuckGoSearchResults.html
search = DuckDuckGoSearchResults(output_format="list",)

results = search.invoke("who is the latest president of the United States?")
for r in results:
    print(f"## [{r['title']}]({r['link']})\n{r['snippet']}\n")