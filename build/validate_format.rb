#!/usr/bin/env ruby
auth_keys = ['apiKey', 'OAuth', 'X-Mashape-Key', 'No']
punctuation = ['.', '?', '!']
https_keys = ['Yes', 'No']
args = ARGV
filename = args[0]
fail_flag = false
File.foreach(filename).with_index do |line, line_num|
    line_num += 1
    if line.start_with?('|')
        # Skip table schema lines
        if line.eql? "|---|---|---|---|---|\n"
            next
        end
        values = line.split("|")
        ################# DESCRIPTION ################
        # First character should be capitalized
        desc_val = values[2].lstrip.chop
        if !/[[:upper:]]/.match(desc_val[0])
            puts "(#{line_num}) Invalid Description (first char not uppercase): #{desc_val}"
            fail_flag = true
        end
        # value should not be punctuated
        last_char = desc_val[desc_val.length-1]
        if punctuation.include?(last_char)
            puts "(#{line_num}) Invalid Description (description should not end with \"#{last_char}\")"
            fail_flag = true
        end
        #################### AUTH ####################
        # Values should conform to valid options only
        auth_val = values[3].lstrip.chop.tr('``', '')
        if !auth_keys.include?(auth_val)
            puts "(#{line_num}) Invalid Auth (not a valid option): #{auth_val}"
            fail_flag = true
        end
        #################### HTTPS ###################
        # Values should be either "Yes" or "No"
        https_val = values[4].lstrip.chop
        if !https_keys.include?(https_val)
            puts "(#{line_num}) Invalid HTTPS: (must use \"Yes\" or \"No\"): #{https_val}"
            fail_flag = true
        end
        #################### LINK ####################
        # Url should be wrapped in "[Go!]" view
        link_val = values[5].lstrip.chop
        if !link_val.start_with?("[Go!](") || !link_val.end_with?(')')
            puts "(#{line_num}) Invalid Link: (format should be \"[Go!](<LINK>)\"): #{link_val}"
            fail_flag = true
        end
    end
end
if fail_flag
    exit(1)
else
    exit(0)
end
