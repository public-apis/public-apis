new Vue({
	data: {
		filter: '',
		items: ''
	},
	created() {
		fetch('https://raw.githubusercontent.com/toddmotto/public-apis/master/json/entries.min.json')
		.then(data => data.json())
		.then(data => {
			this.items = data.entries;
		})
	},
	methods: {
		filtered(item) {
			let show = true;

			if(this.filter.length) {
				
				show = false;

				let filterKeyword = this.filter.toLowerCase();

				Object.keys(item).map(function(key) {
					if(typeof item[key] === 'string') {
						let value = item[key].toString().toLowerCase();
						
						if(value.includes(filterKeyword)) {
							show = true;
						}
					}
				});
			}
			return show;
		}
	}
}).$mount('#app');

function filterRows() {
  var input, filter, table, tr, td, i;
  input = document.getElementById("searchbox");
  filter = input.value.toUpperCase();
  table = document.getElementById("entries");
  tr = table.getElementsByTagName("tr");

  // Loop through all table rows and hide those who don't match the search
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[0];
    if (td) {
      if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    } 
  }
}