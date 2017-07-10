#!/usr/bin/env ruby
args = ARGV
filename = args[0]

File.foreach(filename).with_index do |line, line_num|
    line_num += 1
    puts "#{line_num}: #{line}"

end
