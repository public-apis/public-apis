fs = require('fs')

function setupMd(filename, anchor) {
    fs.readFile(filename, 'utf8', function (err,text) {
      if (err) {
        return console.log(err);
      }
    var lines = text.split("\n"),
        cur_line = 0,
        line = "",
        table_name = "",
        col_num = 0,
        cols = [],
        rows = [],
        arr = [];


    function read_line() {
        return lines[cur_line++];
    }

    while (true) {
        var cols = [];
        var rows = [];
        while (line.indexOf(anchor) == -1 && cur_line != lines.length) {
            line = read_line();
        }
        if (cur_line == lines.length) {
            break;
        }
        table_name = line.split(anchor)[1];
        read_line()
        read_line()
        while (true) {
        	line = read_line()
        	if (line.length < 2 || cur_line == lines.length) {
        		break
        	}
			if (line.indexOf("|") == 0) {
				arr.push(line + table_name)
			} 
        }

    }
    console.log(anchor + " entries")
    console.log("API | Description | Auth | HTTPS | Link | Section")
    console.log("|---|---|---|---|---|---|")
    for (i = 0; i < arr.length; i++) {
    	console.log(arr[i])
    }
  });
}

if (process.argv.length < 3) {
    console.log("No .md file passed!");
    return;
}
if (process.argv.length < 4) {
  anchorText = "###";
} else {
  anchorText = process.argv[3];
}
setupMd(process.argv[2].toString(), anchorText);
