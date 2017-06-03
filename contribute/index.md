---
layout: default
---

# Contributing to public-apis

> While the masses of pull requests and community involvement is appreciated, some pull requests have been specifically 
opened to market company APIs that offer paid solutions. This API list is not a marketing tool, but a tool to help the
community build applications and use free, public APIs quickly and easily. Pull requests that are identified as marketing attempts will not be accepted.
> 
> Thanks for understanding! :)

## How to Contribute 

```
{name: Demo,   
description: "What is it?",  
auth: "No",  
link: http://yada-yada.com,  
category:[one, or, more, categories]}  

```


Example entry:

```
{ name: Nasa,
  description: "NASA data, including imagery,
  author: "No",
  link: http://api.nasa.gov }
```

Currently, the only accepted inputs for this field are as follows:

* `oAuth` - _the API supports oAuth_
* `apiKey` - _the API uses a private key string/token for authentication - try and use the correct parameter_
* `X-Mashape-Key` - _the name of the header which may need to be sent_
* `No` - _the API requires no authentication to run_

Please continue to follow the alphabetical ordering that is in place per section.

### Pull Request Pro Tips  

* [Fork](http://guides.github.com/activities/forking/) the repository and [clone][clone-link] it locally.
Connect your local repository to the original `upstream` repository by adding it as a [remote](https://help.github.com/articles/adding-a-remote/).
Pull in changes from `upstream` often so that you stay up to date and so when you submit your pull request,
merge conflicts will be less likely. See more detailed instructions [here](https://help.github.com/articles/syncing-a-fork).
* Create a [branch](http://guides.github.com/introduction/flow/) for your edits.
* Contribute in the style of the project as outlined above. This makes it easier for the collaborators to merge 
and for others to understand and maintain in the future.
