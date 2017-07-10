#!/usr/bin/env ruby
auth_keys = ['apiKey', 'OAuth', 'X-Mashape-Key', 'No']
https_keys = ['Yes', 'No']

args = ARGV
filename = args[0]

fail_flag = false
File.foreach(filename).with_index do |line, line_num|
    line_num += 1
#  puts "#{line_num}: #{line}"
    if line.start_with?('|')
        # Skip table schema lines
        if line.eql? "|---|---|---|---|---|\n"
            next
        end
        values = line.split("|")

        # Check Auth values to conform to valid options only
        auth_val = values[3].lstrip.chop.tr('``', '')
        if !auth_keys.include?(auth_val)
         puts "(#{line_num}) Invalid Auth (not a valid option): #{auth_val}"
         fail_flag = true
        end

        # Check HTTPS Support values to be either "Yes" or "No"
        https_val = values[4].lstrip.chop
        if !https_keys.include?(https_val)
         puts "(#{line_num}) Invalid HTTPS: (must use \"Yes\" or \"No\"): #{https_val}"
         fail_flag = true
        end
    end
end
