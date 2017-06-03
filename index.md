---
layout: default
---

<div class="page-head">
<h2> Public APIs</h2>  
A collective list of free JSON APIs for use in web development.  
<br>  
For information on contributing to this project, please see the <a href="{{ base.url }}/contribute">contributing guide</a>.
</div>

<!-- search input results -->
<form>
<div id="search-wrapper" class="form-group">
	<label for="jetsSearch">
	  <i class="search icon"></i>
	</label>
	<input type="search" class="form-control" id="jetsSearch" placeholder="Search APIs" autocomplete="off" spellcheck="false" tabindex="0">
</div>
 </form>
 
<br>

<div class="container">

<div class="row">
<table class="table table-hover col-sm-12">
  <thead>
	<tr class="tbl-head">
	  <td>API</td>
	  <td>Description</td>
	  <td>Authorization</td>
	  <td>Category</td>
	</tr>
  </thead>
  <tbody id="jetsContent">
 
{% assign apilist = site.data.apis.apis | sort: 'category' %}
{% for api in apilist %}
	<tr>
		<td><a href="{{ api.link }}"> {{ api.name }} </a></td>
		<td>{{ api.description }}</td>
		<td>{{ api.auth }}</td>
		<td>{{ api.category }} </td>
	</tr> 
{% endfor %}
  </tbody>
</table>
</div>
</div>


<script type="text/javascript">
var jets = new Jets({
  searchTag: '#jetsSearch',
  contentTag: '#jetsContent',
  columns: [0,1,3], 
});
</script>

