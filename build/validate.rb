#!/usr/bin/env ruby

args = ARGV
filename = args[0]

File.foreach(filename).with_index do |line, line_num|
    line_num += 1
#  puts "#{line_num}: #{line}"
    if line.start_with?('|')
        # Skip table schema lines
        if line.eql? "|---|---|---|---|---|\n"
            next
        end

        values = line.split("|")
        values.each.with_index do |v, vn|
            puts "#{vn}: #{v}"
        end
    end
end
