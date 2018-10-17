# Contributing to public-apis

> While the masses of pull requests and community involvement is appreciated, some pull requests have been specifically
opened to market company APIs that offer paid solutions. This API list is not a marketing tool, but a tool to help the
community build applications and use free, public APIs quickly and easily. Pull requests that are identified as marketing attempts will not be accepted.
>
> Thanks for understanding! :)

## Formatting

Current API entry format:

| API | Description | Auth | HTTPS | CORS |
| --- | --- | --- | --- | --- |
| API Title(Link to API webpage) | Description of API | Does this API require authentication? * | Does the API support HTTPS? | Does the API support [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)? * |

Example entry:

```
| [NASA](https://api.nasa.gov) | NASA data, including imagery | No | Yes | Yes |
```

\* Currently, the only accepted inputs for the `Auth` field are as follows:

* `OAuth` - _the API supports OAuth_
* `apiKey` - _the API uses a private key string/token for authentication - try and use the correct parameter_
* `X-Mashape-Key` - _the name of the header which may need to be sent_
* `No` - _the API requires no authentication to run_

\* Currently, the only accepted inputs for the `CORS` field are as follows:

* `Yes` - _the API supports CORS_
* `No` - _the API does not support CORS_
* `Unknown` - _it is unknown if the API supports CORS_

Please continue to follow the alphabetical ordering that is in place per section. Each table column should be padded with one space on either side.

If an API seems to fall into multiple categories, please place the listing within the section most in line with the services offered through the API. For example, the Instagram API is listed under `Social` since it is mainly a social network, even though it could also apply to `Photography`.

## Pull Request

After you've created a branch on your fork with your changes, it's time to [make a pull request][pr-link]!

Once you’ve submitted a pull request, the collaborators can review your proposed changes and decide whether or not to incorporate (pull in) your changes.

### Pull Request Pro Tips

* [Fork][fork-link] the repository and [clone][clone-link] it locally.
Connect your local repository to the original `upstream` repository by adding it as a [remote][remote-link].
Pull in changes from `upstream` often so that you stay up to date and so when you submit your pull request,
merge conflicts will be less likely. See more detailed instructions [here][syncing-link].
* Create a [branch][branch-link] for your edits.
* Contribute in the style of the project as outlined above. This makes it easier for the collaborators to merge
and for others to understand and maintain in the future.
* Please make sure you squash all commits together before opening a pull request. If your pull request requires changes upon review, please be sure to squash all additional commits as well. [This wiki page][squash-link] outlines the squash process.

### Open Pull Requests

Once you’ve opened a pull request, a discussion will start around your proposed changes.

Other contributors and users may chime in, but ultimately the decision is made by the collaborators.

During the discussion, you may be asked to make some changes to your pull request.

If so, add more commits to your branch and push them – they will automatically go into the existing pull request!

Opening a pull request will trigger a Travis CI build to check the validity of all links in the project. After the build completes, **please ensure that the build has passed**. If the build did not pass, please view the Travis CI log and correct any errors that were found in your contribution. 

Thanks for being a part of this project, and we look forward to hearing from you soon! 

[branch-link]: <http://guides.github.com/introduction/flow/>
[clone-link]: <https://help.github.com/articles/cloning-a-repository/>
[fork-link]: <http://guides.github.com/activities/forking/>
[oauth-link]: <https://en.wikipedia.org/wiki/OAuth>
[pr-link]: <https://help.github.com/articles/creating-a-pull-request/>
[remote-link]: <https://help.github.com/articles/configuring-a-remote-for-a-fork/>
[syncing-link]: <https://help.github.com/articles/syncing-a-fork>
[squash-link]: <https://github.com/todotxt/todo.txt-android/wiki/Squash-All-Commits-Related-to-a-Single-Issue-into-a-Single-Commit>

