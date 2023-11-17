IMPORTANT// This version is outdated and may not work as intended. Use at your own will. 

# Facebook-Post-ID-Finder
WARNING: This tool is used to scrape Post ID of Embedded, Album and Text posts. Posts with permalinks might throw an error!

A minimalistic PyQT5 application to gather ID of desired Facebook Post.

Libraries which we use contains PyQT5, bs4(BeautifulSoup,with html.parser), requests.

The main functionality of this tool is to scrape "top_level_post_id",which is the correct ID of the post, from HTML code of the page and bring it to user.

Example:

https://www.facebook.com/johannmcrollin/posts/pfbid02FXLaXcfUmZWYLEVQ2phNPpEsdmQeqbJBB9Ehb2bdGLx829rWMCKSPTjWMoVVfsQHl This is the current encoding of Facebook URLs which is too long and sometimes do not work for several applications.

Using this tool returns "top_level_post_id" = "162583066328243" as result after clicking "Standart" button.

https://www.facebook.com/johannmcrollin/posts/162583066328243 This is the final (and old) URL form which belongs to same post.

In some occasions, "Standart" button return "og_post_id" which do not work if add to the URL. In such occasions, we can use "Alternative" button to get the "top_level_post_id".

If both returns does not return the desired output, then it means there is something wrong with link or the content(those posts came out as comments which won't work).

Thank you! Hope you enjoy the tool.
