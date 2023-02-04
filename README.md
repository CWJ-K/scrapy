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
## Possible Erros
1. the page is not found on the server (there was an error in retrieving it)
 * 404 page not found
 * 500 internal server error
2. the server is not found
3. html tags do not exist
    * bs.None_object.tag: return AttributeError
    * bs.exist_object.none_tag: reutrn None


# Analyze websites
> should not be a hammer to dig all tags and use them. The code is fragile when the structure of tags changes
* look for a "print this page" or "html file" link
* look for the information hidden in a JavaScript file
* look for URL
* use other alternative websites
  * if no, the final way is to select tags by elegant methods: BeautifuleSoup
