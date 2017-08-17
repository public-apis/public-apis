 function loadJSON(callback) {   
    var xobj = new XMLHttpRequest();
        xobj.overrideMimeType("application/json");
    xobj.open('GET', 'https://raw.githubusercontent.com/toddmotto/public-apis/master/json/entries.min.json', true); // Replace 'my_data' with the path to your file
    xobj.onreadystatechange = function () {
          if (xobj.readyState == 4 && xobj.status == "200") {
            // Required use of an anonymous callback as .open will NOT return a value but simply returns undefined in asynchronous mode
            callback(xobj.responseText);
          }
    };
    xobj.send(null);  
 }

function filterRows() {

  	var input, filter, table, tr, td, i;

  	input = document.getElementById("searchbox");
  	filter = input.value.toUpperCase();
  	table = document.getElementById("entries");
  	tr = table.getElementsByTagName("tr");

  	// Loop through all table rows and hide those who don't match the search
  	for (i = 0; i < tr.length; i++) {
  		
  		displayRows = false;

    	title = tr[i].getElementsByTagName("td")[0];
    	if (title) {
    		if (title.innerHTML.toUpperCase().indexOf(filter) > -1) {
    			displayRows = true;
    		}
		}
		section = tr[i].getElementsByTagName("td")[4];
		if (section) {
			if (section.innerHTML.toUpperCase().indexOf(filter) > -1) {
    			displayRows = true;
    		}
		}
		if (displayRows) {
			tr[i].style.display = "";
		} else {
			tr[i].style.display = "none";
		}
	}
}

loadJSON(function(response) {
	var items = JSON.parse(response);
	new Vue({
		data: {
			filter: ''
		},
		computed: {
			data() {
				let output = [];
				for (var category in items) {
					for (var api in items[category]) {
						items[category][api].Category = category;
						output.push(items[category][api]);
					}
				}
				return output;
			}
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
								$( "th" ).addClass( "lol" );
							}
						}
						
					});
				}
				return show;
			}
		}
	}).$mount('#app');
});
