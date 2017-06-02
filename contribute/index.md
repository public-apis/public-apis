---
layout: default
---

#### How to Contribute 

```
{name: Demo,   
description: "What is it?",  
auth: "No",  
link: http://yada-yada.com,  
category:[one, or, more, categories]}  
```

#### Category Reference  
Use one or more of the category names in the table below in your API entry.  The name is used to link your entry to the categories and the slug is what actually shows in the site.  If your category does not exist, you may need to add an entry to the tags.json file. 


| Entry name | Display Name |  
| --------------- | ------------------- |   {% for tag in site.data.tags.tags %}
| {{ tag.name }} | {{ tag.display }} |  {% endfor %}
