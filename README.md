# BeautifulSoup
* html structure
  ```bash
    bs = BeautifulSoup(html, 'html.parser')
    # below produces same results
    bs.h1
    bs.html.body.h1
    bs.body.h1
    bs.html.h1
  ```

  ## parser
  |Type|parser|Advantage|Disadvantage|
  |:---:|:---:|:---|:---|
  |HTML|`html.parser`|||
  |HTML|`lxml`|parse messy or malformed HTML code. Faster than `html.parser`|Depend on C libraries|
  |HTML|`html5lib`|parse messy or malformed HTML code|the slowest one|


# Handling Exceptions
