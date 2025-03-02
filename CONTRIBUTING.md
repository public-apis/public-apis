# 🚀 Contributing to Public APIs

> 💡 **Note:** While community contributions are highly appreciated, some pull requests are created solely to market company APIs offering paid solutions. **This API list is NOT a marketing tool!** It exists to help developers find free, public APIs quickly and easily. Any PR identified as marketing will **not be accepted.**

✅ **Ensure the API you add has full free access or at least a free tier and does not require purchasing a device/service.** Example: An API controlling a smart outlet would be **rejected** because, while free, it requires a paid device.

🙏 Thanks for understanding! 😊

---

## 📝 Formatting Guidelines

🔹 **API Entry Format:**

| 🌐 API | 📜 Description | 🔑 Auth | 🔒 HTTPS | 🔄 CORS | 🚀 Call this API |
| --- | --- | --- | --- | --- | --- |
| [API Title](Link to API documentation) | Short API description | Authentication method* | Supports HTTPS? | Supports [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)?* | [Run in Postman Button] |

📌 **Example Entry:**
```
| [NASA](https://api.nasa.gov) | NASA data, including imagery | No | Yes | Yes | [Run in Postman Button] |
```

📌 **Accepted Inputs for `Auth` Field:**

- 🔐 `OAuth` - Supports OAuth
- 🔑 `apiKey` - Requires a private key/token
- 🗝️ `X-Mashape-Key` - Header name that must be sent
- ❌ `No` - No authentication required
- 👤 `User-Agent` - Must send this header

📌 **Accepted Inputs for `CORS` Field:**

- ✅ `Yes` - API supports CORS
- ❌ `No` - API does not support CORS
- 🤷 `Unknown` - Not sure if API supports CORS

🔹 **For the "Call this API" column, provide a Postman collection link**. If needed, create one: [Guide](https://learning.postman.com/docs/getting-started/first-steps/creating-the-first-collection/).

⚠️ **Without proper [CORS configuration](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS), an API will only work server-side.**

---

## 🔄 Submitting a Pull Request (PR)

📢 **Follow these rules when making a PR:**

✔ **Keep API listings alphabetically ordered within each category.**
✔ **Use a concise description (max 100 characters).**
✔ **If an API fits multiple categories, place it in the most relevant one.**
✔ **Add only one API per PR.**
✔ **Use the PR title format:** `Add [API Name] API` (e.g., `Add Blockchain API`).
✔ **Write a clear commit message:**
   - ❌ `Update Readme.md`
   - ✔ `Add Blockchain API to Cryptocurrency`
✔ **Check for duplicate PRs before submitting.**
✔ **Omit the TLD (e.g., Gmail.com ❌ → Gmail ✔).**
✔ **Avoid adding "API" at the end of the name (e.g., Gmail API ❌ → Gmail ✔).**
✔ **Ensure proper documentation is available.**
✔ **Squash all commits before submitting a PR.** [Guide](https://github.com/todotxt/todo.txt-android/wiki/Squash-All-Commits-Related-to-a-Single-Issue-into-a-Single-Commit).
✔ **Target your PR to the `master` branch.**

🔄 **After submitting, collaborators will review and decide on your changes.**

---

## 🛠️ Pro Tips for PRs

🔹 **Best practices to ensure smooth contributions:**

1. 🍴 [Fork](http://guides.github.com/activities/forking/) the repository and [clone](https://help.github.com/articles/cloning-a-repository/) it locally.
2. 🔄 Add the original repository as an [upstream remote](https://help.github.com/articles/configuring-a-remote-for-a-fork/).
3. 🆙 Regularly **pull updates** from upstream to avoid merge conflicts. [Guide](https://help.github.com/articles/syncing-a-fork)
4. 🌿 Create a new [branch](http://guides.github.com/introduction/flow/) for your changes.
5. 🏗️ Follow the project’s style and formatting for better readability.

---

## 🚀 After Opening a PR

🔹 **What happens next?**

✔ 🎉 A discussion starts around your proposed changes.
✔ 👥 Other contributors may provide feedback.
✔ 🔄 If changes are needed, update your branch and **push again** (no need for a new PR).
✔ ✅ Ensure **the build passes** (all links in the project are valid).
✔ 🛠️ Check logs if the build fails and fix any issues.

🙌 **Thanks for being a part of this project! Looking forward to your contributions!** 🚀✨

---

🔗 **Useful Links:**
- [Forking Guide](http://guides.github.com/activities/forking/)
- [Cloning a Repository](https://help.github.com/articles/cloning-a-repository/)
- [PR Guide](https://help.github.com/articles/creating-a-pull-request/)
- [Squash Commits](https://github.com/todotxt/todo.txt-android/wiki/Squash-All-Commits-Related-to-a-Single-Issue-into-a-Single-Commit)

🔥 Happy Coding! 🚀

