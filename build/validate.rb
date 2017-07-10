#!/usr/bin/env ruby
auth_keys = ['apiKey', 'OAuth', 'X-Mashape-Key', 'No']

args = ARGV
filename = args[0]

fail_flag = false
fail_count = 0
File.foreach(filename).with_index do |line, line_num|
    line_num += 1
#  puts "#{line_num}: #{line}"
    if line.start_with?('|')
        # Skip table schema lines
        if line.eql? "|---|---|---|---|---|\n"
            next
        end

        values = line.split("|")
        # Check Auth Values to conform to valid options only
        auth_val = values[3].lstrip.chop.tr('``', '')
        if !auth_keys.include? auth_val
         puts "(#{line_num}) Invalid Auth (#{auth_val}): #{line}"
         fail_flag = false
         fail_count += 1
        end
    end
end
