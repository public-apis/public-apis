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
