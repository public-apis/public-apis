---
layout: default
---

<h1> Contributing to public-apis</h1>


> While the masses of pull requests and community involvement is appreciated, some pull requests have been specifically 
opened to market company APIs that offer paid solutions. This API list is not a marketing tool, but a tool to help the
community build applications and use free, public APIs quickly and easily. Pull requests that are identified as marketing attempts will not be accepted.
> 
> Thanks for understanding! :)


<h2> Formatting  </h2>

<table class="table table-bordered table-condensed">
<thead>
<tr>
	<td>API</td>
	<td>Description</td>
	<td>Auth</td>
	<td>HTTPS</td>
	<td>Link</td>
</tr>
</thead>
<tr>
	<td>API title</td>
	<td>Description of API</td>
	<td>Does this API require authentication? *</td>
	<td>Does the API support HTTPS?</td>
	<td>Link to API webpage</td>
</tr>
</table>


Example Entry: 
  
	  | NASA | NASA data, including imagery | No | Yes | [Go!](https://api.nasa.gov) |
	  
Currently, the only accepted inputs for the Auth field are as follows:

* `oAuth` - _the API supports oAuth_
* `apiKey` - _the API uses a private key string/token for authentication - try and use the correct parameter_
* `X-Mashape-Key` - _the name of the header which may need to be sent_
* `No` - _the API requires no authentication to run_

Please continue to follow the alphabetical ordering that is in place per section.

If an API seems to fall into multiple categories, please place the listing within the section most in line with the services offered through the API. For example, the Instagram API is listed under Social since it is mainly a social network, even though it could also apply to Photography.

## Pull Request 

After you've created a branch on your fork with your changes, it's time to make a pull request!
Once you've submitted a pull request, the collaborators can review your proposed changes and decide whether or not to incorporate (pull in) your changes.


### Pull Request Pro Tips  

* [Fork](http://guides.github.com/activities/forking/) the repository and [clone](https://help.github.com/articles/cloning-a-repository/) it locally.
Connect your local repository to the original `upstream` repository by adding it as a [remote](https://help.github.com/articles/adding-a-remote/).
Pull in changes from `upstream` often so that you stay up to date and so when you submit your pull request,
merge conflicts will be less likely. See more detailed instructions [here](https://help.github.com/articles/syncing-a-fork).
* Create a [branch](http://guides.github.com/introduction/flow/) for your edits.
* Contribute in the style of the project as outlined above. This makes it easier for the collaborators to merge 
and for others to understand and maintain in the future.

### Open Pull Requests

Once you've opened a pull request, a discussion will start around your proposed changes.

Other contributors and users may chime in, but ultimately the decision is made by the collaborators.

During the discussion, you may be asked to make some changes to your pull request.

If so, add more commits to your branch and push them -- they will automatically go into the existing pull request!

Opening a pull request will trigger a Travis CI build to check the validity of all links in the project. After the build completes, please ensure that the build has passed. Otherwise, view the Travis CI log and see what errors the build found for your contribution. If the build error is not related to your link(s), don't worry! Your pull request will not be delayed because of already existing link causing an error.